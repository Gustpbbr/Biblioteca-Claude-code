# 01 — CLI e modos de execução

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Refs: `code.claude.com/docs/en/cli`, `/permissions`, `/interactive-mode`.

## O que é

A `claude` é a CLI do Claude Code. Ela roda em **modo interativo** (uma sessão de chat no
terminal) ou em **modo headless/não-interativo** (`-p`, retorna a resposta e sai — bom pra
scripts e CI). Os **modos de permissão** controlam quanto o Claude pode fazer sozinho.

## Quando usar

| Quer… | Use |
|---|---|
| Trabalhar interativamente | `claude` (ou `claude "tarefa inicial"`) |
| Rodar em script/CI, capturar saída | `claude -p "..."` (com `--output-format json`) |
| Planejar antes de mexer em arquivos | **plan mode** (Shift+Tab) |
| Deixar o Claude editar sem perguntar a cada vez | **acceptEdits** (Shift+Tab) |
| Ambiente isolado/descartável, sem prompts | `--dangerously-skip-permissions` (com cuidado) |

## Como configurar / usar

### Invocação
```bash
claude                       # sessão interativa
claude "corrija o teste X"   # interativa com prompt inicial
claude -p "liste os TODOs"   # headless: responde e sai
claude -p "..." --output-format json   # saída estruturada (text | json | stream-json)
```

### Modos de permissão
`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`.
- **Trocar na sessão:** `Shift+Tab` (ou `Alt+M`) cicla os modos.
- **Iniciar num modo:** `--permission-mode <modo>`.
- **Persistir:** chave `defaultMode` no `settings.json`.
- **`--dangerously-skip-permissions`** = iniciar em `bypassPermissions` (não pergunta nada).
  ⚠️ Mesmo assim, **não** pula regras `ask` explícitas nem os "circuit breakers" (ex.:
  `rm -rf /` ou `rm -rf ~`).

### Flags úteis (todas reais)
| Flag | Pra quê |
|---|---|
| `--model <id>` | escolher o modelo |
| `--system-prompt-file <arq>` | substituir o system prompt |
| `--append-system-prompt "..."` | acrescentar ao system prompt |
| `--add-dir <dir>` | dar acesso a outra pasta |
| `--continue` / `-c` | retomar a sessão anterior |
| `--mcp-config <arq>` | carregar config de MCP |
| `--plugin-dir <dir>` | testar um plugin local |
| `-p` / `--print` | modo headless |

### Atalhos do modo interativo
| Atalho | O que faz |
|---|---|
| `Shift+Tab` | cicla os modos de permissão (inclui plan mode) |
| `@` | referenciar arquivo/pasta (autocomplete de caminho) |
| `!` | **shell mode** — roda comando direto, sem o Claude interpretar |
| `/` | abrir menu de comandos/skills |
| `Esc` | interromper o Claude (mantém o que já foi feito) |
| `Esc Esc` | limpar o rascunho / abrir menu de **rewind** (voltar no histórico) |
| `Ctrl+O` | alternar o visualizador de transcript |
| `/memory` | editar o `CLAUDE.md` (memória) |

## Exemplo

```bash
# Plan mode: o Claude analisa e propõe um plano antes de tocar em arquivos
claude        # depois Shift+Tab até "plan"

# Headless em CI, saída JSON pra processar
claude -p "resuma as mudanças do último commit" --output-format json
```

## Pegadinhas ⚠️

- **`#` NÃO adiciona à memória.** Para editar o `CLAUDE.md` use `/memory`. (Erro comum.)
- **`--dangerously-skip-permissions` é perigoso.** Use só em ambiente isolado/descartável;
  ele não te protege de tudo (circuit breakers), mas remove quase todas as barreiras.
- **plan mode é seu amigo** pra tarefas grandes: revisa o plano antes de qualquer edição.
- **`-p` é stateless** por padrão; use `--continue`/`--resume` pra manter contexto.

## Referências oficiais

- CLI: https://code.claude.com/docs/en/cli
- Permissões: https://code.claude.com/docs/en/permissions
- Modo interativo: https://code.claude.com/docs/en/interactive-mode
- (relacionado) Settings: `docs/03` · Loops/Goals: `reference/loops-e-goals.md`
</content>
