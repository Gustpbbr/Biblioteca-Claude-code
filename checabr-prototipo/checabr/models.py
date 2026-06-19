"""Tipos de dados do núcleo de checagem."""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class TipoAfirmacao(str, Enum):
    FACTUAL = "FACTUAL"        # afirmação de fato, verificável
    OPINIAO = "OPINIAO"        # juízo de valor — não se checa
    PROMESSA = "PROMESSA"      # promessa de campanha — não se checa (ainda)
    PREVISAO = "PREVISAO"      # previsão de futuro — não se checa


class Grau(str, Enum):
    VERDADEIRO = "VERDADEIRO"
    ENGANOSO = "ENGANOSO"               # parcialmente verdade, induz a erro
    FORA_DE_CONTEXTO = "FORA_DE_CONTEXTO"
    FALSO = "FALSO"
    INSUFICIENTE = "INSUFICIENTE"       # sem fonte suficiente para decidir
    NAO_VERIFICAVEL = "NAO_VERIFICAVEL"  # opinião/promessa/previsão


# Cor do selo no overlay (semáforo)
COR = {
    Grau.VERDADEIRO: "verde",
    Grau.ENGANOSO: "amarelo",
    Grau.FORA_DE_CONTEXTO: "laranja",
    Grau.FALSO: "vermelho",
    Grau.INSUFICIENTE: "cinza",
    Grau.NAO_VERIFICAVEL: "cinza",
}


@dataclass
class Evidencia:
    fonte: str
    tipo_fonte: str           # CHECADORA_HUMANA | FONTE_PRIMARIA | BUSCA_WEB
    trecho: str
    url: str = ""
    data: str = ""
    grau_sugerido: Optional[str] = None


@dataclass
class Afirmacao:
    id: str
    texto: str
    tipo: TipoAfirmacao
    orador: str = ""
    t: str = ""               # timestamp na transmissão (mm:ss)


@dataclass
class Veredito:
    grau: Grau
    confianca: float          # 0..1
    resumo: str
    evidencias: List[Evidencia] = field(default_factory=list)
    verificado_por_humano: bool = False
    origem: str = "automatica"  # humana | automatica | n/a


@dataclass
class CartaoOverlay:
    """Saída pronta para o renderizador do overlay."""
    afirmacao: str
    orador: str
    t: str
    grau: str
    cor: str
    confianca: float
    selo: str
    contexto: str
    fontes: List[str]
