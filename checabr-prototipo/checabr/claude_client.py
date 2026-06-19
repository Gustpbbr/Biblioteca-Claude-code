"""Motor de raciocínio. Usa a API do Claude quando há ANTHROPIC_API_KEY + SDK;
caso contrário, cai num motor offline determinístico só para demonstrar o fluxo.

Modelos recomendados (latência x qualidade, ids reais):
- Extração de afirmações em tempo real: claude-haiku-4-5-20251001 (rápido/barato)
- Veredito: claude-sonnet-4-6 (equilíbrio) ou claude-opus-4-8 (casos difíceis)
"""
import json
import os
from typing import List

from .models import Afirmacao, Evidencia, Grau, Veredito
from .prompts import SYSTEM_VEREDITO


class OfflineReasoner:
    """Sem chave/SDK: apenas formata o grau sugerido pela evidência recuperada.
    NÃO é raciocínio real — serve só para o protótipo rodar de ponta a ponta."""
    nome = "offline (sem ANTHROPIC_API_KEY) — demonstração do fluxo, não é checagem real"

    def julgar(self, af: Afirmacao, evid: List[Evidencia]) -> Veredito:
        sugeridos = [e.grau_sugerido for e in evid if e.grau_sugerido]
        if sugeridos:
            # escolhe o grau mais conservador disponível
            ordem = [Grau.FALSO, Grau.FORA_DE_CONTEXTO, Grau.ENGANOSO, Grau.VERDADEIRO]
            grau = next((g for g in ordem if g.value in sugeridos), Grau(sugeridos[0]))
            return Veredito(grau=grau, confianca=0.6, resumo=evid[0].trecho,
                            evidencias=evid, origem="automatica")
        return Veredito(grau=Grau.INSUFICIENTE, confianca=0.2,
                        resumo="Não foram encontradas fontes suficientes para verificar automaticamente.",
                        evidencias=evid, origem="automatica")


class ClaudeReasoner:
    """Raciocínio real via API do Claude."""

    def __init__(self, model: str = "claude-haiku-4-5-20251001"):
        import anthropic
        self.client = anthropic.Anthropic()
        self.model = model
        self.nome = f"Claude API ({model})"

    def julgar(self, af: Afirmacao, evid: List[Evidencia]) -> Veredito:
        ctx = "\n".join(
            f"- ({e.tipo_fonte}) {e.fonte}: {e.trecho} [{e.url}]" for e in evid
        ) or "Nenhuma evidência recuperada."
        msg = self.client.messages.create(
            model=self.model, max_tokens=600, system=SYSTEM_VEREDITO,
            messages=[{"role": "user",
                       "content": f'AFIRMAÇÃO: "{af.texto}"\n\nEVIDÊNCIAS:\n{ctx}\n\nClassifique.'}],
        )
        txt = msg.content[0].text
        data = json.loads(txt[txt.find("{"): txt.rfind("}") + 1])
        return Veredito(grau=Grau(data["grau"]), confianca=float(data["confianca"]),
                        resumo=data["resumo"], evidencias=evid, origem="automatica")


def get_reasoner():
    import importlib.util
    if os.getenv("ANTHROPIC_API_KEY") and importlib.util.find_spec("anthropic"):
        return ClaudeReasoner()
    return OfflineReasoner()
