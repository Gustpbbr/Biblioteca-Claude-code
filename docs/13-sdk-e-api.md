# 13 — SDK de agentes e API Claude

> 🚧 **Stub** — a preencher. Tópicos previstos: Claude Agent SDK (construir
> agentes próprios), API Claude/Anthropic (modelos, tool use, streaming,
> caching), relação entre Claude Code, SDK e API.

## Claude Managed Agents (public beta) ✅ verificado

Lançado pela Anthropic em **public beta (~8–9/abr/2026)**. É um **harness gerenciado**
que empacota "agent loop + execução de tools + sandbox + persistência de estado"
em APIs REST — você define tarefas, ferramentas e limites, e a Anthropic cuida da
infraestrutura (escala, segurança, uptime), sem você construir o próprio runtime.
- Endpoints: `/v1/agents`, `/v1/environments`, `/v1/sessions`.
- Primeiros adotantes: Notion, Asana, Sentry.
- Evolução: **memória persistente** (23/abr, memórias como arquivos exportáveis/editáveis
  via API ou Console) e **cron schedules + cofre de credenciais** (9/jun).
- Relação: é o "irmão hospedado" do Agent SDK — em vez de rodar o loop você mesmo,
  a Anthropic roda. Bom para agentes autônomos de longa duração em produção.
- Fontes: https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/ ·
  https://www.techtimes.com/articles/318163/20260610/claude-managed-agents-add-cron-schedules-credential-vaultsanthropic-beta-puts-agents-autopilot.htm
  _(⚠️ confirmar detalhes finais na doc oficial platform.claude.com antes de publicar como definitivo)_

## O que é
_A preencher._

## Quando usar
_A preencher._

## Como configurar / usar
_A preencher._

## Exemplo
_A preencher._

## Pegadinhas
_A preencher._

## Referências oficiais
_A preencher._
