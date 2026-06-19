"""Recuperação de evidências.

Em produção, estes adaptadores conversam com:
- Bases de checadoras humanas (Aos Fatos, Agência Lupa, AFP, Projeto Comprova) via API/scrape autorizado.
- Fontes primárias: TSE, IBGE, Diário Oficial, Portal da Transparência, SICONFI, leis.
- Busca web com recuperação + reranking.

Aqui usamos mocks locais (JSON) só para o protótipo rodar e demonstrar o fluxo.
"""
import json
import re
from typing import List, Optional, Tuple

from .models import Evidencia


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9çãõáéíóúâêôà ]", "", s.lower())


class BaseChecagensHumanas:
    """Procura uma checagem humana já existente para a afirmação."""

    def __init__(self, caminho: str, limiar: float = 0.35):
        with open(caminho, encoding="utf-8") as f:
            self.itens = json.load(f)
        self.limiar = limiar

    def buscar(self, texto: str) -> Tuple[Optional[dict], float]:
        toks = set(_norm(texto).split())
        if not toks:
            return None, 0.0
        melhor, best = None, 0.0
        for it in self.itens:
            a = set(_norm(it["afirmacao"]).split())
            if not a:
                continue
            jac = len(toks & a) / len(toks | a)
            if jac > best:
                best, melhor = jac, it
        return (melhor, best) if best >= self.limiar else (None, best)


class RecuperadorFontesPrimarias:
    """STUB de demonstração. Substituir por conectores reais (TSE/IBGE/busca)."""

    def __init__(self, caminho_mock: str):
        with open(caminho_mock, encoding="utf-8") as f:
            self.mock = json.load(f)

    def buscar(self, texto: str) -> List[Evidencia]:
        t = _norm(texto)
        out: List[Evidencia] = []
        for m in self.mock:
            if any(g in t for g in m["gatilhos"]):
                out.append(Evidencia(
                    fonte=m["fonte"], tipo_fonte=m["tipo_fonte"], trecho=m["trecho"],
                    url=m.get("url", ""), data=m.get("data", ""),
                    grau_sugerido=m.get("grau_sugerido"),
                ))
        return out
