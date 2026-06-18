# 🗂️ Curadoria de conteúdo (triagem)

Log de triagem do conteúdo enviado pelo usuário (prints de redes sociais, posts,
vídeos). Sinaliza o que é **relevante** para a biblioteca (✅), o que é **ruído**
(❌) e captura os nuggets úteis para virar docs/recipes/building-blocks depois.

> Regra: nem tudo que viraliza é verdade. Cada item relevante é verificado antes
> de virar conteúdo da biblioteca.

---

## Lote 2026-06-18 (b) — 9 imagens

### ✅ Relevante

**1. Tool: fotos → mundos 3D jogáveis, feito com Claude Code**
- Fonte: post @appinventiv4ai (AI4AI). Repo confirmado: `github.com/neilsonnn/image-blaster` (✅ existe).
- O quê: ferramenta open source que converte fotos normais em mundos 3D jogáveis.
  Destaque por ter sido **construída usando Claude Code**.
- Uso na biblioteca: exemplo de "o que dá pra construir com Claude Code" (showcase),
  não é um building-block. Candidato a uma seção "Projetos feitos com Claude Code".

**2. Técnica: memórias + skills compartilhadas entre duas pessoas**
- Fonte: story (Instagram). Sem repo — é um **workflow**.
- O quê: dois usuários compartilham memórias (CLAUDE.md) e skills entre si via uma
  **pasta sincronizada** (OneDrive). Há uma pasta específica para memórias/skills
  compartilhadas; ao fim de cada sessão, ambos rodam uma **skill de atualização
  automática** dessa pasta. Resultado relatado: muito mais produtividade em equipe.
- Uso na biblioteca: ótima ideia de **recipe** — "Compartilhar memórias e skills do
  Claude Code em equipe (via pasta sincronizada + skill de sync no SessionEnd)".
  ⚠️ Verificar viabilidade: usar `post-session hook` / SessionEnd para disparar o
  sync; cuidado com conflitos de merge e dados sensíveis na pasta compartilhada.

### ❌ Ruído (não entra na biblioteca)

- **Quadribol/Harry Potter com IA** (@diegoalmeida.ia) — geração de vídeo com
  Seedance 2.0 (controle de câmera por linha desenhada). IA de vídeo, não Claude Code.
- **Forbes / Pousada Verbicaro** (astroturismo, Santa Maria Madalena) — turismo.
- **AutoClaw / "ML engineer vs AI developer"** (Ollama, Qdrant, LangChain, FastAPI)
  — conteúdo genérico de stack de IA; sem relação direta com Claude Code.
- **AIReel** (ad) — gerar vídeo de drone desenhando o trajeto. IA de vídeo.
- **IDALL AI** (@darrenmaen, ad) — comunidade de "cinematic system" com Seedance.
  Marketing de prompts de vídeo.

---

## Lote 2026-06-18 (c) — 10 imagens

### ✅ Relevante

**1. "5 prompts do Claude para criar apps" (@gurudoprompt)** — carrossel de 7 slides.
- Pipeline de 5 prompts: Arquiteto → Dev Full Stack → Designer → Monetizador → Lançador.
- Embalagem clickbait ("R$10k/mês em 10 min"), mas a **estrutura dos prompts é boa**.
- ✅ Já transcrito e virou recipe: `recipes/construir-app-com-claude-code.md`.

### ❌ Ruído (não entra como técnica de Claude Code)

- **Anúncios do Cursor** (@ui.ananya_ + trycursor, patrocinado) — mostram projeto de
  hand-tracking (OpenCV+MediaPipe) e o seletor de modelos do Cursor (Composer, GPT-5.x,
  Sonnet 4.6, Opus 4.6). É concorrente do Claude Code. Nota: o Cursor roda modelos
  Claude, mas é outro cliente — fora do escopo da biblioteca (que é sobre Claude Code).

---

## Lote 2026-06-18 (d) — pasta "Prints Claude code" do Drive (100 imagens)

Varredura completa via OCR (`read_file_content`). A pasta é um dump misto: a
maioria é **conteúdo pessoal do usuário** (não entra no repo) ou ruído. Abaixo,
só o que é relevante para a biblioteca.

### ⚠️ Privacidade e segurança (ação recomendada)
- **Revogar/rotacionar** chaves que apareceram em prints: **Qdrant API key**
  (cluster "Gus_") e conferir a `ANTHROPIC_API_KEY` exibida no Railway.
- Há **dados médicos de paciente** (Dimagem) e financeiros (Pix) em prints —
  conteúdo sensível; **nada disso foi copiado para o repositório**.

