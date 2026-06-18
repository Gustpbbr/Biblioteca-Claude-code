# Commands — slash commands reutilizáveis

Slash commands prontos para copiar em `.claude/commands/` de qualquer projeto.

## Disponíveis

- [`commit.md`](./commit.md) — monta um commit git a partir do diff atual (`/commit`).

> Cada command é um `.md` com frontmatter (`allowed-tools`, `description`) e pode
> injetar contexto com a sintaxe `` !`comando` `` e usar `$ARGUMENTS`/`$1`.
