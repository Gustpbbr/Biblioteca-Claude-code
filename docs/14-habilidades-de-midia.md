# 14 — Habilidades de mídia (imagem, vídeo, áudio, design)

O Claude Code não edita pixels sozinho — ele ganha "habilidades de mídia" por
dois caminhos: **Skills** (instruções + scripts em `.claude/skills/`) e
**servidores MCP** (que expõem ferramentas de imagem/vídeo/áudio/design). Este
doc cataloga o que existe e o que está disponível nesta sessão.

> 🚧 Em construção — seção de skills da comunidade será enriquecida com a pesquisa.

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

## Skills de mídia da comunidade (catálogo)

> Verificadas em repositórios reais (jun/2026). Instale copiando para
> `.claude/skills/` ou via marketplace, conforme o repo.

### Design / UI / Banner / Slides
- **ui-ux-pro-max** (`nextlevelbuilder/ui-ux-pro-max-skill`, MIT) — design intelligence
  com 161 regras e 67 estilos. Inclui sub-skills: `design`, `banner-design`
  (Facebook/IG/LinkedIn/YouTube/print, vários estilos), `slides` (apresentações
  HTML com Chart.js), `brand`, `design-system`, `ui-styling`.
- **design-is** (em `thedotmack/claude-mem`) — auditoria de design pelos 10
  princípios do Dieter Rams, com handoff para um plano.

### Apresentações / Documentos
- **wowerpoint** (em `thedotmack/claude-mem`) — transforma 1 documento em um
  slide-deck PDF estilo NotebookLM ("wowerpoint this", "make a deck about <file>").
- Skills oficiais de criação de documentos (pptx/docx/pdf/xlsx) — ver pesquisa.

### Diagramas / Canvas
- **json-canvas** (`kepano/obsidian-skills`, MIT) — cria/edita arquivos `.canvas`
  (mind maps, fluxogramas) seguindo a JSON Canvas Spec 1.0.
- **Figma `generate_diagram`** (FigJam) — diagramas via MCP.

### Conteúdo social / marketing
- **social-content** (`davila7/claude-code-templates`) — criação/agendamento de
  conteúdo para LinkedIn, X, Instagram, TikTok, Facebook.

---

## Como instalar uma skill

```bash
# Via marketplace de plugin (quando o repo é um plugin)
/plugin marketplace add <org>/<repo>
/plugin install <skill>@<repo>

# Via npx skills (repos compatíveis com agentskills.io)
npx skills add https://github.com/<org>/<repo>

# Manualmente: copie a pasta da skill para .claude/skills/<nome>/
```

## Pegadinhas

- **Skills ≠ MCP:** skill é instrução/receita; MCP é ferramenta executável. Muitas
  skills de mídia *dependem* de um MCP ou CLI externo (ex: ffmpeg, notebooklm).
- **Custos e contas:** MCPs como Adobe/Canva podem exigir conta/limites de uso.
- **Segurança:** skills de terceiros podem rodar scripts — revise antes (ver alerta
  em `reference/repos-recomendados.md`).
- **Geração de imagem/vídeo "do zero"** geralmente exige um MCP de modelo generativo
  (ex: Adobe Firefly, Replicate) — o Claude Code orquestra, não gera pixel nativamente.

## Referências oficiais

- Skills no Claude Code: https://code.claude.com/docs/en/skills
- MCP no Claude Code: https://code.claude.com/docs/en/mcp
- Spec de Agent Skills: https://agentskills.io/specification
- _Demais fontes da comunidade: ver `reference/` (pesquisa será mesclada aqui)._
