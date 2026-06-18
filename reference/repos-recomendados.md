# 🌟 Repositórios recomendados da comunidade

Catálogo curado de repositórios públicos úteis para Claude Code, MCP e skills.
Cada item traz **o que é**, **licença**, **como instalar/usar** e uma nota honesta.

> Verificado em 2026-06-18 (existência confirmada via clone; licenças conferidas).
> Estrelas são aproximadas. Sempre revise o código antes de usar em projeto sério.

---

## 🏗️ Frameworks e metodologias de desenvolvimento

### obra/superpowers — ~95k ⭐ · MIT
Metodologia completa de desenvolvimento para agentes de código, sobre um conjunto
de **skills componíveis**: o agente extrai a spec da conversa, mostra em pedaços
digeríveis, monta um plano, e roda **desenvolvimento dirigido por subagents**
(TDD red/green, YAGNI, DRY) — chega a trabalhar autônomo por horas.
- Suporta Claude Code, Codex, Cursor, Gemini CLI, Copilot CLI e outros.
- É um **plugin** (`.claude-plugin/`) — ótima referência de arquitetura de plugin.
- Repo: https://github.com/obra/superpowers

### open-gsd/gsd-core — "Get Shit Done" · spec-driven
Sistema de meta-prompting, context engineering e desenvolvimento spec-driven para
Claude Code (criado por TÂCHES).
- ⚠️ **Atenção:** o repo antigo `gsd-build/get-shit-done` (~34k ⭐) foi **arquivado**
  e migrou para `open-gsd/gsd-core`. Use o novo.
- Repo: https://github.com/open-gsd/gsd-core

---

## 🧠 Memória persistente

### thedotmack/claude-mem — ~38k ⭐ · Apache-2.0
Plugin que **captura automaticamente** o que o Claude faz nas sessões, comprime
com IA (usando o Agent SDK) e **reinjeta o contexto relevante** em sessões
futuras. Resolve a dor de "o Claude esquece tudo quando a sessão acaba".
- É um **plugin** com hooks de SessionStart/Stop — boa referência de uso de hooks.
- Repo: https://github.com/thedotmack/claude-mem

---

## 🎨 Skills (Agent Skills)

### kepano/obsidian-skills — ~14k ⭐ · MIT
Skills para o **Obsidian** (do criador do Obsidian), ensinando o agente a usar
Markdown, Bases, JSON Canvas e a CLI. Seguem a [spec agentskills.io](https://agentskills.io/specification),
então funcionam em qualquer agente compatível.
```
/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills
```
- Repo: https://github.com/kepano/obsidian-skills

### nextlevelbuilder/ui-ux-pro-max-skill — ~44k ⭐ · MIT
Skill de **design/UI-UX** com 161 regras de raciocínio e 67 estilos de UI, para
construir front-ends profissionais em várias plataformas.
- Inclui CLI (`uipro-cli` no npm) e plugin (`.claude-plugin/`).
- Repo: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

---

## 🔌 Servidores MCP

### czlonkowski/n8n-mcp — ~15k ⭐ · MIT
Servidor MCP que dá ao Claude acesso profundo ao **n8n** (automação de workflows):
1.845 nodes, propriedades, operações, 2.352 templates. Permite o Claude **montar
workflows do n8n** pra você.
- Excelente **caso de estudo de um MCP server de produção** (5.418 testes passando,
  Docker, deploy em minutos).
- Repo: https://github.com/czlonkowski/n8n-mcp

---

## 📚 Listas "awesome" (porta de entrada)

### hesreallyhim/awesome-claude-code — ~29k ⭐
Lista curada de skills, hooks, slash-commands, orquestradores, aplicações e
plugins para Claude Code. A referência geral da categoria.
- Repo: https://github.com/hesreallyhim/awesome-claude-code

> Veja também o catálogo mais amplo (MCP, subagents, marketplaces, ferramentas)
> na seção 4 de [`pesquisa-2026-06.md`](./pesquisa-2026-06.md).

---

## ⚖️ Nota sobre uso

Estes são repositórios de **terceiros**. Antes de instalar plugins/skills/MCP de
terceiros: leia o código, confira permissões e hooks, e prefira versões fixadas
(pin) — lembre do incidente de supply-chain de jun/2026 documentado na pesquisa.
