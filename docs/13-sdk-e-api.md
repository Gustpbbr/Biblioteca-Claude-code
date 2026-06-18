# 13 — SDK de agentes e API Claude

> Verificado em 2026-06-18. Detalhes voláteis (IDs de modelo, preços, limites) **mudam** —
> confira sempre a doc oficial (`docs.claude.com` / `platform.claude.com`) e a referência
> rápida em `reference/` antes de depender de números. Há também a skill `claude-api`.

## O que é

Três camadas, da mais "pronta" para a mais "crua":

1. **Claude Code** — a ferramenta (CLI/IDE/web) que você usa direto.
2. **Claude Agent SDK** — bibliotecas (TypeScript e Python) pra **construir seus próprios
   agentes** com o mesmo "motor" do Claude Code: agent loop, execução de tools, MCP,
   subagents, hooks e permissões — embutidos no **seu** app.
3. **Claude API (Messages API)** — a API do modelo por baixo de tudo: você manda mensagens
   e recebe respostas, com tool use, streaming, prompt caching, etc.

E, em paralelo, o **Claude Managed Agents** (hospedado pela Anthropic — ver abaixo).

## Claude Managed Agents (public beta) ✅ verificado

Lançado pela Anthropic em **public beta (~8–9/abr/2026)**. É um **harness gerenciado**
que empacota "agent loop + execução de tools + sandbox + persistência de estado"
em APIs REST — você define tarefas, ferramentas e limites, e a Anthropic cuida da
infraestrutura (escala, segurança, uptime), sem você construir o próprio runtime.
- Endpoints: `/v1/agents`, `/v1/environments`, `/v1/sessions`.
- Primeiros adotantes: Notion, Asana, Sentry.
- Evolução: **memória persistente** (23/abr, memórias como arquivos exportáveis/editáveis
  via API ou Console) e **cron schedules + cofre de credenciais** (9/jun).
- É o "irmão hospedado" do Agent SDK — em vez de rodar o loop você mesmo, a Anthropic roda.
- Fontes: https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/ ·
  https://www.techtimes.com/articles/318163/20260610/claude-managed-agents-add-cron-schedules-credential-vaultsanthropic-beta-puts-agents-autopilot.htm
  _(⚠️ confirmar detalhes finais na doc oficial antes de publicar como definitivo)_

## Quando usar

| Você quer… | Use |
|---|---|
| Codar/automatizar no seu ambiente, interativo | **Claude Code** (CLI) |
| Embutir um agente "estilo Claude Code" no seu produto, controlando o loop | **Agent SDK** |
| Chamar o modelo direto (chat, extração, classificação, tool use) | **Claude API** |
| Agente autônomo de longa duração em produção, sem gerir infra | **Managed Agents** |

## Como configurar / usar

### Agent SDK
- Pacotes: **TypeScript** (`@anthropic-ai/claude-agent-sdk`) e **Python**
  (`claude-agent-sdk`). Confira o nome/import exatos na doc.
- Dá controle programático sobre: prompt do sistema, ferramentas, **MCP servers**,
  **subagents**, **hooks**, **permissões** e o **loop** do agente.
- Use quando quer a experiência do Claude Code, mas **dentro do seu app/serviço**.

### Claude API (Messages)
- Endpoint de mensagens; suporta **tool use** (function calling), **streaming**,
  **prompt caching** (reduz custo/latência reusando prefixo), **conector MCP**,
  **token counting** e **extended thinking**.
- SDKs oficiais em Python e TypeScript (`anthropic`).
- **Modelos** (família atual): `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5`,
  e o `claude-fable-5` (classe Mythos). ⚠️ **IDs/preços/limites mudam** — confirme na doc.
  Lembrete: o **Claude Code usa Sonnet como padrão**.

### Esboço de chamada (ilustrativo — confira a doc)
```python
from anthropic import Anthropic
client = Anthropic()  # usa ANTHROPIC_API_KEY do ambiente
msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Resuma este texto: ..."}],
)
print(msg.content)
```

## Exemplo (qual camada escolher)

- "Quero um bot que revisa PRs no nosso SaaS." → **Agent SDK** (ou Managed Agents se não
  quiser gerir infra).
- "Quero classificar tickets de suporte em lote." → **Claude API** direto.
- "Quero codar no meu repo agora." → **Claude Code** (CLI).

## Pegadinhas ⚠️

- **Não documente preços/limites de cabeça.** Eles mudam; sempre aponte pra doc oficial
  (e para a skill `claude-api`).
- **Use os modelos mais recentes** por padrão (família 4.x / Fable 5) em apps novos.
- **Segurança de chave:** `ANTHROPIC_API_KEY` é segredo — variável de ambiente/secret,
  nunca no código versionado.
- **Agent SDK ≠ API crua:** o SDK traz o loop/tools/permissões prontos; a API é o tijolo.
- **Managed Agents é beta:** confirme disponibilidade e detalhes na doc antes de produção.

## Referências oficiais

- Doc da API / SDKs: https://docs.claude.com
- Plataforma/Console: https://platform.claude.com
- (no repo) Skill de referência de API: `claude-api` · Modelos citados na curadoria:
  `reference/curadoria-conteudo.md`
</content>
