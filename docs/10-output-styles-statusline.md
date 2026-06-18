# 10 — Output styles e status line

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Refs: `code.claude.com/docs/en/output-styles`, `/statusline`.

## O que é

Dois recursos de **personalização da experiência**:
- **Output styles** — mudam o **papel/tom/formato** das respostas do Claude (via system
  prompt). Vigente em 2026.
- **Status line** — uma **barra inferior customizada** no terminal, gerada por um script
  seu (mostra contexto, custo, git, etc.).
- (Bônus) **Keybindings** — atalhos customizáveis em `~/.claude/keybindings.json`.

## Quando usar

| Quer… | Use |
|---|---|
| Respostas mais didáticas / num papel específico | **output style** |
| Modo "ensina enquanto faz" | output style **Learning** |
| Ver uso de contexto/custo/branch sempre à vista | **status line** |
| Rebindar teclas/atalhos | **keybindings** |

## Como configurar / usar

### Output styles
- **Built-ins:** `Default`, `Proactive`, `Explanatory`, `Learning`.
- **Trocar:** comando `/config`, ou chave `"outputStyle"` no `settings.json`.
- **Customizado:** arquivo `.md` com frontmatter em `.claude/output-styles/` (projeto),
  `~/.claude/output-styles/` (usuário) ou dentro de um plugin.
```markdown
---
name: Conciso-PTBR
description: Respostas curtas e diretas em português, sem floreio.
keep-coding-instructions: true
---

Responda em PT-BR, direto ao ponto. Sem introduções longas.
Mostre código quando ajudar; explique só o essencial.
```

### Status line
- Chave **`statusLine`** no `settings.json` apontando pra um script.
- O script recebe **JSON da sessão no stdin** e o que ele **imprime aparece na barra**
  (suporta múltiplas linhas e cores ANSI). Fica **acima** dos badges nativos.
```json
{ "statusLine": "${CLAUDE_PROJECT_DIR}/.claude/statusline.sh" }
```
```bash
#!/usr/bin/env bash
# recebe JSON no stdin; imprime uma linha de status
input=$(cat)
branch=$(git branch --show-current 2>/dev/null)
printf "⎇ %s" "${branch:-sem-git}"
```

### Keybindings
- Customizáveis em `~/.claude/keybindings.json` (rebind, chords, tecla de envio, etc.).

## Exemplo

- Ative o estilo didático: `/config` → Output style → **Explanatory**.
- Ou fixe no projeto:
```json
{ "outputStyle": "Explanatory", "statusLine": "${CLAUDE_PROJECT_DIR}/.claude/statusline.sh" }
```

## Pegadinhas ⚠️

- **Output styles não foram deprecados** — seguem vigentes em 2026.
- **Status line é um script:** se ele for lento ou quebrar, atrapalha a UI; deixe rápido e
  à prova de erro (ex.: `2>/dev/null`).
- **`keep-coding-instructions`** no output style controla se as instruções de código base
  são mantidas — desligue só se souber o que está fazendo.
- **Não confunda** output style (formato da resposta) com `CLAUDE.md` (contexto do projeto)
  nem com skills (capacidades).

## Referências oficiais

- Output styles: https://code.claude.com/docs/en/output-styles
- Status line: https://code.claude.com/docs/en/statusline
- (relacionado) Settings: `docs/03`
</content>