### ✅ Tools/skills da comunidade encontrados (de redes sociais — ⭐ aproximadas, confirmar)
- **CLAUDE.md "anti-maus-hábitos"** (forrestchang, ~78,5k⭐) — 4 princípios baseados
  nas críticas do Karpathy. → virou cheatsheet `reference/claude-md-boas-praticas.md`.
- **Graphify** (`/graphify`, safishar, ~16k⭐) — skill que monta um grafo de
  conhecimento do codebase (JSON+HTML) como RAG local, visível no Obsidian.
- **rtk** — proxy de CLI que reduz consumo de tokens em 60–90% (binário Rust,
  filtra/comprime saídas de comandos antes de irem pro contexto).
- **code-review-graph** — mapa estrutural do código via Tree-sitter, contexto
  preciso para review via MCP.
- **brain-ingest** — transcreve YouTube/podcast/áudio → nota no Obsidian acessível ao Claude.
- **Obsidian + MCP** (smart-connections) — "segundo cérebro" conectado ao Claude.

### ✅ Técnicas/conceitos relevantes
- **Gestão de contexto/tokens** (carrossel @brandsdecoded_, base: vídeo do Nate Herk)
  → virou cheatsheet `reference/gestao-contexto-tokens.md`.
- **Skills = expertise empacotada** (@rafaelmilagre): markdown que ensina seu fluxo;
  agente genérico + biblioteca de skills > muitos agentes especializados.
- **Conectar MCP server remoto como Connector no claude.ai** (passos genéricos).

### 🔎 A verificar (não cataloguei como fato)
- **"Claude Managed Agents"** (@diegoalmeida.ia): alegação de que a Anthropic lançou
  infra gerenciada de agentes (beta público; Notion/Asana/Rakuten/Sentry usando).
  **Confirmar na fonte oficial** antes de documentar.
- Comandos citados a confirmar na doc: `/btw` (pergunta fora do histórico), `/re`.

### ❌ Ruído/pessoal (não entra): NeuroGus, gus-mcp-server, formulário médico,
Pix, Shakira Copacabana, farinha/focaccia, café, galáxias, móveis, ads (OpenClaw,
NVIDIA free APIs, DeepSeek, Cursor).

---

## Lote 2026-06-18 (f) — Instagram (em andamento)

> Varredura dos ~314 prints do Instagram (decisão do usuário: "tem muita coisa lá").
> Reporto só o relevante; ads/receitas/estudo de concurso = descartados.

### ⭐ Achados de alto valor
- **Mapa canônico da pasta `.claude/`** (@leadgenman) — referência ótima p/ um doc de
  estrutura. Arquivos: `CLAUDE.md` (advisory, <200 linhas), `CLAUDE.local.md` (overrides
  pessoais, gitignored), `.mcp.json` (servers MCP, na raiz), `.claude/` com `hooks/`
  (`PostToolUse.sh`, `SessionStart.sh`, `PreCompact.sh` — determinísticos), `commands/`
  (slash legacy), `skills/` (model-invokable, sob demanda), `agents/` (subagents, contexto
  isolado), `output-styles/`, `plugins/` (1st-class 2026, `/plugin:command`), `rules/`
  (path-scoped, carrega via glob — ⚠️ VERIFICAR se é oficial), `statusline`, `settings.json`
  + `settings.local.json`. Lema: "CLAUDE.md is advisory. hooks are deterministic. skills load on demand."
- 🎥 **Vídeo oficial Anthropic "Mastering Claude Code in 30 minutes"** (Boris Cherny) — referência.
- 📁 **Talk "Don't build agents, build skills" / "Skills are just folders"** (Barry Zhang & Mahesh Murag, Anthropic) — skill = pasta com `SKILL.md` + recursos (ex.: `apply_template.py`).

### Achados menores / tendências
- **paperclip** (`paperclip.ing`) — orquestração open-source de agentes (~51k stars).
- Demos de multi-agente em produção citam modelos reais: **`claude-sonnet-4-6`**, **`claude-haiku-4-5`** (confirma IDs).

### Mais achados (prints 41-80)
- **Técnica "premortem"** (@hollyfield.ia) — contra a bajulação do Claude ("acha tudo ótimo"),
  peça um premortem: "simule por que este plano fracassou daqui a X meses". (vira prompt/técnica)
