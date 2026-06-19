"""Orquestração: transcrição -> afirmações -> veredito híbrido -> cartão de overlay."""
import re
from typing import List

from .models import (Afirmacao, CartaoOverlay, COR, Evidencia, Grau,
                     TipoAfirmacao, Veredito)
from .sources import BaseChecagensHumanas, RecuperadorFontesPrimarias
from .claude_client import get_reasoner

# Heurística simples de classificação (no protótipo offline). Em produção,
# a extração/classificação é feita pelo SYSTEM_EXTRACAO via Claude.
OPINIAO_KW = ("melhor", "pior", "acho", "acredito", "na minha opiniao",
              "maravilhoso", "pessimo", "incompetente", "vergonha")
PROMESSA_KW = ("vou ", "irei ", "vamos ", "prometo", "no meu mandato",
               "no meu governo eu vou", "pretendo")


def classificar(texto: str) -> TipoAfirmacao:
    t = texto.lower()
    if any(k in t for k in PROMESSA_KW):
        return TipoAfirmacao.PROMESSA
    if any(k in t for k in OPINIAO_KW):
        return TipoAfirmacao.OPINIAO
    return TipoAfirmacao.FACTUAL


def extrair_afirmacoes(linha_transcript: str, idx: int) -> List[Afirmacao]:
    """Formato esperado: '[mm:ss] Orador: texto'. Quebra em sentenças."""
    m = re.match(r"\[(.*?)\]\s*(.*?):\s*(.*)", linha_transcript.strip())
    if m:
        t, orador, texto = m.group(1), m.group(2), m.group(3)
    else:
        t, orador, texto = "", "", linha_transcript.strip()
    out = []
    for j, frase in enumerate(re.split(r"(?<=[.!?])\s+", texto)):
        frase = frase.strip()
        if len(frase) < 6:
            continue
        out.append(Afirmacao(id=f"{idx}.{j}", texto=frase,
                             tipo=classificar(frase), orador=orador, t=t))
    return out


class Pipeline:
    def __init__(self, base_humana: str, fontes_primarias: str):
        self.humanas = BaseChecagensHumanas(base_humana)
        self.primarias = RecuperadorFontesPrimarias(fontes_primarias)
        self.reasoner = get_reasoner()

    def verificar(self, af: Afirmacao) -> Veredito:
        # 1) Não-checáveis (opinião / promessa / previsão)
        if af.tipo in (TipoAfirmacao.OPINIAO, TipoAfirmacao.PROMESSA, TipoAfirmacao.PREVISAO):
            rotulo = {"OPINIAO": "Opinião", "PROMESSA": "Promessa de campanha",
                      "PREVISAO": "Previsão"}[af.tipo.value]
            return Veredito(grau=Grau.NAO_VERIFICAVEL, confianca=1.0,
                            resumo=f"{rotulo} — não é afirmação factual verificável.",
                            origem="n/a")
        # 2) Existe checagem humana? (caminho preferencial — mais defensável)
        item, score = self.humanas.buscar(af.texto)
        if item:
            ev = [Evidencia(fonte=item["fonte"], tipo_fonte="CHECADORA_HUMANA",
                            trecho=item["resumo"], url=item.get("url", ""),
                            data=item.get("data", ""))]
            return Veredito(grau=Grau(item["grau"]), confianca=min(0.95, 0.6 + score),
                            resumo=item["resumo"], evidencias=ev,
                            verificado_por_humano=True, origem="humana")
        # 3) Checagem automática (Claude + fontes primárias) — claramente rotulada
        evid = self.primarias.buscar(af.texto)
        return self.reasoner.julgar(af, evid)

    def montar_cartao(self, af: Afirmacao, ver: Veredito) -> CartaoOverlay:
        if ver.origem == "humana":
            selo = f"✔ Checado por {ver.evidencias[0].fonte}"
        elif ver.origem == "automatica":
            selo = "⚠ Checagem automática — não verificada por humano"
        else:
            selo = "ⓘ Não verificável"
        return CartaoOverlay(
            afirmacao=af.texto, orador=af.orador, t=af.t, grau=ver.grau.value,
            cor=COR[ver.grau], confianca=round(ver.confianca, 2), selo=selo,
            contexto=ver.resumo,
            fontes=[f"{e.fonte} {e.url}".strip() for e in ver.evidencias],
        )
