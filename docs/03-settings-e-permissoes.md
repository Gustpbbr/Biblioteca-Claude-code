# 03 — Settings e permissões

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Refs: `code.claude.com/docs/en/settings`, `/permissions`.

## O que é

O comportamento do Claude Code é configurado por arquivos **`settings.json`** em vários
níveis (usuário, projeto, pessoal-do-projeto, gerenciado). Entre outras coisas, eles
definem **permissões** (o que o Claude pode/precisa pedir/não pode fazer), modelo padrão,
hooks, variáveis de ambiente e modo de permissão padrão.

## Quando usar

| Quer… | Onde |
|---|---|
| Padrão do time (versionado no git) | `.claude/settings.json` |
| Override só seu, neste repo | `.claude/settings.local.json` (→ `.gitignore`) |
| Preferência sua em todos os projetos | `~/.claude/settings.json` |
| Política imposta por IT/segurança | managed settings (não sobrescrevível) |

## Como configurar / usar

### Precedência (maior → menor)
1. **Managed/MDM** (`managed-settings.json`) — imposto
2. **Argumentos de CLI** (`--model`, `--permission-mode`, …)
3. **`.claude/settings.local.json`** (pessoal do repo)
4. **`.claude/settings.json`** (time)
5. **`~/.claude/settings.json`** (usuário)

### Permissões: `allow` / `ask` / `deny`
Regras por ferramenta (e padrão de argumento). `deny` vence; `ask` força confirmação;
`allow` libera sem perguntar.
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run test:*)",
      "Read(./src/**)"
    ],
    "ask": [
      "Bash(git push:*)"
    ],
    "deny": [
      "Read(./.env)",
      "Bash(rm -rf:*)"
    ]
  },
  "defaultMode": "default"
}
```
- A sintaxe `Tool(padrão)` casa ferramenta + argumento (ex.: `Bash(git commit:*)`).
- `deny` em `Read(./.env)` é uma boa prática pra **proteger segredos** do contexto.

### Outras chaves comuns
- `model` — modelo padrão.
- `defaultMode` — modo de permissão inicial (`default`, `acceptEdits`, `plan`, …).
- `hooks` — registro de hooks (ver `docs/06`).
- `statusLine` — script da status line (ver `docs/10`).
- `env` — variáveis de ambiente da sessão.

## Exemplo (settings de projeto + local)

`.claude/settings.json` (versionado):
```json
{
  "permissions": {
    "allow": ["Bash(npm run lint:*)", "Bash(npm run test:*)"],
    "deny": ["Read(./.env*)", "Read(./secrets/**)"]
  }
}
```
`.claude/settings.local.json` (no `.gitignore`):
```json
{ "model": "claude-opus-4-8", "permissions": { "allow": ["Bash(gh:*)"] } }
```

## Pegadinhas ⚠️

- **`settings.local.json` deve ir no `.gitignore`.** É o lugar dos seus overrides pessoais.
- **`deny` é absoluto** e vence `allow`/`ask`. Use pra blindar `.env`, `secrets/`, etc.
- **Managed settings não dá pra sobrescrever** — se algo "não obedece", pode ser política.
- **Permissão ≠ hook.** Permissões dizem "pode/pergunta/não pode"; hooks executam código
  determinístico (e podem bloquear via `exit 2`). Pra regra que precisa de lógica, use hook.
- **Não há `settings.global.json`.** Os caminhos são fixos (os 5 níveis acima).

## Referências oficiais

- Settings: https://code.claude.com/docs/en/settings
- Permissões: https://code.claude.com/docs/en/permissions
- (relacionado) Anatomia: `reference/anatomia-projeto-claude.md` · Hooks: `docs/06`
</content>
