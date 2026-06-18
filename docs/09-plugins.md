# 09 — Plugins

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Confira `https://code.claude.com/docs/en/plugins` antes de depender de detalhes.

## O que é

Um **plugin** empacota várias extensões do Claude Code em **uma pasta autocontida e
distribuível**: skills, subagents, hooks, servidores MCP, servidores LSP, slash commands
e binários. Em 2026 plugins são **cidadãos de primeira classe** — o jeito recomendado de
**reusar e distribuir** configuração entre projetos e times (enquanto `.claude/` é pra
config sob medida de **um** projeto).

O que um plugin pode conter:
- **Skills** (`skills/<nome>/SKILL.md`)
- **Agents/subagents** (`agents/<nome>.md`)
- **Hooks** (`hooks/hooks.json`)
- **MCP servers** (`.mcp.json`)
- **LSP servers** (`.lsp.json`) e **monitors** (`monitors/monitors.json`)
- **Binários** (`bin/`, adicionados ao PATH)

## Quando usar

| Situação | Use |
|---|---|
| Config específica de **um** projeto | `.claude/` direto (ver `docs/anatomia`) |
| Quero **reusar** um conjunto de skills/agents/hooks em vários projetos | **Plugin** |
| Quero **distribuir** pra um time ou comunidade | Plugin + **marketplace** |
| Empacotar uma metodologia inteira (skills + hooks + MCP juntos) | Plugin |

## Como configurar / usar

### Estrutura de um plugin
```
meu-plugin/
├── .claude-plugin/
│   └── plugin.json          # manifesto: name, description, version, author (SÓ isto aqui)
├── skills/
│   └── deploy/SKILL.md
├── agents/
│   └── revisor.md
├── hooks/
│   └── hooks.json
├── .mcp.json                # MCP servers do plugin
├── .lsp.json                # LSP servers (opcional)
├── monitors/monitors.json   # (opcional)
└── bin/                     # executáveis adicionados ao PATH (opcional)
```

> ⚠️ **Só o `plugin.json` vai dentro de `.claude-plugin/`.** Skills, agents e hooks ficam
> na **raiz do plugin** (não dentro de `.claude-plugin/`).

### Comandos
- **`/plugin`** — gerenciador de plugins (instalar, listar, habilitar/desabilitar).
- **`/plugin install <nome>`** — instala um plugin.
- **`/plugin marketplace add <org>/<repo>`** — adiciona um marketplace (repo GitHub) como
  fonte de plugins. Ex.: `/plugin marketplace add kepano/obsidian-skills`.

### Marketplaces
- Oficial: `anthropics/claude-plugins-official`
- Comunidade: `anthropics/claude-plugins-community`
- Qualquer repo GitHub com o layout de marketplace pode ser adicionado.

### Testar um plugin local (sem publicar)
```
claude --plugin-dir ./meu-plugin
```

### Namespacing
Skills/commands de um plugin aparecem com **prefixo** pra evitar conflito:
`/<nome-do-plugin>:<comando>` (ex.: `/superpowers:brainstorm`).

## Exemplo (instalar uma skill via marketplace)

```
# 1. adiciona o repo como marketplace
/plugin marketplace add kepano/obsidian-skills

# 2. instala o plugin de lá
/plugin install obsidian@obsidian-skills

# 3. usar (namespaced)
/obsidian:...
```

> Skills publicadas como pasta em `~/.claude/skills/<nome>/.claude-plugin/plugin.json`
> também são auto-carregadas como `<nome>@skills-dir`.

## Pegadinhas ⚠️

- **`.claude-plugin/` ≠ raiz do plugin.** Erro comum: jogar `skills/` dentro de
  `.claude-plugin/`. Só o `plugin.json` mora ali; o resto fica na raiz.
- **Namespacing muda o nome do comando.** Depois de instalar, é `/plugin:comando`, não
  `/comando` — não se assuste se o nome "mudar".
- **Marketplace é um repo GitHub.** `marketplace add` aponta pra um repositório; confie na
  fonte antes de adicionar.
- **Supply-chain.** Plugin pode trazer hooks (executam comandos), MCP e binários. **Leia o
  código, confira hooks/permissões e fixe versões** antes de instalar de terceiros
  (lembre do incidente de jun/2026 documentado na pesquisa).
- **Plugin vs `.claude/`.** Não duplique: use `.claude/` pra o que é exclusivo do projeto e
  plugin pra o que você quer reusar/distribuir.

## Referências oficiais

- Plugins: https://code.claude.com/docs/en/plugins
- Marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- (relacionados) Skills `docs/07`, Hooks `docs/06`, MCP `docs/08`, Subagents `docs/05`.

> Curadoria relacionada: muitos repos do catálogo são plugins (`.claude-plugin/`) —
> ver `reference/repos-recomendados.md` (superpowers, knowledge-work-plugins,
> Anthropic-Cybersecurity-Skills, ui-ux-pro-max, etc.).
</content>
