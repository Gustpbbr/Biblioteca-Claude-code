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

## Itens a transformar em conteúdo (backlog)

- [ ] Recipe: "Compartilhar memórias e skills em equipe via pasta sincronizada"
      (validar com post-session hook / SessionEnd).
- [ ] Seção/anexo: "Projetos feitos com Claude Code" (showcase) — começar com
      `neilsonnn/image-blaster`.
