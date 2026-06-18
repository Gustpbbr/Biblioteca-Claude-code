# 🔁 Loops e Goals — tarefas autônomas e de longa duração

> Verificado em 2026-06-18 contra a doc oficial e relatos da equipe do Claude Code
> (Boris Cherny / Cat Wu). `/loop` está na doc oficial (`scheduled-tasks`); `/goal`
> foi introduzido na **v2.1.139+**. Sempre confira a doc atual antes de depender de detalhes.

## O que é

Dois comandos que deixam o Claude Code **trabalhar sozinho até terminar**, em vez de
você ficar dando prompt e aprovando passo a passo:

- **`/loop`** — repete um prompt/slash-command de tempos em tempos (ou no ritmo que o
  próprio Claude define). Bom para **vigiar** algo ou **iterar** uma tarefa.
- **`/goal`** — define uma **condição de conclusão verificável** e mantém o Claude
  planejando → escrevendo → testando → revisando **até a condição ser satisfeita**.

A ideia central (resumida pelo Boris Cherny, criador do Claude Code):
> *"Eu não dou mais prompt pro Claude. Tenho loops rodando que dão o prompt e
> descobrem o que fazer. Meu trabalho é escrever os loops."*

A evolução do workflow dele: escrever código na mão → rodar 5–10 sessões do Claude em
paralelo dando prompt em cada → **construir loops automáticos** que entregam a tarefa,
deixam o Claude agir, **conferem o resultado** e decidem o próximo passo. O dev sai da
execução e vira o **arquiteto da máquina que faz a tarefa**.

## Quando usar

| Situação | Use |
|---|---|
| Vigiar algo que não pode cair (ex.: site no ar, fila de deploy) | `/loop 5m ...` (intervalo fixo) |
| Iterar até bater um alvo, sem saber quanto tempo leva | `/loop` sem intervalo (self-pacing) ou `/goal` |
| Ter um **critério objetivo de "pronto"** (testes passam, build compila, 0 erro de TS) | `/goal` |
| Tarefas que terminam com o laptop fechado (resumos, revisão a cada commit, migração testada passo a passo) | `/goal` + `/loop` |

Não use para tarefas curtas e interativas — o overhead (e o custo) não compensa.

## Como configurar / usar

### `/loop`
- **Intervalo fixo:** `/loop <n><unidade> <prompt>` — unidade é `m` (min), `h` (hora),
  `d` (dia). Mínimo **1 minuto** (é cron por baixo; `30s` arredonda pra 1 min).
  ```
  /loop 10m rode os testes e me avise se algum quebrar
  /loop 1h verifique se o site de produção responde 200
  ```
- **Self-pacing (sem intervalo):** omita o tempo e o Claude escolhe o ritmo, armando
  *monitores de evento* como sinal primário de "acordar" e usando heartbeats de fallback.
  ```
  /loop continue refinando o design até bater a referência que enviei
  ```

### `/goal`
- Defina um **estado final mensurável**. Um **modelo avaliador (grader) separado e menor**
  confere, **a cada turno**, se o objetivo foi atingido — ou seja, **quem escreve não é
  quem julga** (evita o Claude "achar" que terminou).
  ```
  /goal todos os testes passam e não há nenhum erro de TypeScript
  /goal o app compila e o Lighthouse mobile fica acima de 90
  ```
- Veredito "não atingido" → inicia a próxima volta. Há limite por turnos/tempo na condição.
- Sai automaticamente ao atingir o alvo, ou manualmente com `/goal clear`.
- **`/goal` + `/loop`** = agente que se auto-dirige e se auto-encerra.

> No **Claude Managed Agents** o mesmo padrão aparece como "Outcomes": rubrica com
> critérios graduáveis + sub-agente grader independente + `max_iterations`.

## Exemplo (padrão recomendado)

> Princípio (de um teste da Anthropic): foram **9 critérios** e um **verificador
> separado** só deixou o loop parar quando **todos** passaram.

```
# 1. dê um alvo conferível e externo
/goal todos os testes passam, lint sem erros, e o build de produção conclui

# 2. (opcional) combine com um loop de vigilância em outra sessão
/loop 15m rode a suíte de testes e reporte regressões
```

## Pegadinhas ⚠️

- **Paralelismo queima dinheiro.** Um loop só gasta pouco; **dezenas em paralelo**
  evaporam tokens (relato real: ~5 milhões de tokens em 3 minutos). Pior: loops
  paralelos **não trocam descobertas** entre si e "batem todos na mesma pedra".
  **Comece com um loop só.**
- **O verificador não pode ser o próprio escritor.** Sem um alvo conferível por algo
  externo, o loop "gira em falso" e o Claude declara vitória cedo demais. Por isso o
  `/goal` usa um grader separado.
- **Loops são efêmeros.** Tarefas agendadas ficam **em memória da sessão**: fechar o
  terminal/encerrar a sessão **apaga os loops ativos**. Além disso, tarefas recorrentes
  **expiram 7 dias** após a criação (disparam uma última vez e se removem).
- **Custo/segurança.** Tarefa autônoma + `--dangerously-skip-permissions` é poderoso e
  perigoso. Dê alvos estreitos, prefira ambiente isolado e monitore o gasto.

## Referências oficiais

- Doc oficial — Run prompts on a schedule: https://code.claude.com/docs/en/scheduled-tasks
- Equipe do Claude Code (Boris Cherny & Cat Wu) sobre agent loops:
  https://www.theneuron.ai/explainer-articles/claude-code-creators-boris-cherny-and-cat-wu-explain-how-to-use-agent-loops/
- (Comunidade) Guia do `/loop`: https://betterstack.com/community/guides/ai/claude-code-loop/
- (Comunidade) Comandos autônomos `/goal` `/loop` `/batch`: https://medium.com/@richardhightower/claude-code-the-autonomous-commands-that-finish-work-while-you-sleep-goal-loop-batch-etc-7acb82bf46b1

> Origem da curadoria: carrossel "LOOPS" (@Overlens) + fala do Boris Cherny, capturados
> nos prints do usuário e verificados contra as fontes acima.