- 📋 **Lista "15 coisas que instalei no Claude Code"** (@laschuk):
  - Skills: `superpowers`, `frontend-design`, `caveman` (corta ~65% dos tokens),
    `overclock-mkt` (pipeline de carrossel → PNG), `deploy` (deploy 1 comando).
  - MCP servers: `playwright` (opera sites), `supabase` (DB ao vivo), `overclock`
    (workspace + agentes visíveis), `sydra` (transcreve YouTube), `emailhacker` (email por voz).
  - Config: `CLAUDE.md`, `hooks`, `settings.json` (zero permissões), `~/.secrets`
    (credenciais fora do repo), `caveman mode` (respostas mais rápidas no terminal).
- 🌐 **agent-browser** (`vercel-labs/agent-browser`) — skill/plugin que dá "olhos" ao Claude
  Code: browser autônomo, "pull context from anywhere" (`.claude-plugin`).
- 🐝 **claude-flow v3** (@fabianocarvalhojr) — `npx claude-flow@v3alpha init`. Framework de
  orquestração: 60+ agentes especializados, swarms com 5 protocolos de consenso, "Queen-led",
  178+ MCP tools, 42+ skills, "RuVector Intelligence", 6 providers c/ failover. (⚠️ verificar repo)
- **Understand-Anything** (`Lum1104/Understand-Anything`) — plugin multi-plataforma
  (`.claude-plugin` / `.cursor-plugin` / `.copilot-plugin`), usa `docs/superpowers`.
- Variante da skill "Conselho/Council" também vista em @maxcarrauda (mesmo conceito do @gabrielsamp).

### Descartado (ruído)
Ads (ElevenLabs, curso frontend rodrigotadewald, GPAI, dermocosméticos, construção, etc.),
receitas, conteúdo de estudo p/ concurso, posts pessoais, e agentes de concorrentes (Gemini Omni/Spark).

---

## Lote 2026-06-18 (e) — restante da pasta (PARCIAL: ~140/625 lidos)

> A contagem real da pasta é **625 imagens** (não 100 — a paginação do Drive
> repetia a 1ª página). Li ~140 no total. O restante é majoritariamente pessoal.

### 🔴 ALERTA DE SEGURANÇA — credenciais expostas em prints (REVOGAR/ROTACIONAR)
- **`sk-ant-...`** (Anthropic API key) · **QDRANT** · **MEMO_API_KEY**
- **Telegram botfather token** · **GitHub token (GITHUB_T...)**
- **Supabase** (`NEXT_PUBLIC_SUPABASE_URL/ANON_KEY`) no Vercel
- (Antes: Qdrant key e ANTHROPIC_API_KEY no Railway)
- Nada disso foi copiado para o repositório.

### ✅ Achados relevantes (Claude Code) deste trecho
- **Claude Managed Agents** (verificado) → documentado em `docs/13-sdk-e-api.md`.
- **Boris Cherny (criador do Claude Code) — workflow mobile:** Claude Code tem app
  mobile (ele escreve código pelo iOS); `/teleport` continua uma sessão da nuvem na
  máquina local; `/remote-control` controla uma sessão local pelo celular.
- **GitNexus** (`abhigyanpatwari/GitNexus`) — grafo de conhecimento do codebase p/ Claude Code (MCP/skill).
- **Dashboard multi-Claude** (hesamsheikh, via @ohmo.ai) — roda vários Claude Code em paralelo no mesmo codebase.
- **Skill "Conselho dos 5" / Council** (@gabrielsamp.ai) — 5 "conselheiros" + peer review + chairman para reduzir alucinação ("fazer o Claude parar de mentir").
- **Prompt de monetização de habilidades** (@fabricadegpt) — Claude lista formas de monetizar + Perplexity valida demanda. (prompt reutilizável)

### ✅ Fechamento (decisão do usuário: "só apps de IA específicos")
Lidos também os ~20 prints restantes de Claude/ChatGPT/GitHub/DeepSeek.
**Nenhum conteúdo novo de Claude Code** — todos pessoais (app de finanças
`contas_roger`/Fluux, "Livro Dourado da República" p/ concurso, fichas de estudo,
mensagens "Fable 5 unavailable / mythos-access"). Os 328 Instagram + demais apps
(banco/gov/navegador) **não foram varridos** por decisão do usuário (ROI baixo,
risco de dado pessoal). Varredura encerrada.

**Total processado:** ~160 de 625 imagens. O conteúdo relevante de Claude Code
foi todo extraído e catalogado nos arquivos da biblioteca.

---

## Itens a transformar em conteúdo (backlog)

- [ ] Recipe: "Compartilhar memórias e skills em equipe via pasta sincronizada"
      (validar com post-session hook / SessionEnd).
- [ ] Seção/anexo: "Projetos feitos com Claude Code" (showcase) — começar com
      `neilsonnn/image-blaster`.
