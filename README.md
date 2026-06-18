# 📚 Biblioteca Claude Code

Biblioteca de referência sobre **tudo que o Claude Code faz** — pensada para ser
reutilizada em todos os seus outros projetos. Aqui você encontra desde a
explicação a fundo de cada funcionalidade até peças prontas pra copiar e colar.

> **Status:** ✅ `docs/` (01–14) **100% preenchido** e verificado contra a doc oficial.
> `reference/`, `building-blocks/` e `recipes/` em evolução contínua (curadoria ativa).

---

## 🧭 Como navegar

A biblioteca é organizada em **4 pilares**, cada um respondendo a uma pergunta diferente:

| Pilar | Pergunta que responde | Pasta |
|-------|----------------------|-------|
| 📖 **Referência** | "Quero **entender** essa funcionalidade a fundo" | [`docs/`](./docs/) |
| 🧱 **Peças prontas** | "Quero **pegar algo pronto** e usar em outro projeto" | [`building-blocks/`](./building-blocks/) |
| 🍳 **Receitas** | "Quero **resolver uma tarefa concreta** passo a passo" | [`recipes/`](./recipes/) |
| ⚡ **Consulta rápida** | "Só quero **dar uma olhada rápida** numa tabela" | [`reference/`](./reference/) |

---

## 📖 Documentação de referência (`docs/`)

Explicação completa de cada funcionalidade, sempre no mesmo formato:
**O que é → Quando usar → Como configurar → Exemplo → Pegadinhas → Referências oficiais**.

| # | Tópico | Arquivo |
|---|--------|---------|
| 01 | CLI e modos de execução | [`docs/01-cli-e-modos.md`](./docs/01-cli-e-modos.md) |
| 02 | CLAUDE.md (memória) | [`docs/02-claude-md-memoria.md`](./docs/02-claude-md-memoria.md) |
| 03 | Settings e permissões | [`docs/03-settings-e-permissoes.md`](./docs/03-settings-e-permissoes.md) |
| 04 | Slash commands | [`docs/04-slash-commands.md`](./docs/04-slash-commands.md) |
| 05 | Subagents | [`docs/05-subagents.md`](./docs/05-subagents.md) |
| 06 | Hooks | [`docs/06-hooks.md`](./docs/06-hooks.md) |
| 07 | Skills | [`docs/07-skills.md`](./docs/07-skills.md) |
| 08 | MCP (Model Context Protocol) | [`docs/08-mcp.md`](./docs/08-mcp.md) |
| 09 | Plugins | [`docs/09-plugins.md`](./docs/09-plugins.md) |
| 10 | Output styles e status line | [`docs/10-output-styles-statusline.md`](./docs/10-output-styles-statusline.md) |
| 11 | IDE e Claude Code na web/cloud | [`docs/11-ide-e-web-cloud.md`](./docs/11-ide-e-web-cloud.md) |
| 12 | GitHub Actions | [`docs/12-github-actions.md`](./docs/12-github-actions.md) |
| 13 | SDK de agentes e API Claude | [`docs/13-sdk-e-api.md`](./docs/13-sdk-e-api.md) |
| 14 | Habilidades de mídia (imagem, vídeo, áudio, design) | [`docs/14-habilidades-de-midia.md`](./docs/14-habilidades-de-midia.md) |

---

## 🧱 Peças prontas (`building-blocks/`)

Componentes reutilizáveis — copie para o `.claude/` de qualquer projeto.

- [`building-blocks/commands/`](./building-blocks/commands/) — slash commands reutilizáveis
- [`building-blocks/agents/`](./building-blocks/agents/) — subagents prontos
- [`building-blocks/hooks/`](./building-blocks/hooks/) — hooks (lint, test, format, guard-rails)
- [`building-blocks/skills/`](./building-blocks/skills/) — skills reutilizáveis
- [`building-blocks/settings/`](./building-blocks/settings/) — templates de `settings.json`
- [`building-blocks/claude-md/`](./building-blocks/claude-md/) — templates de `CLAUDE.md` por tipo de projeto

---

## 🍳 Receitas (`recipes/`)

Guias práticos de ponta a ponta para tarefas comuns. Veja [`recipes/`](./recipes/).

## ⚡ Consulta rápida (`reference/`)

Cheatsheets e tabelas para olhar em segundos:
- [`anatomia-projeto-claude.md`](./reference/anatomia-projeto-claude.md) — todos os arquivos que o Claude Code lê
- [`loops-e-goals.md`](./reference/loops-e-goals.md) — `/loop` e `/goal` (tarefas autônomas)
- [`gestao-contexto-tokens.md`](./reference/gestao-contexto-tokens.md) — não estourar o contexto
- [`claude-md-boas-praticas.md`](./reference/claude-md-boas-praticas.md) — bom `CLAUDE.md`
- [`repos-recomendados.md`](./reference/repos-recomendados.md) — catálogo de repos da comunidade
- [`curadoria-conteudo.md`](./reference/curadoria-conteudo.md) · [`pesquisa-2026-06.md`](./reference/pesquisa-2026-06.md)

---

## 🚀 Como usar em outros projetos

Três formas, da mais simples à mais integrada:

### 1. Copiar peças prontas (mais comum)
Copie o que precisar de `building-blocks/` para o `.claude/` do projeto-alvo:
```bash
# exemplo: levar o /commit, o subagent revisor e o hook de segurança
mkdir -p /caminho/projeto/.claude/{commands,agents,hooks}
cp building-blocks/commands/commit.md        /caminho/projeto/.claude/commands/
cp building-blocks/agents/revisor-de-codigo.md /caminho/projeto/.claude/agents/
cp building-blocks/settings/settings-base.json /caminho/projeto/.claude/settings.json
```
Depois adapte o `CLAUDE.md` a partir de `building-blocks/claude-md/template-generico.md`.

### 2. Usar como fonte de consulta
Mantenha esta biblioteca clonada e consulte os `docs/` e `reference/` quando precisar —
sem copiar nada. Bom para aprender/relembrar como cada recurso funciona.

### 3. Referenciar como submódulo (avançado)
Para times que querem versionar a fonte junto do projeto:
```bash
git submodule add <url-deste-repo> .biblioteca-claude
# e então copiar/symlinkar peças de .biblioteca-claude/building-blocks/ conforme a necessidade
```

### Checklist rápido para um projeto novo
1. `CLAUDE.md` enxuto (< 200 linhas) — stack, comandos, regras (`docs/02`).
2. `.claude/settings.json` com permissões (`allow`/`deny` p/ proteger `.env`) (`docs/03`).
3. Um hook de segurança em `PreToolUse` (`docs/06` + `building-blocks/hooks/`).
4. Os slash commands/subagents/skills que fizerem sentido (`docs/04`/`05`/`07`).
5. `.gitignore`: `settings.local.json`, `CLAUDE.local.md`.

> Antes de copiar peças de **terceiros** (repos do catálogo), revise o código — ver a
> nota de supply-chain em `reference/repos-recomendados.md`.

---

## 🗺️ Roadmap de preenchimento

- [x] Preencher `docs/` (01–14, referência completa — verificada na doc oficial)
- [x] Primeiros cheatsheets de `reference/` (anatomia, loops/goals, contexto, claude.md)
- [x] Primeiras peças em `building-blocks/` (`/commit`, subagent revisor, hook, templates)
- [x] Primeira `recipe/` (construir app com Claude Code)
- [ ] Enriquecer a recipe de pipeline com os prompts curados
- [ ] Verificar (via clone) os repos "a verificar" em `repos-recomendados.md`
- [x] Detalhar o guia "Como usar em outros projetos"
