# 06 — Hooks

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> A lista completa e atual de eventos está em `https://code.claude.com/docs/en/hooks`.

## O que é

**Hooks** são comandos de shell que o Claude Code executa **automaticamente** em pontos
específicos do ciclo de vida (antes/depois de usar uma ferramenta, ao iniciar a sessão,
ao terminar uma resposta, etc.). Diferente do `CLAUDE.md` (que é **orientação** que o
modelo pode seguir ou não), **hooks são determinísticos** — rodam sempre, independente do
que o modelo "decide".

> Lema: **CLAUDE.md é advisory. Hooks são determinísticos. Skills carregam sob demanda.**

Casos típicos: rodar lint/format depois de editar, **bloquear** comandos perigosos antes
de executá-los, carregar contexto no início da sessão, auto-commitar, logar atividade.

## Quando usar

| Quer… | Use hook |
|---|---|
| Garantir que algo **sempre** acontece (não "se o modelo lembrar") | ✅ |
| Bloquear uma ação perigosa antes de rodar (ex.: `rm -rf`) | ✅ `PreToolUse` (exit 2) |
| Formatar/testar automaticamente após edição | ✅ `PostToolUse` |
| Injetar contexto no começo da sessão | ✅ `SessionStart` |
| Só dar uma instrução que o modelo *deveria* seguir | ❌ use `CLAUDE.md` |

## Como configurar / usar

### Onde se configura
Hooks são definidos **dentro dos arquivos de settings** (não numa pasta própria):
- `.claude/settings.json` (time) · `.claude/settings.local.json` (pessoal) ·
  `~/.claude/settings.json` (usuário) · plugins (`hooks/hooks.json`).

Os **scripts** podem ficar em `.claude/hooks/` e são referenciados por caminho.

### Eventos principais
- **`SessionStart`** — início/retomada da sessão (bom p/ carregar contexto).
- **`UserPromptSubmit`** — quando você envia um prompt.
- **`PreToolUse`** — **antes** de uma ferramenta rodar. Pode **bloquear** (exit code `2`).
- **`PostToolUse`** — **depois** de uma ferramenta ter sucesso (lint/format/testes).
- **`Stop`** — quando o Claude termina de responder.
- **`PreCompact`** — antes da compactação de contexto (salvar estado).
- **`Notification`**, **`SubagentStop`**, **`SessionEnd`**, **`InstructionsLoaded`** — entre outros.

> A lista canônica/atual está na doc oficial — confira lá antes de depender de um evento específico.

### Formato (em `settings.json`)
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-dangerous.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "npm run format --silent" }
        ]
      }
    ]
  }
}
```
- **`matcher`** filtra por ferramenta (ex.: `Bash`, `Edit|Write`). Vazio/omisso = todos.
- O hook recebe um **JSON no stdin** (dados da sessão/ferramenta) e pode **retornar JSON
  no stdout** pra influenciar o fluxo.

### Bloqueando uma ação (`PreToolUse`)
- **Exit code `2`** no `PreToolUse` **bloqueia** a chamada da ferramenta e devolve a saída
  de erro ao Claude (que então tenta outra coisa).
- Outros exit codes ≠ 0 sinalizam erro sem necessariamente bloquear da mesma forma.

## Exemplo (bloquear `rm -rf` perigoso)

`.claude/hooks/block-dangerous.sh`:
```bash
#!/usr/bin/env bash
# Recebe JSON do PreToolUse no stdin; bloqueia rm -rf perigoso.
input=$(cat)
cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // ""')
if printf '%s' "$cmd" | grep -Eq 'rm\s+-rf?\s+(/|~|\*)'; then
  echo "Bloqueado: comando rm perigoso." >&2
  exit 2   # exit 2 = bloqueia a execução da ferramenta
fi
exit 0
```
Registre no `settings.json` como no formato acima (matcher `Bash`).

> Há uma peça pronta deste hook em `building-blocks/` — ver o catálogo do repositório.

## Pegadinhas ⚠️

- **A config fica no `settings.json`, não em `.claude/hooks/`.** Em `.claude/hooks/` ficam
  só os **scripts**; o registro do evento é JSON nos settings.
- **`exit 2` é o que bloqueia** (no `PreToolUse`). Esquecer isso faz o hook "avisar" mas
  deixar a ação passar.
- **Determinístico = roda sempre.** Um hook lento/quebrado atrapalha toda sessão; deixe-os
  rápidos e idempotentes, e teste o script isolado.
- **Segurança nos dois sentidos.** Hooks rodam comandos na sua máquina; ao instalar
  plugins de terceiros, **leia os hooks** que eles trazem antes de habilitar.
- **`${CLAUDE_PROJECT_DIR}`** ajuda a referenciar scripts de forma portável (em vez de
  caminho absoluto).

## Referências oficiais

- Hooks (guia + referência de eventos): https://code.claude.com/docs/en/hooks
- Settings (onde os hooks vivem): https://code.claude.com/docs/en/settings
- (relacionado) Anatomia do projeto: `reference/anatomia-projeto-claude.md`
</content>
