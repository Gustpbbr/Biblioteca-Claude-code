# ⚡ Gestão de contexto e tokens no Claude Code

Como não estourar o limite de contexto e manter a performance alta em sessões longas.

> **Origem:** carrossel @brandsdecoded_ (base: vídeo "How to Never Hit Your Claude
> Session Limit Again", do Nate Herk) + alinhamento com a orientação oficial de
> *context engineering* da Anthropic. Itens marcados com 🔎 dependem de confirmação
> na documentação oficial.

## Por que o contexto importa

- **Custo composto:** a cada mensagem, o modelo relê o histórico. As últimas
  mensagens custam muito mais que as primeiras (o histórico inteiro é reprocessado).
- **Context rot:** conforme a janela enche, a precisão de recuperação cai (a fonte
  cita ~92% → ~78% ao ir de ~256k para ~1M tokens). **Mais contexto ≠ melhor** —
  isso bate com a ressalva oficial da Anthropic sobre janelas grandes.

## As táticas

| # | Tática | Como |
|---|--------|------|
| 1 | **Compactação manual** | Ao chegar ~60% da janela, peça "resumo completo do que fizemos + status", dê `/clear`, cole o resumo e continue. Não espere o auto-compact (~95%, que mantém só 20–30% do detalhe). |
| 2 | **`/clear` entre tarefas** | Limpe o contexto ao trocar de assunto. |
| 3 | **Rewind** 🔎 | Volte e descarte tentativas erradas (checkpoints/`/rewind`; o carrossel chama de `/re`). |
| 4 | **Sub-agentes** | Delegue pesquisa/processamento a subagents (janela separada), em modelo mais barato (ex.: Haiku). Eles devolvem só o essencial. |
| 5 | **Converter para Markdown** | Antes de enviar arquivos: HTML→md ~90% menos tokens; PDF→md ~65–70%; DOCX→md ~33%. |
| 6 | **Plan mode** | Comece em plan mode (Shift+Tab). Boris Cherny (criador do Claude Code) começa toda sessão assim — planejar antes sai mais barato que corrigir depois. |
| 7 | **CLAUDE.md enxuto** | Mantenha < ~200 linhas (~2k tokens). Ele carrega em toda sessão; detalhes específicos vão em arquivos que só carregam quando necessário. |
| 8 | **Encadear sessões** | Divida em etapas (descoberta → planejamento → execução), cada uma com contexto limpo e tarefa especializada. |
| 9 | **`/btw`** 🔎 | Perguntas rápidas fora do histórico principal (citado na fonte; confirmar se existe na sua versão). |

## Comandos úteis (confirmar versão)

- `/clear` — limpa o contexto da sessão.
- `/compact` — condensa a sessão atual.
- `/rewind` (ou Esc-Esc) — volta a um checkpoint (código + conversa).
- `/context` — mostra o uso atual de contexto.
- `/goal` — define critério de conclusão para tarefas longas.

> Veja também: `claude-md-boas-praticas.md` e o doc `docs/01-cli-e-modos.md`.
