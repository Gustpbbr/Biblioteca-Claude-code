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

## 💾 Economia de contexto/tokens e RAG de codebase

> Encontrados em conteúdo de redes sociais (curadoria do usuário). ⭐ aproximadas;
> **revise o código antes de usar**. Todos prometem reduzir tokens dando ao Claude
> contexto mais preciso em vez de reler tudo.

- **rtk** — proxy de CLI (binário Rust) que filtra/comprime saídas de comandos
  antes de irem ao contexto; promete **60–90% menos tokens**, 100+ comandos, <10ms.
- **code-review-graph** — mapa estrutural do código com Tree-sitter, incremental,
  entrega contexto preciso via MCP (foco em code review). PyPI.
- **Graphify** (`/graphify`) — skill que constrói um grafo de conhecimento
  (JSON+HTML) do codebase/docs como **RAG local**; visualização no Obsidian.
  Funciona em Claude Code e vários outros agentes. ~16k⭐.
- **brain-ingest** — transcreve YouTube/podcast/áudio e salva nota limpa no
  Obsidian, acessível ao Claude (alimenta o "segundo cérebro").

> Tema relacionado: ver os cheatsheets `gestao-contexto-tokens.md` e
> `claude-md-boas-praticas.md`.

## 🆕 Novos da curadoria de Instagram (2026-06-18) — ⚠️ a verificar

> Coletados de prints; **existência/licença ainda não conferida via clone**. Revise antes de usar.

**Orquestração / multi-agente**
- **claude-flow v3** — `npx claude-flow@v3alpha init`. 60+ agentes, swarms c/ consenso, "Queen-led",
  178+ MCP tools, 42+ skills, "RuVector". Framework pesado de orquestração.
- **affaan-m/ECC ("Everything Claude Code")** — harness de otimização: skills, instincts, memory,
  security, research-first; PreToolUse hooks, prompt-defense; multi-tool (Claude Code/Codex/Cursor).

**Skills**
- **hardikpandya/stop-slop** — remove "AI tells" da prosa (escrita mais humana).
- **mukul975/Anthropic-Cybersecurity-Skills** — 754 skills mapeadas p/ MITRE ATT&CK.
- **AgricDaniel/banana-claude** — geração de imagem (Claude como "Diretor de Arte" via Gemini Nano Banana).
- **remotion-dev/skills** — motion design/vídeo via Remotion (`npx skills add remotion-dev/skills`).
- **anthropics/knowledge-work-plugins** (oficial) — plugins por área (eng., design, legal, finanças, RH…).

**MCP / connectors**
- **agent-browser** (`vercel-labs/agent-browser`) — browser autônomo p/ o Claude ("olhos").
- **Blender MCP** — modelar/renderizar no Blender por linguagem natural.
- **Higgsfield MCP** (`https://mcp.higgsfield.ai/mcp`) — gerar imagem/vídeo cinematográfico.
- **Trimble SketchUp** e **Autodesk Fusion** — connectors oficiais (Anthropic & Partners) p/ 3D/CAD.
- **GitNexus** (`abhigyanpatwari/GitNexus`) — grafo de conhecimento do codebase.

**Referência / outros**
- **elder-plinius/CL4R1T4S** — coleção de system prompts reconstruídos (uso da flag `--system-prompt-file`).
- **neilsonnn/image-blaster** — fotos → mundos 3D jogáveis via Claude Code.
- **Lum1104/Understand-Anything** — plugin multi-plataforma (claude/cursor/copilot).
- Plugin **`/codex:review`** — roda review do OpenAI Codex de dentro do Claude Code.

---

## ⚖️ Nota sobre uso

Estes são repositórios de **terceiros**. Antes de instalar plugins/skills/MCP de
terceiros: leia o código, confira permissões e hooks, e prefira versões fixadas
(pin) — lembre do incidente de supply-chain de jun/2026 documentado na pesquisa.
