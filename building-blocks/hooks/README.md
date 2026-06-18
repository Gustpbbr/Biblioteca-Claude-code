# Hooks — peças prontas

Hooks reutilizáveis (scripts + trechos de `settings.json`) para automações como
lint, testes, formatação e guard-rails.

## Disponíveis

- [`bloquear-comandos-perigosos/`](./bloquear-comandos-perigosos/) — hook
  PreToolUse que bloqueia comandos Bash destrutivos (`rm -rf /`, fork bomb, etc.).
  Inclui script + snippet de settings. ✅ Testado.

> Cada hook traz o trecho de configuração e o script associado, com README de
> instalação.
