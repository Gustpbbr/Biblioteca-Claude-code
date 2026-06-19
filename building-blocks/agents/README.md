# Agents — subagents prontos

Subagents prontos para copiar em `.claude/agents/` de qualquer projeto.

## Disponíveis

- [`revisor-de-codigo.md`](./revisor-de-codigo.md) — revisa código com filtro por
  confiança (reporta só o que importa).
- [`planejador.md`](./planejador.md) — planeja features/refatorações grandes antes
  de codar: fases, passos com caminhos de arquivo, dependências, risco e critérios
  de sucesso (plan-first).
- [`cacador-de-falhas-silenciosas.md`](./cacador-de-falhas-silenciosas.md) — caça
  erros engolidos, catch vazio e fallbacks que mascaram falhas (foco em error
  handling).

> Cada agent é um `.md` com frontmatter (`name`, `description`, `tools`, `model`,
> `color`) seguido do prompt de sistema do agente.
