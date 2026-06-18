# 14 — Habilidades de mídia (imagem, vídeo, áudio, design)

O Claude Code não edita pixels sozinho — ele ganha "habilidades de mídia" por
dois caminhos: **Skills** (instruções + scripts em `.claude/skills/`) e
**servidores MCP** (que expõem ferramentas de imagem/vídeo/áudio/design). Este
doc cataloga o que existe e o que está disponível nesta sessão.

## O que é

- **Skill de mídia:** um `SKILL.md` que ensina o agente a produzir/editar mídia
  (ex: gerar slides em HTML, criar banner, montar um deck em PDF). Pode trazer
  scripts (Python, etc.) e seguir a [spec agentskills.io](https://agentskills.io/specification).
- **MCP de mídia:** um servidor que dá ao Claude ferramentas reais — remover
  fundo de imagem, renderizar vídeo, transcrever áudio, gerar design.

## Quando usar

- Precisa **gerar/editar imagem** (fundo, cor, recorte, vetorizar) → MCP de imagem (Adobe) ou skill de design.
- Precisa **mexer em vídeo** (cortar, redimensionar, extrair frame, animar) → MCP de vídeo (Adobe).
- Precisa de **áudio** (melhorar fala, resumir mídia, playlists) → MCP (Adobe media, Spotify).
- Precisa de **design/UI, banner, slides, PDF** → skills (ui-ux-pro-max, wowerpoint) ou Canva/Figma MCP.

---

## Integrações de mídia disponíveis nesta sessão (via MCP)

> Estas são capacidades reais conectadas neste ambiente. Em outro projeto, você
> habilita os MCPs correspondentes (ver `docs/08-mcp.md`).

### 🖼️ Imagem / Foto — Adobe (creativity)
- **Conteúdo:** remover fundo, expandir (generative expand), vetorizar, recortar/
  redimensionar, preencher área, selecionar por prompt/assunto, inverter seleção.
- **Ajustes:** brilho/contraste, temperatura de cor, exposição, realces, sombras,
  HSL, saturação por cor, vibração/saturação, auto-tom, presets.
- **Efeitos:** desfoque (gaussiano/lente), glitch, meio-tom (halftone), grão,
  ruído, tom monocromático, sobreposição de cor; auto-endireitar.

### 🎬 Vídeo — Adobe (creativity)
- Quick cut (corte rápido), render, extrair frame, redimensionar, metadados,
  **animar design**.

### 🔊 Áudio / Mídia
- **Adobe:** melhorar fala (`enhance_speech`), resumir mídia (`summarize`).
- **Spotify:** buscar faixas, criar playlist, ver o que está tocando.

### 🎨 Design / Documentos
- **Adobe:** criar design (Express), preencher texto, recomendar/buscar fontes,
  converter PDF, mesclar dados em layout, exportar IDML, mudar cor de fundo.
- **Canva:** gerar design, editar, exportar, templates de marca, redimensionar.
- **Figma:** ler/gerar design, screenshots, design system, **gerar diagramas** (FigJam).

---

## Skills e plugins de mídia da comunidade (catálogo)

> Verificados em jun/2026 (fetch direto de repo/SKILL.md ou múltiplas fontes).
> ⚠️ alguns marcados como *reconferir* (fonte única ou página com bloqueio a fetch).
> Onde achar mais: **anthropics/skills** (oficial), **VoltAgent/awesome-agent-skills**
> (~1.400 skills, diretório officialskills.sh), **travisvn/awesome-claude-skills**.

### 📄 Documentos / Apresentações
- **document-skills (OFICIAL Anthropic)** — criar/ler/editar **pptx, docx, xlsx, pdf**
  (deck do zero via `pptxgenjs`, notas de orador, templates).
  `/plugin marketplace add anthropics/skills` → `/plugin install document-skills@anthropic-agent-skills`
- **wowerpoint** (`thedotmack/claude-mem`) — 1 documento → slide-deck PDF estilo NotebookLM.
- **cc-slidev** (`rhuss/cc-slidev`) — apresentações técnicas com Slidev (≤6 elementos/slide).
- **marp-slides** (`robonuggets/marp-slides`) — apresentações MARP (SVG, temas, exemplos).
- **frontend-slides** (`zarazhangrui`) — apresentações HTML animadas; converte de/para PPTX.

### 🎨 Design / UI
- **frontend-design (OFICIAL)** — design visual distintivo (tipografia, cor, direção
  estética não-"template"). `/plugin install frontend-design@claude-plugins-official`
- **canvas-design (OFICIAL)** — arte visual estática em **.png/.pdf** (pôster, peça de arte).
- **web-artifacts-builder (OFICIAL)** — artefatos web autônomos (React + Tailwind + shadcn/ui).
- **algorithmic-art / brand-guidelines / theme-factory (OFICIAIS)** — arte generativa (p5.js),
  aplicação de marca, fábrica de temas. `/plugin install example-skills@anthropic-agent-skills`
- **ui-ux-pro-max** (`nextlevelbuilder/ui-ux-pro-max-skill`, MIT) — 161 regras, 67 estilos;
  sub-skills `design`, `banner-design`, `slides` (Chart.js), `brand`, `design-system`, `ui-styling`.
- **design-is** (`thedotmack/claude-mem`) — auditoria de design pelos 10 princípios de Dieter Rams.

### 🖼️ Imagem / Foto
- **Adobe for Creativity (Connector OFICIAL)** — 50+ ferramentas (Photoshop/Lightroom/
  Illustrator/Firefly/Express). ✅ já conectado nesta sessão.
- **replicate/skills (OFICIAL Replicate)** — `prompt-images` (gerar/editar imagem) e
  `prompt-videos` (Flux/SDXL etc.). `npx skills add replicate/skills`
- **Image Production Plugin** (`danielrosehill/Claude-Image-Production-Plugin`) — lote:
  remover fundo, upscaling 2–4× (Real-ESRGAN), raster→SVG, WebP/AVIF (ImageMagick/libvips).
- **imagegen-mcp** (`writingmate/imagegen-mcp`) — MCP multimodelo (GPT-Image-1, DALL-E,
  Imagen 4, Gemini "Nano Banana", Flux 1.1 Pro, Qwen, SeedDream-4).
- **nano-banana-2-skill** (`kingbootoshi`) / **cc-nano-banana** (`kkoppenhaver`) /
  **claude-image-gen** (`guinacio`, MIT) — geração/edição via Gemini Image.

### 🎬 Vídeo
- **Adobe MCP** — `video_create_quick_cut`, `video_render`, `video_resize`. ✅ nesta sessão.
- **claude-ffmpeg-skill** (`ychoi-kr`) — FFmpeg: converter, escalar, GIF, extrair áudio,
  trim, legendas, thumbnails, compressão. (a skill mais "faz-tudo" de vídeo)
- **video-use** (`browser-use/video-use`) — corta filler/silêncio, color-grade, fades,
  legendas, overlays (Remotion/Manim + FFmpeg + ElevenLabs).
- **claude-video `/watch`** (`bradautomates/claude-video`) — ingere vídeo: baixa, extrai
  frames (ffmpeg), transcreve (Whisper). É análise, não edição.
- **video-audio-mcp** (`misbahsy`) — MCP (FastMCP + FFmpeg): conversão, trim, overlays, transições.

### 🔊 Áudio
- **ElevenLabs MCP (OFICIAL)** — TTS, clonagem de voz, SFX, transcrição (Scribe), isolamento
  de voz. `claude mcp add elevenlabs -e ELEVENLABS_API_KEY=<key> -- uvx elevenlabs-mcp`
- **Adobe MCP** — `media_enhance_speech` e `media_summarize`. ✅ nesta sessão.
- **Audio Production Plugin** (`danielrosehill/Claude-Audio-Production-Plugin`, MIT) —
  normalização EBU R128, denoise, compressão, de-essing, montagem (FFmpeg).

### 📊 Diagramas / Canvas
- **claude-mermaid** (`veelenga/claude-mermaid`) — MCP que renderiza Mermaid com live
  reload, export SVG/PNG/PDF. `/plugin install claude-mermaid@claude-mermaid`
- **Excalidraw MCP (OFICIAL)** — diagramas "à mão". ✅ nesta sessão.
- **drawio-mcp (OFICIAL jgraph)** — gera `.drawio` com export PNG/SVG/PDF.
- **json-canvas** (`kepano/obsidian-skills`, MIT) — arquivos `.canvas` (mind maps, fluxogramas).
- **Figma `generate_diagram`** (FigJam) — diagramas via MCP. ✅ nesta sessão.

### 📣 Conteúdo social
- **social-content** (`davila7/claude-code-templates`) — conteúdo para LinkedIn, X,
  Instagram, TikTok, Facebook.

---

## Como instalar (3 mecanismos)

```bash
# 1) Plugin/skill oficial (marketplace de plugin)
/plugin marketplace add <org>/<repo>
/plugin install <plugin>@<marketplace>     # ex: document-skills@anthropic-agent-skills

# 2) CLI npx skills (vercel-labs/skills, registro skills.sh) — "npm para skills"
npx skills add <org>/<repo>                 # --skill <nome>, -g (global), -a claude-code

# 3) Servidor MCP (stdio/http)
claude mcp add <nome> -- <comando>          # ou: claude mcp add --transport http <nome> <url>

# Manual: copie a pasta da skill para .claude/skills/<nome>/ (spec agentskills.io)
```

## Pegadinhas

- **Skills ≠ MCP:** skill é instrução/receita; MCP é ferramenta executável. Muitas
  skills de mídia *dependem* de um MCP ou CLI externo (ex: ffmpeg, notebooklm).
- **Custos e contas:** MCPs como Adobe/Canva podem exigir conta/limites de uso.
- **Segurança:** skills de terceiros podem rodar scripts — revise antes (ver alerta
  em `reference/repos-recomendados.md`).
- **Geração de imagem/vídeo "do zero"** geralmente exige um MCP de modelo generativo
  (ex: Adobe Firefly, Replicate) — o Claude Code orquestra, não gera pixel nativamente.
- **`agentskills.io` é a *especificação*, não um CLI** — o CLI real é `npx skills`
  (vercel-labs/skills, registro skills.sh).
- **`gofireflyio/firefly-mcp` NÃO é o Adobe Firefly** — é infra-as-code (Terraform).
  O Firefly da Adobe vem pelo connector "Adobe for Creativity".
- **Não existe "OpenAI image MCP" oficial** — modelos de imagem da OpenAI vêm por MCPs
  multimodelo (ex: `imagegen-mcp`) com `OPENAI_API_KEY`.
- **Não há skill oficial Anthropic de "diagramas"** — diagramas vêm de MCPs (Figma
  `generate_diagram`, Mermaid, Excalidraw, draw.io).

## Referências oficiais

- Skills no Claude Code: https://code.claude.com/docs/en/skills
- Descobrir plugins: https://code.claude.com/docs/en/discover-plugins
- MCP no Claude Code: https://code.claude.com/docs/en/mcp
- Spec de Agent Skills: https://agentskills.io
- CLI de skills: https://github.com/vercel-labs/skills · https://www.skills.sh/
- Catálogos: https://github.com/anthropics/skills · https://github.com/VoltAgent/awesome-agent-skills · https://github.com/travisvn/awesome-claude-skills
