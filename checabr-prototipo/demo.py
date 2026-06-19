"""Demo de ponta a ponta. Lê uma transcrição fictícia e imprime os cartões de
overlay que apareceriam na tela. Roda sem chave (modo offline de demonstração);
com ANTHROPIC_API_KEY + `pip install anthropic`, usa o Claude de verdade.

Uso:  python demo.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from checabr.pipeline import Pipeline, extrair_afirmacoes  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
EMOJI = {"verde": "🟢", "amarelo": "🟡", "laranja": "🟠", "vermelho": "🔴", "cinza": "⚪"}


def main():
    pipe = Pipeline(
        os.path.join(BASE, "data", "checagens_mock.json"),
        os.path.join(BASE, "data", "fontes_primarias_mock.json"),
    )
    print("ChecaBR — protótipo do núcleo de verificação")
    print("Motor de raciocínio:", getattr(pipe.reasoner, "nome", type(pipe.reasoner).__name__))
    print("=" * 78)

    with open(os.path.join(BASE, "data", "transcript_exemplo.txt"), encoding="utf-8") as f:
        linhas = [l for l in f if l.strip() and not l.lstrip().startswith("#")]

    for i, linha in enumerate(linhas):
        for af in extrair_afirmacoes(linha, i):
            ver = pipe.verificar(af)
            c = pipe.montar_cartao(af, ver)
            print(f"\n[{c.t}] {c.orador}: {c.afirmacao}")
            print(f"   {EMOJI[c.cor]} {c.grau}  ·  confiança {c.confianca}  ·  {c.selo}")
            print(f"   ↳ {c.contexto}")
            if c.fontes and c.fontes[0]:
                print(f"   Fontes: {'; '.join(c.fontes)}")
    print("\n" + "=" * 78)
    print("Aviso: dados de exemplo são ILUSTRATIVOS (mock). Não use como checagem real.")


if __name__ == "__main__":
    main()
