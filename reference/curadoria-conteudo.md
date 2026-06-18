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

## Itens a transformar em conteúdo (backlog)

- [ ] Recipe: "Compartilhar memórias e skills em equipe via pasta sincronizada"
      (validar com post-session hook / SessionEnd).
- [ ] Seção/anexo: "Projetos feitos com Claude Code" (showcase) — começar com
      `neilsonnn/image-blaster`.
