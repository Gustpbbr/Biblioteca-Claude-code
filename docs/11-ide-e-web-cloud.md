# 11 — IDE e Claude Code na web/cloud

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Refs: `code.claude.com/docs/en/vs-code`, `/claude-code-on-the-web`, `/cli`.

## O que é

Além do terminal, o Claude Code roda em **extensões de IDE** (VS Code, JetBrains) e na
**web/cloud** (`claude.ai/code`), com **sessões em ambiente gerenciado** pela Anthropic.
Há comandos para **mover uma sessão entre web e terminal** (`/teleport`) e **controlar uma
sessão local de outro dispositivo** (`/remote-control`).

## Quando usar

| Situação | Use |
|---|---|
| Trabalhar com diffs e painel gráfico no editor | extensão **VS Code**/**JetBrains** |
| Rodar tarefas em ambiente isolado na nuvem | **Claude Code on the web** |
| Começou na web e quer continuar no terminal local | **`/teleport`** |
| Sessão local rodando e quer acompanhar/controlar do celular | **`/remote-control`** |

## Como configurar / usar

### Extensões de IDE
- **VS Code:** extensão `anthropic.claude-code` — painel gráfico, **diffs lado a lado**,
  `@`-menções de arquivos, `Alt+K`/`Option+K` pra inserir menção com intervalo de linhas,
  histórico de sessão. Compartilha o `.claude/settings.json` com a CLI.
- **JetBrains:** integração equivalente (a doc mais detalhada é a do VS Code).

### Claude Code na web/cloud (`claude.ai/code`)
- Roda em **infra gerenciada da Anthropic** (sandbox). As sessões **persistem** mesmo
  fechando o navegador.
- Acesso pelo **navegador** do celular/tablet (não há app nativo dedicado do Claude Code —
  ver abaixo).
- Política de rede e setup do ambiente são definidos por quem cria o ambiente
  (ver a doc oficial de Claude Code on the web).

### Mover entre web e terminal
- **`/teleport`** (ou `claude --teleport`): **puxa** uma sessão da nuvem pra continuar no
  **terminal local** (cloud → local).
- **`/remote-control`** (ou `claude --remote-control` / `claude remote-control`): deixa uma
  **sessão local acessível remotamente** via claude.ai — a sessão local segue no comando;
  você só a "vê/controla" de outro dispositivo (ex.: celular).

### Mobile
- **Não há app nativo do Claude Code para celular.** O que existe: acesso via **navegador**
  a `claude.ai/code`, o **`/remote-control`** pra controlar uma sessão local, e o **app
  Claude** (mobile) pra acompanhar.

## Exemplo

```bash
# começou uma tarefa na web; agora continua localmente:
claude --teleport      # (ou /teleport dentro de uma sessão)

# expõe sua sessão local pra controlar do celular:
claude --remote-control
```

## Pegadinhas ⚠️

- **`/teleport` ≠ `/remote-control`.** Teleport = trazer a sessão da nuvem pra cá;
  remote-control = abrir uma "janela remota" pra uma sessão local (que continua no comando).
- **Não procure um "app Claude Code" na loja.** Mobile é navegador + remote-control + app
  Claude pra monitorar.
- **Ambiente cloud é efêmero/isolado:** o que não for commitado/enviado se perde quando o
  container é reciclado.
- **Política de rede** na nuvem pode bloquear acessos externos — depende de como o ambiente
  foi configurado.

## Referências oficiais

- VS Code: https://code.claude.com/docs/en/vs-code
- Claude Code na web: https://code.claude.com/docs/en/claude-code-on-the-web
- CLI (flags `--teleport`, `--remote-control`): https://code.claude.com/docs/en/cli
</content>
