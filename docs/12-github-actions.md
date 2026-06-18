# 12 — GitHub Actions

> Verificado em 2026-06-18 (via agente `claude-code-guide`). A doc detalhada vive no
> repositório oficial da action: `github.com/anthropics/claude-code-action`.

## O que é

A **action oficial `anthropics/claude-code-action`** roda o Claude Code dentro do **GitHub
Actions**: ele responde a **menções `@claude`** em issues e PRs, implementa mudanças, abre
PRs e faz **code review** automático — tudo no CI do seu repositório.

## Quando usar

| Quer… | Use |
|---|---|
| "@claude, implementa isso" direto numa issue/PR | ✅ menção `@claude` |
| Code review automático em PRs | ✅ |
| Autofix de CI / tarefas recorrentes no repo | ✅ (com workflow próprio) |
| Rodar localmente no seu terminal | ❌ use a CLI (`docs/01`) |

## Como configurar / usar

### Setup básico
1. No terminal, rode **`/install-github-app`** — ele guia a instalação do app do GitHub e a
   criação do workflow.
2. Adicione o secret **`ANTHROPIC_API_KEY`** no repositório (Settings → Secrets).
   - Também suporta **Amazon Bedrock**, **Google Vertex AI** e **Foundry** como provedores.
3. Faça commit do workflow (ex.: `.github/workflows/claude.yml`).

### Esqueleto de workflow
```yaml
name: Claude
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
    steps:
      - uses: actions/checkout@v4
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```
> Confira o `README`/exemplos oficiais da action pelos nomes exatos de inputs e eventos —
> eles evoluem (este é um esqueleto ilustrativo).

### Como acionar
- Comente **`@claude faça X`** numa issue ou PR (conforme os eventos do workflow).
- O Claude lê o contexto (issue/PR/diff), age e responde / abre PR.

## Exemplo (casos de uso)

- **Issue → implementação:** "@claude implemente o endpoint descrito acima e abra um PR."
- **PR → revisão:** review automático apontando bugs/riscos no diff.
- **Comentário em PR → ajuste:** "@claude troque a lib X por Y neste PR."

## Pegadinhas ⚠️

- **Segurança de credenciais:** o `ANTHROPIC_API_KEY` é um secret — nunca o coloque no
  YAML em texto puro; use `secrets`. Restrinja `permissions` do job ao mínimo.
- **Conteúdo não confiável:** corpos de issues/PRs/comentários vêm de terceiros. Trate como
  entrada não confiável (não deixe o Claude seguir instruções embutidas que fujam do escopo).
- **Custo/escopo:** workflows que disparam em muitos eventos podem gerar custo; limite os
  `types`/branches e quem pode acionar.
- **A doc canônica está no repo da action**, não em `code.claude.com` — siga o README de lá
  pros nomes de inputs atuais.

## Referências oficiais

- Action oficial: https://github.com/anthropics/claude-code-action
- (relacionado) CLI/headless pra CI: `docs/01` · SDK/API: `docs/13`
</content>
