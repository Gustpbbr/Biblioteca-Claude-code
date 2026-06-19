# ChecaBR — protótipo

Núcleo de **verificação de fatos em tempo real** para cobertura eleitoral (Brasil 2026).
Abordagem **híbrida**: usa checagem humana quando ela existe; quando não existe, faz
checagem **automática** com o Claude + fontes primárias, sempre **rotulada como tal**.

> ⚠️ Protótipo. Os dados em `data/` são **ilustrativos (mock)**. Não use como checagem real.

## Por que existe
O produto "viral" que motivou isto **não foi encontrado de forma pública/verificável**.
A categoria existe lá fora (Factiverse, CheckMate/BBC, FactCheck for YouTube…), mas no
Brasil a checagem é feita por **consulta/monitoramento** (chatbot Fátima/Aos Fatos, Lupa,
Comprova) — **não há overlay ao vivo sobre vídeo**. Esse é o nicho.

## O que este protótipo É e NÃO é
- **É:** o *cérebro* reaproveitável — transcrição → afirmações → veredito → cartão de overlay.
- **Não é:** a captura de TV nem o renderizador do overlay (a "casca" de infra — ver abaixo).

## Rodar
```bash
cd checabr-prototipo
python demo.py
```
Roda **sem chave** (motor offline de demonstração). Para usar o Claude de verdade:
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python demo.py
```

## Arquitetura do núcleo (`checabr/`)
```
transcrição ─▶ extrair_afirmacoes ─▶ classificar (FACTUAL/OPINIAO/PROMESSA/PREVISAO)
                                          │
                       ┌──────────────────┴───────────────────┐
                 não verificável                          FACTUAL
              (opinião/promessa)                              │
                       │                       1) há checagem HUMANA? (Aos Fatos/Lupa/Comprova)
                  cartão cinza                     │ sim ──▶ veredito humano  ✔
                                                   │ não
                                          2) checagem AUTOMÁTICA (Claude + fontes primárias)
                                                       └──▶ veredito automático  ⚠ (rotulado)
                                          ─▶ CartaoOverlay (grau, cor, confiança, selo, fonte)
```
Arquivos: `models.py` (tipos) · `prompts.py` (system prompts — **neutralidade**) ·
`sources.py` (recuperação) · `claude_client.py` (Claude / offline) · `pipeline.py` (orquestra).

## A casca: overlay de TV ao vivo (alvo escolhido)
O núcleo acima é alimentado por este pipeline de produção:
1. **Captura** do sinal (SDI/HDMI/stream) → áudio.
2. **ASR streaming** (transcrição contínua com timestamps; ex.: Whisper streaming).
3. **Buffer de afirmações** + workers assíncronos chamando o núcleo (latência ~poucos s).
4. **Renderizador de overlay** (ex.: OBS / vMix / lower-third via NDI) consumindo os
   `CartaoOverlay` em JSON.
5. **Painel do editor humano** para aprovar/segurar cartões sensíveis antes do ar
   (recomendado fortemente em ano eleitoral).

## Princípios de neutralidade (inegociáveis)
- Trata todos os candidatos/partidos igual; avalia **conteúdo**, não pessoa; não infere intenção.
- Só classifica **fato verificável**; opinião/promessa/previsão → `NAO_VERIFICAVEL`.
- **Fonte sempre**; sem evidência suficiente → `INSUFICIENTE` (admite incerteza).
- Na dúvida, grau **mais conservador**. A ferramenta é ponto de partida, não árbitro.

## Cuidados legais (Brasil eleitoral)
- Respeitar resoluções do **TSE** sobre IA em contexto eleitoral (rotulagem, deepfake, responsabilidade).
- **Responsabilidade civil:** selo errado em candidato = risco de processo → revisão humana no ar.
- **Transparência:** publicar metodologia, fontes e taxa de erro; permitir contestação/correção.
- **Proteção contra manipulação** das fontes e do próprio sistema.

## Roadmap
- [ ] Substituir mocks por conectores reais (Aos Fatos/Lupa/Comprova; TSE/IBGE/Transparência).
- [ ] Extração/classificação via Claude (`SYSTEM_EXTRACAO`) + ASR streaming.
- [ ] Embeddings para casar afirmação ↔ checagem (hoje é Jaccard simples).
- [ ] Calibração de confiança + avaliação com conjunto rotulado (precisão/recall por grau).
- [ ] Painel do editor + renderizador de overlay.
- [ ] Auditoria de neutralidade (testes adversariais balanceados entre lados).

## Modelos (latência × qualidade)
- Extração em tempo real: `claude-haiku-4-5-20251001`
- Veredito: `claude-sonnet-4-6` (equilíbrio) ou `claude-opus-4-8` (casos difíceis)
