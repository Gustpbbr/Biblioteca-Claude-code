# 🎬 Receita: Animar uma foto em vídeo (image-to-video)

> Como pegar **uma foto parada** e transformá-la num **vídeo curto** (ex: 5s) pelo
> Claude Code — desde o movimento simples de "slideshow" (zoom/pan) até a animação
> **generativa** de verdade (a foto "ganha vida": cabelo balança, água se mexe,
> a câmera orbita).
>
> ⚠️ Plataformas, nomes de modelo e **preços** de geração de vídeo mudam rápido.
> Confirme na doc/página de preços de cada serviço antes de depender de detalhes.
> Última revisão: 2026-06-19.

---

## 🎯 Objetivo

Sair de `foto.jpg` → `video.mp4` de ~5 segundos, escolhendo o nível de movimento
certo para o seu caso (e sabendo o custo de cada caminho).

---

## 💡 A grande sacada: existem 3 níveis de "animar foto"

São coisas técnicas diferentes, com ferramentas e custos diferentes. Decida qual
você quer **antes** de escolher a ferramenta.

| Nível | O que acontece | Parece com | Precisa de... |
|-------|----------------|------------|---------------|
| **1. Movimento de câmera** | A foto continua estática; só a "câmera" dá zoom/pan/fade | Slideshow, Stories, efeito Ken Burns | Editor/timeline — **sem IA generativa** |
| **2. Render de clipe** | A foto vira um clipe de N segundos (quadro parado) + transições/áudio | Cartão, intro estática | Render de vídeo simples |
| **3. Animação generativa** | A imagem **se mexe** de verdade (pessoas piscam, água flui, parallax 3D) | Runway/Kling/Sora, "live photo" | **Modelo image-to-video** (pago, por GPU) |

> 🔑 Regra de ouro: **só o Nível 3 é "IA animando a foto"**. Os níveis 1 e 2 são
> edição de vídeo comum (a foto não muda, só a câmera/tempo).

---

## 🧭 Nível 1 e 2 — movimento simples (sem modelo generativo)

Dá pra fazer com as ferramentas de mídia já comuns numa sessão com **MCP da Adobe**
conectado (ver `docs/14-habilidades-de-midia.md`):

- **`animate_design`** (Adobe Express) — coloca a foto num design e aplica
  **movimento**: zoom (Ken Burns), pan, fade, deslize. É o mais próximo de
  "animar a foto" sem IA generativa.
- **`video_render`** — monta um clipe de N segundos a partir da imagem (fit/fill,
  rotação, áudio opcional). Quadro estático.

✅ **Bom quando:** você só quer um movimentinho de slideshow, intro, capa animada.
❌ **Não serve quando:** você quer que o *conteúdo* da foto se mexa (aí é Nível 3).

---

## 🚀 Nível 3 — animação generativa (image-to-video)

Aqui a foto realmente ganha vida. O Claude Code **orquestra** um modelo generativo;
ele não gera vídeo nativamente. Você habilita o acesso ao modelo por **skill** ou
**MCP** e depois pede em linguagem natural.

### Caminho recomendado: skill `replicate/skills`

