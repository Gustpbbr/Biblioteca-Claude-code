# 05 — Subagents

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Ref: `code.claude.com/docs/en/sub-agents`.

## O que é

**Subagents** são "assistentes especializados" que o Claude pode acionar para tarefas
específicas. Cada subagent roda no **próprio contexto isolado** (não polui o contexto
principal), com sua própria instrução, e opcionalmente seu próprio **modelo** e conjunto de
**ferramentas**. São definidos como arquivos **Markdown com frontmatter** em
`.claude/agents/` (projeto) ou `~/.claude/agents/` (usuário).

## Quando usar

| Situação | Por quê |
|---|---|
| Tarefa de busca ampla ("varra o repo e ache X") | Mantém os despejos fora do contexto principal; devolve só a conclusão |
| Trabalho repetível com papel próprio (revisor, pesquisador) | Instrução especializada + ferramentas restritas |
| Rodar coisas em paralelo | Vários subagents independentes ao mesmo tempo |
| Quer um modelo mais barato pra subtarefa | `model:` próprio no frontmatter |

Evite pra tarefas triviais: o overhead de delegar não compensa.

## Como configurar / usar

### Definição (`.claude/agents/revisor.md`)
```markdown
---
name: revisor
description: Revisa diffs em busca de bugs e devolve um resumo. Use após mudanças
  de código quando o usuário pedir revisão.
tools: Read, Grep, Glob          # (opcional) restringe ferramentas
model: claude-haiku-4-5          # (opcional) modelo próprio
---

Você é um revisor de código rigoroso e conciso.
Analise o diff, aponte bugs/riscos/simplificações com arquivo:linha.
Devolva um resumo curto — não reescreva o código.
```

### Como é acionado
- **Model-invoked:** o Claude **delega automaticamente** quando a tarefa casa com a
  `description` (por isso escreva a `description` deixando claro *quando* usar).
- **Explícito:** via `/agents` (gerenciar/disparar) ou pedindo "use o subagent revisor".
- **Isolamento:** o subagent tem o próprio contexto; só o **resultado final** volta pro
  agente principal (ótimo pra não encher o contexto com arquivos lidos).

### Escopo
- **Projeto:** `.claude/agents/` (versionado, do time).
- **Usuário:** `~/.claude/agents/` (seus, em todos os projetos).
- Cada subagent é **um arquivo** `.md` (diferente de skill, que é uma **pasta**).

## Exemplo (delegar uma busca ampla)

> "Use um subagent pra mapear onde a função `parseInvoice` é usada e me devolva só a lista
> de arquivos:linha e um resumo — não cole o conteúdo dos arquivos."

O subagent lê dezenas de arquivos no contexto **dele** e devolve só a conclusão.

## Pegadinhas ⚠️

- **A `description` controla a delegação automática.** Vaga = o Claude não delega quando
  deveria.
- **Restrinja `tools`** quando fizer sentido (ex.: revisor só precisa de `Read/Grep/Glob`)
  — reduz risco e custo.
- **Contexto isolado = sem memória compartilhada.** O subagent não "lembra" da conversa
  principal além do que você passar na tarefa.
- **Subagent (arquivo) ≠ skill (pasta) ≠ plugin (distribuição).** Não confunda os três.
- **Custo:** muitos subagents em paralelo multiplicam o consumo de tokens (ver a pegadinha
  de paralelismo em `reference/loops-e-goals.md`).

## Referências oficiais

- Subagents: https://code.claude.com/docs/en/sub-agents
- (relacionado) Skills: `docs/07` · Loops/Goals: `reference/loops-e-goals.md`
- Peça pronta: subagent revisor em `building-blocks/` (ver catálogo do repositório).
</content>
