# 🔎 Pesquisa de base — junho/2026

Consolidado da varredura feita na internet (fontes oficiais + comunidade) para
embasar o preenchimento da biblioteca. **Não é a documentação final** — é a
matéria-prima factual, com links para conferência.

> Data da coleta: 2026-06-18. Versões e datas vêm dos changelogs/specs oficiais.
> Métricas de popularidade (estrelas) são aproximadas.

---

## 1. Claude Code — novidades e capacidades

**Modelos**
- Disponíveis: Fable 5, Opus 4.8/4.7/4.6/4.5, Sonnet 4.6/4.5, Haiku 4.5. Padrão: **Sonnet 4.6**.
- Opus 4.8 (28/05/2026): padrão "high effort", `/effort xhigh`, "fast mode" (2x velocidade, 2x custo).
- Fable 5 (09/06/2026): modelo "Mythos-class" para uso geral.
- Fontes: https://code.claude.com/docs/en/model-config • https://code.claude.com/docs/en/changelog

**Claude Code na web/cloud** (`claude.ai/code`)
- Sessões em sandbox isolado, persistem com browser fechado, monitoráveis pelo app móvel.
- Integra com GitHub (clona repo, cria branches), setup scripts, allowlist de rede, Docker.
- Flags `--remote` / `--teleport` movem sessão entre web e terminal. **Auto-fix de PRs**.
- Fonte: https://code.claude.com/docs/en/claude-code-on-the-web

**Sandboxing**
- Isolamento de filesystem + rede; reduziu ~84% dos prompts de permissão (uso interno Anthropic).
- `--safe-mode` / `CLAUDE_CODE_SAFE_MODE` desliga CLAUDE.md, plugins, skills, hooks e MCP.
- Bloqueio de comandos perigosos (ex.: `rm -rf $HOME`).
- Fontes: https://www.anthropic.com/engineering/claude-code-sandboxing • https://www.infoq.com/news/2025/11/anthropic-claude-code-sandbox/

**Plugins**
- Bundle versionado: skills + subagents + slash commands + hooks + output styles + MCP.
- Carregamento local (sem marketplace); scaffold com `claude plugin init <nome>`; `claude plugin validate`.

**Skills**
- `SKILL.md` com frontmatter em `.claude/skills/`; invocável por `/nome` ou autonomamente.
- Skills aninhadas; colisão de nome vira `<dir>:<nome>`; o `.claude/` mais próximo vence.
- `SessionStart` pode retornar `reloadSkills: true`; `/context` mostra tokens por skill.

**Subagents**
- Aninhados (subagent gera subagent, até 5 níveis em background).
- `claude agents` (Agent View): lista todas as sessões com tempo/tokens/turns.
- Dynamic Workflows (`/workflows`); isolamento por worktree (`isolation: "worktree"`).

**Hooks**
- 12 eventos: PreToolUse, PostToolUse, UserPromptSubmit, SessionStart, Stop, SubagentStop, etc.
- `async: true` (background), **HTTP hooks** (validação remota), post-session hook.
- `args: string[]` (exec form), env `CLAUDE_PROJECT_DIR`, `${CLAUDE_PLUGIN_ROOT}`.
- Fonte: https://code.claude.com/docs/en/hooks

**Outras capacidades úteis**
- Checkpoints/Rewind: Esc-Esc ou `/rewind` reverte código + conversa.
- `/goal`, `/ultraplan` (trabalho longo com checkpoints), `/context`, `/compact`.
- `fallbackModel` (até 3 fallbacks), permissão `Tool(param:value)`, `/config key=value`.
- `/code-review` (com `--comment` posta inline no PR) e `/simplify`.
- Remote Control (`/remote-control`), Claude in Chrome (`/chrome`).
- Fonte principal: https://code.claude.com/docs/en/changelog

---

## 2. MCP (Model Context Protocol)

- **Spec estável: `2025-11-25`**. Próxima `2026-07-28` em Release Candidate.
- Transport moderno: **Streamable HTTP** (substituiu HTTP+SSE). RC traz core stateless, Extensions, Tasks, MCP Apps.
- **Governança:** doado à **Agentic AI Foundation** (Linux Foundation) em dez/2025; co-fundada com Block e OpenAI.
- **Servidores oficiais** (`modelcontextprotocol/servers`): everything, fetch, filesystem, git, memory, sequentialthinking, time.
- **Mais populares:** GitHub MCP (o mais instalado de 2026), Playwright MCP (Microsoft), Context7, Brave Search. 14.000+ servidores no ecossistema.
- **Registry oficial:** https://registry.modelcontextprotocol.io (nomes reverse-DNS). Diretórios: PulseMCP, MCP Market.
- **No Claude Code:** `claude mcp add` (stdio/http), escopos `user`/`project` (`.mcp.json`), OAuth via `--header`.
- Fontes: https://modelcontextprotocol.io/specification/2025-11-25 • https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ • https://code.claude.com/docs/en/mcp • https://github.com/modelcontextprotocol/servers

---

## 3. GitHub para desenvolvimento com IA

**GitHub MCP Server oficial**
- Toolsets: context, repos, issues, pull_requests, actions, code_security, secret_protection, dependabot, discussions, projects, etc. (flag `--toolsets`).
- Remoto hospedado pelo GitHub (`https://api.githubcopilot.com/mcp/`, OAuth/PAT) ou local via Docker (`ghcr.io/github/github-mcp-server`).
- GA em 04/09/2025 (OAuth 2.1 + PKCE).
- Fonte: https://github.com/github/github-mcp-server