A [Replicate](https://replicate.com) hospeda vários modelos de imagem e vídeo
atrás de uma API única. A skill oficial da Replicate expõe `prompt-images`
(gerar/editar imagem) e `prompt-videos` (gerar vídeo, inclusive image-to-video).

#### Passo 1 — Token da Replicate
1. Crie conta em **replicate.com**.
2. **Account → API tokens** → copie a token (formato `r8_...`).
3. É **pago por uso** (por segundo de GPU). Vídeo custa bem mais que imagem —
   confira o preço do modelo específico antes de rodar em lote.

#### Passo 2 — Instalar a skill
No terminal, dentro do projeto (ou global com `-g`):
```bash
npx skills add replicate/skills
# opções: -g (global) · -a claude-code · --skill prompt-videos (só a de vídeo)
```
> `npx skills` é o CLI de skills (vercel-labs/skills, registro skills.sh). Ver os
> 3 mecanismos de instalação em `docs/14-habilidades-de-midia.md`.

#### Passo 3 — Autenticar
```bash
export REPLICATE_API_TOKEN="r8_sua_token_aqui"
```
> 🔒 Não comite a token. Use `.env` ignorado pelo git ou os secrets do seu SO/CI.

#### Passo 4 — Usar
Reinicie o Claude Code (pra carregar a skill) e peça em linguagem natural:
> "Use a skill prompt-videos pra animar `foto.jpg` num vídeo de 5s: câmera com
> zoom lento pra dentro, o fundo se movendo suavemente, sem distorcer o rosto."

---

## ✍️ Como escrever um bom prompt de image-to-video

O modelo recebe **sua imagem + um texto descrevendo o movimento**. Dicas:

- **Descreva o movimento, não a cena** (a cena já está na foto): "câmera empurra
  lentamente pra frente", "leve parallax", "cabelo e folhas balançam ao vento".
- **Diga o que NÃO deve mudar:** "mantenha o rosto e a identidade estáveis",
  "sem morphing", "sem mudar as cores".
- **Defina a duração e o ritmo:** "5 segundos", "movimento lento e contínuo".
- **Comece curto e barato** (3–5s, resolução menor) pra validar antes de gastar
  em renders longos/HD.

---

## 🔀 Alternativas ao Replicate (Nível 3)

| Opção | Como entra no Claude Code | Notas |
|-------|---------------------------|-------|
| **Replicate** (`replicate/skills`) | skill + `REPLICATE_API_TOKEN` | catálogo multimodelo; recomendado p/ começar |
| **MCP multimodelo** (ex: `imagegen-mcp`) | servidor MCP + API key | foco em imagem; checar suporte a vídeo |
| **Runway / Kling / Hailuo / Luma / Pika** | API própria via MCP/skill caseiro | qualidade alta; cada um com SDK e preço próprios |
| **Adobe Firefly Video** | connector Adobe (quando expor a tool) | dentro do ecossistema Adobe; ver `docs/14` |

> ⚠️ Disponibilidade de cada modelo no catálogo da Replicate (Kling, Wan, Hailuo
> etc.) muda com o tempo — confira a página do modelo antes de fixar no fluxo.

---

## 🌐 Pegadinha: sessão na nuvem (Claude Code web) vs. local

- **Local (terminal/IDE):** você controla rede e variáveis de ambiente — os passos
  acima funcionam direto. **É o caminho mais simples.**
- **Claude Code na web/cloud:** o container é isolado e o **acesso de rede é
  limitado pela política do ambiente**; `REPLICATE_API_TOKEN` precisa estar
  configurado como variável de ambiente do ambiente web. Se a política bloquear
  `replicate.com`, a chamada falha. Ver `docs/11-ide-e-web-cloud.md`.

---

## ⚠️ Pegadinhas gerais

- **Claude não gera pixel/vídeo sozinho** — ele orquestra um modelo (Adobe Firefly,
  Replicate, etc.). Sem MCP/skill generativo, só dá Nível 1/2.
- **Custo cresce com duração e resolução** — vídeo é cobrado por segundo de GPU;
  teste curto antes de render longo.
- **Direitos de imagem e pessoas reais** — anime fotos que você tem direito de usar;
  cuidado com semelhança de pessoas reais (deepfake).
- **Áudio é à parte** — a maioria dos modelos image-to-video entrega só vídeo;
  trilha/voz vêm de outra ferramenta (ver áudio em `docs/14`).
- **`npx skills` ≠ `agentskills.io`** — `agentskills.io` é a *especificação*; o CLI
  real é `npx skills` (vercel-labs/skills).

---

## 📚 Referências

- Habilidades de mídia (catálogo completo): [`docs/14-habilidades-de-midia.md`](../docs/14-habilidades-de-midia.md)
- IDE e Claude Code na web/cloud: [`docs/11-ide-e-web-cloud.md`](../docs/11-ide-e-web-cloud.md)
- Skills no Claude Code: https://code.claude.com/docs/en/skills
- CLI de skills: https://github.com/vercel-labs/skills · https://www.skills.sh/
- Replicate: https://replicate.com · skill: https://github.com/replicate/skills
