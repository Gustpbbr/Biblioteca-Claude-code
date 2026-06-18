# 08 — MCP (Model Context Protocol)

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Ref: `code.claude.com/docs/en/mcp`.

## O que é

**MCP (Model Context Protocol)** é o padrão aberto que conecta o Claude Code a
**ferramentas e dados externos** via **servidores MCP**: bancos de dados, navegadores,
APIs (GitHub, Notion, Figma), automação (n8n), 3D (Blender, SketchUp), etc. Um servidor
MCP expõe **tools**, **resources** e **prompts** que o Claude passa a poder usar.

## Quando usar

| Quer… | Use MCP |
|---|---|
| Dar ao Claude acesso a um sistema externo (DB, API, app) | ✅ |
| Operar um navegador, gerar imagem/vídeo, mexer no Blender | ✅ (servidor específico) |
| Só rodar comandos locais de shell | ❌ já tem a tool `Bash` |

## Como configurar / usar

### Tipos de servidor
- **stdio** — processo local (ex.: um binário/Node que fala MCP pelo stdin/stdout).
- **HTTP / SSE** — servidor remoto acessível por URL.

### Escopos (onde a config vive)
| Escopo | Arquivo | Compartilhado? |
|---|---|---|
| **local** | `~/.claude.json` (por projeto, pessoal) | só você |
| **project** | **`.mcp.json` na raiz do projeto** | ✅ time (versionado) |
| **user** | `~/.claude.json` (entrada de topo) | você, todos os projetos |

> ⚠️ O `.mcp.json` do time fica na **raiz do repositório**, **não** em `.claude/`.

### Adicionar servidores
```bash
# via CLI (jeito mais fácil)
claude mcp add github --transport http https://api.githubcopilot.com/mcp
claude mcp list
```
Ou editando `.mcp.json` direto:
```json
{
  "mcpServers": {
    "meu-servidor": {
      "type": "http",
      "url": "https://exemplo.com/mcp"
    },
    "local-tool": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "algum-mcp-server"]
    }
  }
}
```

### Conectores no app (claude.ai / Desktop)
No app: **Configurações → Connectors → "Add custom connector (BETA)"** e cole a URL do
**Remote MCP** (ex.: `https://mcp.higgsfield.ai/mcp`). Há também conectores oficiais
(Anthropic & Partners): Canva, Figma, Notion, Google Drive, Atlassian, Google Calendar,
Trimble SketchUp, Autodesk Fusion, etc.

### Aprovação e uso
- Na **primeira vez**, o Claude Code **pede aprovação** pra usar um servidor de projeto
  (segurança). Depois disso as tools dele ficam disponíveis ao Claude.

## Exemplo

`.mcp.json` (na raiz, versionado pro time):
```json
{
  "mcpServers": {
    "n8n": { "type": "http", "url": "https://meu-n8n-mcp.exemplo.com/mcp" }
  }
}
```
Agora o Claude pode "montar um workflow no n8n" usando as tools do servidor.

## Pegadinhas ⚠️

- **`.mcp.json` na raiz, não em `.claude/`.** (Erro comum.)
- **Aprovação na 1ª vez** é proposital — não é bug.
- **Supply-chain:** um servidor MCP pode ler dados sensíveis e agir em sistemas externos.
  Use só servidores confiáveis, prefira escopos restritos e revise antes de versionar no
  `.mcp.json` do time (lembre do incidente de jun/2026 na pesquisa).
- **Escopo local vs project vs user:** se "some" entre máquinas, provavelmente está no
  escopo errado (local/user são pessoais; project é versionado).

## Referências oficiais

- MCP: https://code.claude.com/docs/en/mcp
- (relacionado) Plugins (que podem trazer MCP): `docs/09` · Anatomia: `reference/anatomia-projeto-claude.md`
- Servidores MCP úteis no catálogo: `reference/repos-recomendados.md`
</content>
