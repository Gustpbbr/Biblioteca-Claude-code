# 🧠 Modelos Claude — referência rápida

> Atualizado em 2026-06-18. **IDs e capacidades mudam; preços e limites mudam mais ainda.**
> Esta tabela cobre só **identificação e quando usar** — para **preço, limites de taxa,
> janela exata e benchmarks**, consulte **sempre** a doc oficial (não confie em números de
> redes sociais nem de memória).

## Família atual (2026)

| Modelo | ID da API | Posição | Quando usar |
|---|---|---|---|
| **Opus 4.8** | `claude-opus-4-8` | Mais capaz (raciocínio/código difícil) | Tarefas complexas, arquitetura, problemas que exigem profundidade |
| **Sonnet 4.6** | `claude-sonnet-4-6` | Equilíbrio capacidade/custo | Dia a dia de código; **é o padrão do Claude Code** |
| **Haiku 4.5** | `claude-haiku-4-5` | Rápido/barato | Subtarefas, classificação, grading de loops, alto volume |
| **Fable 5** | `claude-fable-5` | Classe Mythos (acima de Opus em capacidade) | Casos de ponta; ⚠️ acesso/limitações específicos — ver doc oficial |

> Observações verificadas nesta sessão:
> - O **Claude Code usa Sonnet como modelo padrão**.
> - **Fable 5** e **Mythos 5** compartilham o mesmo modelo-base; Fable é o "geralmente
>   disponível" com medidas de segurança extras p/ capacidades dual-use.

## Como escolher (regra prática)

- **Comece no Sonnet.** Cobre a maioria do trabalho de código com bom custo.
- **Suba pro Opus** quando a tarefa for difícil de verdade (raciocínio longo, refactor
  arquitetural, bug sutil).
- **Desça pro Haiku** em subtarefas baratas e de alto volume — inclusive como **grader**
  em loops `/goal` (ver `reference/loops-e-goals.md`).
- **Trocar na sessão:** `/model` (ou `--model <id>` ao iniciar; ver `docs/01`).

## Onde isso aparece na biblioteca

- Selecionar modelo de subagent: `docs/05-subagents.md` (frontmatter `model:`).
- Modelo padrão por projeto: `docs/03-settings-e-permissoes.md` (chave `model`).
- API/SDK: `docs/13-sdk-e-api.md`.

## ⚠️ Pegadinha

- **Não copie preços/benchmarks de carrosséis.** Os números que circularam (ex.: tabelas
  com "Opus 4.7 / SWE-bench / $X") envelhecem rápido e podem se referir a versões
  anteriores. Para valores atuais, **só a doc/console oficial**.

## Referências oficiais

- Modelos & visão geral: https://docs.claude.com/en/docs/about-claude/models
- Preços: https://www.anthropic.com/pricing
- Console/plataforma: https://platform.claude.com
</content>
