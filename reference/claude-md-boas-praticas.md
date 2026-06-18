# ⚡ CLAUDE.md — boas práticas (anti-maus-hábitos)

Princípios para um `CLAUDE.md` que corrige os vícios comuns de agentes de código.

> **Origem:** projeto `forrestchang` (CLAUDE.md inspirado nas observações do Andrej
> Karpathy sobre como LLMs escrevem código; ~78,5k⭐, instalável via curl no `~/.claude`).
> Capturado de conteúdo de rede social — **confira o repositório oficial** antes de
> copiar literalmente. Os princípios abaixo são gerais e seguros.

## Os 4 princípios

1. **Explicite suas suposições** — não escolha uma interpretação em silêncio. Se a
   tarefa tem várias leituras, diga. Em dúvida, pergunte. Aponte inconsistências e
   discorde quando algo não fizer sentido, em vez de tocar um plano ruim.

2. **Código mínimo viável** — sem features especulativas, sem abstração para código
   de uso único, sem "flexibilidade" que ninguém pediu. Se escreveu 200 linhas e 50
   resolveriam, reescreva. Pergunte-se: um engenheiro sênior chamaria isto de
   "complicado demais"?

3. **Mudanças cirúrgicas** — não toque em código que você não entende totalmente,
   não refatore coisas não relacionadas como efeito colateral, não apague comentários
   só porque "parecem" desnecessários. Mude só o que a tarefa exige.

4. **Execução por objetivo** — dê **critérios de sucesso**, não passo a passo. Citando
   Karpathy: *"LLMs são excepcionais em iterar até atingir objetivos específicos. Não
   diga o que fazer; dê critérios de sucesso e observe."* (Veja também `/goal` no Claude Code.)

## Por que funciona

Karpathy aponta os vícios típicos: o modelo faz suposições erradas sem checar,
superdimensiona código/abstrações, e às vezes altera/remove código que não entende.
Os 4 princípios atacam exatamente esses pontos — e cabem em poucas linhas no
`CLAUDE.md`, que carrega em toda sessão.

> Combina com: manter o `CLAUDE.md` enxuto (ver `gestao-contexto-tokens.md`) e com
> o template em `building-blocks/claude-md/`.
