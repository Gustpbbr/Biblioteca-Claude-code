# 🗂️ Anatomia de um projeto Claude Code

> Mapa de consulta rápida de **todos os arquivos e pastas que o Claude Code lê**.
> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Para detalhes de cada peça, veja os docs numerados em `docs/`.

## Visão geral (árvore)

```
seu-projeto/
├── CLAUDE.md                 # memória do projeto (raiz OU .claude/CLAUDE.md). Auto-carregado. <200 linhas.
├── CLAUDE.local.md           # preferências pessoais do projeto (NÃO deprecado). → .gitignore
├── .mcp.json                 # servidores MCP do time (⚠️ na RAIZ, não em .claude/). Versionado.
├── .gitignore
└── .claude/
    ├── settings.json         # settings do time (versionado)
    ├── settings.local.json   # overrides pessoais (→ .gitignore)
    ├── commands/             # slash commands (.md) — funciona, mas skills são o caminho novo
    │   └── deploy.md         #   → /deploy
    ├── agents/               # subagents (1 arquivo .md c/ frontmatter cada)
    │   └── revisor.md
    ├── skills/               # Agent Skills (PASTA com SKILL.md) — carregam sob demanda
    │   └── carousel/
    │       └── SKILL.md
    ├── rules/                # regras com path-scoping (frontmatter `paths:`)
    │   └── api.md            #   carrega só ao mexer em arquivos que casam o glob
    ├── output-styles/        # estilos de resposta (role/tom/formato) — vigente em 2026
    │   └── terse.md
    ├── hooks/                # SCRIPTS dos hooks (.sh) — a CONFIG fica no settings.json
    │   └── block-rm.sh
    └── statusline.sh         # script da status line (apontado por "statusLine" no settings)
```

> Níveis também válidos: **usuário** (`~/.claude/…`) e **gerenciado/MDM**
> (`/etc/claude-code/…`, `/Library/Application Support/ClaudeCode/…`, `C:\Program Files\ClaudeCode\…`).

## Tabela de referência

| Item | Onde | O que faz | Versionar? | Doc |
|---|---|---|---|---|
| `CLAUDE.md` | raiz **ou** `.claude/` (+ `~/.claude/`, subpastas) | Memória/contexto auto-carregado no início. Suporta imports `@caminho`. | ✅ | `docs/02` |
| `CLAUDE.local.md` | raiz | Preferências pessoais do projeto (sandbox, dados de teste). **Não** deprecado. | ❌ gitignore | `docs/02` |
| `.mcp.json` | **raiz** | Servidores MCP do time (escopo *project*). 1ª vez pede aprovação. | ✅ | `docs/08` |
| `.claude/settings.json` | `.claude/` | Settings do time: permissões, hooks, MCP, etc. | ✅ | `docs/03` |
| `.claude/settings.local.json` | `.claude/` | Overrides pessoais deste repo. | ❌ gitignore | `docs/03` |
| `~/.claude/settings.json` | usuário | Settings pessoais de todos os projetos. | n/a | `docs/03` |
| `commands/` | `.claude/` | Slash commands em `.md` (`deploy.md` → `/deploy`). **Skills são o jeito recomendado agora.** | ✅ | `docs/04` |
| `agents/` | `.claude/` ou `~/.claude/` | Subagents (1 `.md` com frontmatter). Contexto isolado. | ✅ | `docs/05` |
| `skills/<nome>/SKILL.md` | `.claude/`, `~/.claude/` ou plugin | Skills: **pastas** com `SKILL.md` + recursos. Carregam **sob demanda** (model-invoked ou `/nome`). | ✅ | `docs/07` |
| `rules/` | `.claude/` | Regras **path-scoped**: frontmatter `paths:` → carrega só ao tocar arquivos que casam o glob. Sem `paths` = sempre. | ✅ | `docs/02`/`03` |
| `output-styles/` | `.claude/`, `~/.claude/` ou plugin | Muda role/tom/formato da resposta. Built-ins: Default, Proactive, Explanatory, Learning. | ✅ | `docs/10` |
| Hooks | **config no `settings.json`**; scripts em `.claude/hooks/` | Eventos: `SessionStart`, `PreToolUse`, `PostToolUse`, `Stop`, `PreCompact`, `InstructionsLoaded`. | ✅ | `docs/06` |
| `statusLine` | chave no `settings.json` → script | Barra inferior custom (recebe JSON no stdin, imprime a linha). | ✅ | `docs/10` |
| Plugins | `.claude-plugin/plugin.json` + skills/agents/hooks na raiz do plugin | 1ª classe em 2026. `/plugin`, `/plugin marketplace add <org>/<repo>`. Namespacing `/plugin:comando`. | ✅ | `docs/09` |

## Precedência de settings (maior → menor)

1. **Managed/MDM** (`managed-settings.json`) — imposto, não dá pra sobrescrever
2. **Argumentos de CLI** (`--model`, etc.)
3. **`.claude/settings.local.json`** (pessoal do repo)
4. **`.claude/settings.json`** (time)
5. **`~/.claude/settings.json`** (usuário)

## O que commitar vs ignorar

- ✅ **Commitar:** `CLAUDE.md`, `.mcp.json`, `.claude/settings.json`, `.claude/rules/`,
  `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/hooks/`, `.claude/output-styles/`.
- ❌ **`.gitignore`:** `.claude/settings.local.json`, `CLAUDE.local.md`.

## ⚠️ Mitos comuns (corrigidos)

| Alegação | Realidade |
|---|---|
| `.mcp.json` vai em `.claude/` | ❌ Vai na **raiz** do projeto. |
| Hooks ficam só na pasta `.claude/hooks/` | ❌ A **config** fica no `settings.json`; em `.claude/hooks/` ficam os **scripts**. |
| `CLAUDE.local.md` foi deprecado | ❌ Continua suportado/recomendado p/ preferências pessoais. |
| CLAUDE.md aninhado faz "path-scoping" | ❌ CLAUDE.md aninhado carrega sob demanda; **path-scoping de verdade é `.claude/rules/` com `paths:`**. |
| `output-styles` foi removido | ❌ Vigente em 2026. |
| Em `.claude-plugin/` ficam skills/agents/hooks | ❌ Lá só vai o `plugin.json`; skills/agents/hooks ficam na **raiz do plugin**. |
| `CLAUDE.md` precisa estar na raiz | ⚠️ Pode estar na raiz **ou** em `.claude/CLAUDE.md` (+ níveis usuário/managed). |

## Lema (resumo mental)

> **CLAUDE.md é orientação (advisory). Hooks são determinísticos. Skills carregam sob demanda.**
> *(origem: print @leadgenman; conceito confirmado na doc oficial.)*

## Referências oficiais

- Memória / CLAUDE.md: https://code.claude.com/docs/en/memory
- Settings: https://code.claude.com/docs/en/settings
- Hooks: https://code.claude.com/docs/en/hooks
- Skills: https://code.claude.com/docs/en/skills
- Plugins: https://code.claude.com/docs/en/plugins
- MCP: https://code.claude.com/docs/en/mcp
</content>
</invoke>
