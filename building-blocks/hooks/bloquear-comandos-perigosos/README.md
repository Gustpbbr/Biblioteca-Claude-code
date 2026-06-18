# Hook — bloquear comandos perigosos

Hook **PreToolUse** que intercepta chamadas da ferramenta `Bash` e **bloqueia**
comandos potencialmente destrutivos (ex.: `rm -rf /`, fork bomb, `mkfs`, `dd`
em disco) antes de rodarem.

## Arquivos

- `bloquear-comandos-perigosos.sh` — o script do hook (lê o evento JSON via stdin,
  sai com código **2** para bloquear).
- `settings-snippet.json` — trecho para colar no seu `settings.json`.

## Como instalar

1. Copie o script para o seu projeto e dê permissão de execução:
   ```bash
   mkdir -p .claude/hooks
   cp bloquear-comandos-perigosos.sh .claude/hooks/
   chmod +x .claude/hooks/bloquear-comandos-perigosos.sh
   ```
2. Cole o conteúdo de `settings-snippet.json` dentro do seu `.claude/settings.json`
   (mesclando com o que já existir em `hooks`).

## Como funciona

- O Claude Code dispara o hook **antes** de executar qualquer comando `Bash`.
- O script recebe o payload do evento em JSON no stdin e extrai `tool_input.command`.
- Se casar com um padrão perigoso, escreve um aviso no stderr e sai com **código 2**,
  o que faz o Claude Code **bloquear** a execução.
- Saída 0 = libera. Ajuste os padrões conforme a sua necessidade.

> ⚠️ É uma rede de segurança, não uma garantia. Combine com sandboxing e permissões.