**Claude Code GitHub Action** (`anthropics/claude-code-action`, MIT)
- Mencionar `@claude` em issue/PR; analisa, implementa, corrige bugs, abre PR, **autofix de CI**.
- Setup: `/install-github-app` ou app https://github.com/apps/claude + `ANTHROPIC_API_KEY`.
- Auth: API key, OAuth (`CLAUDE_CODE_OAUTH_TOKEN`), Bedrock (OIDC), Vertex.
- v1.0: detecção automática de modo; args passam por `claude_args`.
- Fontes: https://code.claude.com/docs/en/github-actions • https://github.com/anthropics/claude-code-action

**GitHub Actions — novidades p/ IA**
- **GitHub Agentic Workflows** (public preview 11/06/2026): agentes como workflows escritos em Markdown, read-only por padrão, escrita via "safe-outputs". Engines: Copilot CLI, Claude Code, Codex.
- Immutable Actions (OCI/GHCR), SHA-pinning policy, Artifact Attestations, OIDC keyless.

**Segurança (essencial ao dar acesso de IA a repos)**
- Use `GITHUB_TOKEN` (escopado, expira) em vez de PAT; read-only por padrão.
- **Prompt injection é risco real**: a action sanitiza conteúdo mas avisa que não é à prova de bypass; use allowlist de autores.
- OIDC > segredos longos; cuidado com `pull_request_target`; pin de actions por SHA.
- ⚠️ Incidente jun/2026: falha de supply-chain na própria claude-code-action (corrigida na v1.0.94 / Claude Code 2.1.128). Lição: pinar versões e revisar permissões.
- Fontes: https://github.com/anthropics/claude-code-action/blob/main/docs/security.md • https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/

---

## 4. Repositórios públicos de referência

**Listas "awesome" (porta de entrada)**
- hesreallyhim/awesome-claude-code (~46,8k ⭐) — skills, hooks, commands, plugins
- punkpeye/awesome-mcp-servers (~89,4k ⭐) — maior coleção de servidores MCP
- modelcontextprotocol/servers (~87,4k ⭐) — servidores MCP oficiais

**Coleções reutilizáveis**
- VoltAgent/awesome-claude-code-subagents (~22k ⭐) — 150+ subagents
- VoltAgent/awesome-agent-skills — 1000+ skills (Anthropic, Vercel, Stripe, Cloudflare...)
- rohitg00/awesome-claude-code-toolkit — agents, skills, commands, plugins, hooks

**Plugins / marketplaces**
- anthropics/claude-plugins-official (~30,4k ⭐) — marketplace **oficial** (já vem por padrão)

**Ferramentas da comunidade**
- ruvnet/claude-flow (~59k ⭐) — orquestração multi-agente
- musistudio/claude-code-router (~35k ⭐) — roteia para outros modelos
- davila7/claude-code-templates (~28k ⭐) — CLI de setup/monitoramento
- ryoppippi/ccusage (~16k ⭐) — análise de uso/custo

---

## 5. Capacidades do modelo (Opus 4.8 / contexto 1M)

> O Claude Code desta sessão roda no `claude-opus-4-8[1m]`. Resumo dos achados.

**Especificações**
- Model ID (API): `claude-opus-4-8`.
- **Contexto: 1M tokens** na Claude API, Bedrock e Vertex (no Microsoft Foundry fica em 200K). Para o Opus 4.8 o 1M é nativo — **sem beta header dedicado**.
- **Output máximo:** 128K tokens (até 300K via Batch API com header `output-300k-2026-03-24`).
- **Knowledge cutoff:** janeiro/2026. Entrada texto + imagem; saída texto.

**Raciocínio e effort**
- **Adaptive thinking** (`thinking: {type:"adaptive"}`): o modelo decide quando/quanto pensar. Extended thinking clássico (`budget_tokens`) **não** é suportado (erro 400). Sampling params (`temperature` etc.) removidos.
- **Effort levels:** `low` / `medium` / `high` / `xhigh` / `max`. **Default = `high`**. Recomendação oficial: **`xhigh` para coding/agêntico** de longo horizonte.

**Benchmarks** (anúncio oficial, ~28/05/2026 — via busca, confirmar na fonte)
- SWE-bench Verified 88,6% • SWE-bench Pro **69,2%** (+4,9 vs 4.7) • MCP-Atlas 82,2% • BrowseComp 84,3%.

**Preço**
- **$5/MTok input • $25/MTok output** (padrão). Cache read $0,50/MTok. Batch 50% off.
- ⭐ **Contexto de 1M NÃO tem preço premium** — janela inteira ao preço padrão (difere do antigo long-context do Sonnet 4).
- Fast mode (Opus 4.8): ~2,5× mais rápido, $10/$50 por MTok.

**Quando o 1M brilha**
- Agentes de longo horizonte, refactors multi-arquivo em bases grandes, RAG pesado (muitos PDFs/docs), workflows multi-etapa.
- ⚠️ Ressalva oficial: "mais contexto não é automaticamente melhor" (*context rot*). Curar o que entra + usar `compaction`/context editing.

- Fontes: https://platform.claude.com/docs/en/about-claude/models/overview • https://platform.claude.com/docs/en/build-with-claude/context-windows • https://platform.claude.com/docs/en/build-with-claude/effort • https://platform.claude.com/docs/en/about-claude/pricing
