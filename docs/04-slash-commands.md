# 04 — Slash commands

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Ref: `code.claude.com/docs/en/slash-commands`.

## O que é

**Slash commands** são atalhos digitados com `/` no modo interativo. Há os **embutidos**
(ex.: `/memory`, `/clear`, `/config`, `/agents`, `/plugin`, `/loop`, `/goal`) e os
**customizados**, que você cria como arquivos **Markdown** em `.claude/commands/`.

> ⚠️ Hoje os comandos customizados em `.claude/commands/` **continuam funcionando**, mas as
> **skills** (`docs/07`) são o caminho recomendado: um `.claude/skills/deploy/SKILL.md` e um
> `.claude/commands/deploy.md` criam ambos `/deploy` e se comportam igual.

## Quando usar

| Quer… | Use |
|---|---|
| Atalho simples de prompt repetível (1 arquivo) | command em `.claude/commands/` |
| Capacidade com arquivos auxiliares/script, descoberta automática | **skill** (`docs/07`) |
| Operação do sistema (limpar, configurar, ver agentes) | command **embutido** |

## Como configurar / usar

### Comando customizado (Markdown)
`.claude/commands/revisar.md` → vira `/revisar`:
```markdown
---
description: Revisa o diff atual em busca de bugs e sugere melhorias.
argument-hint: "[arquivo opcional]"
---

Revise as mudanças em `$ARGUMENTS` (ou o diff atual se vazio).
Aponte bugs, riscos e simplificações. Seja específico e cite arquivo:linha.
```

### Argumentos
- **`$ARGUMENTS`** — tudo que veio depois do comando.
- **`$1`, `$2`, …** — argumentos posicionais.
- (Opcional) **`!`comando`​`** no corpo injeta a saída de um shell antes do Claude ler.

### Escopo e namespacing
- **Projeto:** `.claude/commands/` (versionado).
- **Usuário:** `~/.claude/commands/` (todos os projetos).
- **Subpastas** viram namespace (ex.: `.claude/commands/git/sync.md` → `/git:sync`).
- **De plugin:** aparecem como `/<plugin>:<comando>`.

### Frontmatter útil
`description`, `argument-hint`, `disable-model-invocation` (impede o modelo de chamar
sozinho), e seleção de modelo/ferramentas conforme a doc.

## Exemplo

`~/.claude/commands/commit.md` → `/commit`:
```markdown
---
description: Cria um commit com mensagem no padrão do repositório.
---

Analise o diff staged e crie UM commit com mensagem clara e imperativa em PT-BR.
Não inclua nada além do necessário. Não faça push.
```

> Há uma peça pronta de `/commit` em `building-blocks/` — ver o catálogo do repositório.

## Pegadinhas ⚠️

- **Command vs skill:** pra algo além de um prompt simples (scripts, vários arquivos,
  descoberta automática), prefira **skill**.
- **Nome = caminho do arquivo.** `deploy.md` → `/deploy`; subpasta vira `prefixo:`.
- **`disable-model-invocation`** se você quer que só rode quando **você** chamar.
- **Não confunda com `@`** (referência de arquivo) nem com `!` (shell mode).

## Referências oficiais

- Slash commands: https://code.claude.com/docs/en/slash-commands
- (relacionado) Skills: `docs/07` · Plugins: `docs/09`
</content>
