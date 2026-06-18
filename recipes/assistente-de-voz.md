# 🎙️ Receita: Assistente de voz autônomo (estilo "Jarvis")

> Como montar um assistente com **conversa fluida por voz** + **muita autonomia**
> (pede por voz → ele faz: cria vídeo, salva no Drive, manda email, builda site…),
> usando **Claude como cérebro**.
>
> ⚠️ Esta recipe é um **mapa de arquitetura**, não um copia-e-cola. Nomes de SDK,
> endpoints e preços de plataformas de voz **mudam** — confirme na doc oficial de cada
> peça antes de depender de detalhes. Última revisão: 2026-06-18.

---

## 🎯 Objetivo

Um agente que você **fala** (não digita), que responde **na hora**, deixa você
**interromper**, e que **executa tarefas de verdade** no seu lugar — inclusive tarefas
longas (gerar um vídeo, criar e publicar um site) — entregando o resultado por email/Drive
e te avisando quando terminar.

---

## 💡 A grande sacada (leia isto antes de tudo)

Você está juntando **duas coisas que rodam em escalas de tempo MUITO diferentes**:

| | Latência | Exemplo |
|---|---|---|
| **Conversa por voz** | milissegundos | "que horas é minha próxima reunião?" |
| **Tarefa autônoma pesada** | minutos a horas | "faz um vídeo sobre X e manda no meu email" |

❌ **Não dá** pra fazer os dois no mesmo loop: se o agente de voz "travar" 20 minutos
gerando um vídeo, a conversa morre.

✅ **Solução — separar em duas camadas:**

```
        VOCÊ (fala)
           │
           ▼
┌─────────────────────────┐
│  CAMADA DE VOZ (rápida)  │  ← ElevenLabs Agents / Vapi / LiveKit
│  ouve, fala, interrompe  │     cérebro = Claude (Messages API)
│  responde o que é rápido │
└───────────┬─────────────┘
            │  tarefa pesada? → DESPACHA e responde "ok, vou fazer e te aviso"
            ▼
┌─────────────────────────┐
│ CAMADA TRABALHADORA      │  ← Claude Agent SDK  ou  Claude Managed Agents
│ (lenta, autônoma)        │     roda em background, multi-passos, ferramentas
│ faz vídeo / site / etc.  │
└───────────┬─────────────┘
            │  terminou → salva no Drive, manda email, te notifica (push/voz)
            ▼
        VOCÊ (recebe)
```

A camada de voz é o **recepcionista** (rápido, sempre disponível). A camada trabalhadora
são os **funcionários** (fazem o trabalho duro e avisam quando acaba). É o padrão
**fire-and-forget / job assíncrono**.

---

## 🧩 Componentes

| Papel | Opção mais fácil (hospedada) | No repo |
|---|---|---|
| **Voz** (STT+TTS+turn-taking+barge-in) | **ElevenLabs Agents** ou **Vapi** (plug-and-play); LiveKit/Pipecat (mais controle) | — |
| **Cérebro da conversa** | **Claude Messages API** (`claude-sonnet-4-6` p/ rapidez; `opus` p/ raciocínio) | `docs/13`, `reference/modelos-claude.md` |
| **Camada trabalhadora** | **Claude Managed Agents** (hospedado, longa duração, memória, cron, cofre de credenciais) ou **Agent SDK** | `docs/13` |
| **Ferramentas / acesso ao mundo** | **MCP** (Gmail, Google Calendar, Drive já existem) | `docs/08` |
| **Delegação de subtarefas** | **subagents** | `docs/05` |
| **Gerar vídeo/imagem/áudio** | **habilidades de mídia** (Adobe/Canva já conectados) ou API de vídeo | `docs/14` |
| **Buildar/publicar site** | o próprio **Claude Code** (gera código + deploy Vercel) | `docs/01`, `recipes/construir-app-com-claude-code.md` |
| **Autonomia "até terminar"** | `/goal` + `/loop` (ou "Outcomes" no Managed Agents) | `reference/loops-e-goals.md` |
| **Memória (lembrar de você)** | memória persistente do Managed Agents | `docs/13` |

---

## 🗣️ Qual plataforma para português (BR)? (pesquisa 2026-06)

**Recomendação: comece pelo ElevenLabs Agents.** Motivos, conferidos na doc/blog oficial:

- ✅ **Aceita o Claude como cérebro nativamente** — Claude Sonnet 4.x e Haiku estão na
  lista de LLMs do ElevenLabs Agents (e dá pra apontar um *Custom LLM URL* também). Ou
  seja: **um fornecedor só** já faz voz + agente + Claude pensando.
- ✅ **Melhor voz em PT-BR** — vozes brasileiras prontas (Keren, Roberta, Diego, Lax…) e
  o modelo **Flash v2.5 com ~75ms de latência**, feito pra conversa em tempo real.
- ✅ **Mais fácil de começar** — tem widget web/telefone pronto; existe até guia oficial
  "voice agent com Claude + ElevenLabs em ~15 min".

**Alternativas (pra depois, se precisar):**
- **Vapi** — camada de orquestração multi-fornecedor: usa **Claude** como LLM + voz do
  **ElevenLabs** por baixo. Escolha quando quiser trocar peças/escalar telefonia. ~536ms.
- **LiveKit / Pipecat** — frameworks "dev-first" (você monta STT+LLM+TTS). Mais controle,
  mais trabalho. Bom pra rodar local (Fase "Local no meu PC").

> Regra de ouro de latência: acima de ~500ms a conversa "parece quebrada". ElevenLabs
> (Flash) fica bem abaixo disso. Fontes: ver "Referências" no fim.

## 🪜 Passo a passo (em 3 fases)

> Faça em fases. Cada fase **funciona sozinha** e já é útil — não tente a autonomia
> total no dia 1.

### Fase 1 — Conversa fluida (uma tarde) ✅ — passo a passo (ElevenLabs Agents)

> Meta da fase: você **fala** e o Claude **responde por voz**, em PT-BR, fluido. Sem
> integrações ainda. Tudo pela interface web do ElevenLabs (não precisa codar).

1. **Conta:** crie em `elevenlabs.io`. No menu, abra **Agents** (Conversational AI) →
   **Create agent** (pode partir de um template em branco).
2. **Idioma:** em *Language*, selecione **Portuguese (Brazil)**.
3. **Voz:** em *Voice*, escolha uma voz **BR** (ex.: **Keren** ou **Roberta**) e o modelo
   de fala **Flash v2.5** (menor latência). Ouça o preview até gostar.
4. **Cérebro (LLM):** em *LLM*, selecione **Claude** (Sonnet 4.x para rapidez na conversa).
   - Se a versão que você quer não estiver na lista, use **Custom LLM URL** apontando para
     a Claude API e cole sua `ANTHROPIC_API_KEY` no campo de credencial.
5. **System prompt:** defina a persona (exemplo pronto abaixo).
6. **Primeira fala (greeting):** algo como *"Oi Gustavo, sou seu assistente. No que ajudo?"*
7. **Testar:** clique em **Talk to agent** (widget web) e converse. Ajuste voz/latência/
   prompt até a conversa ficar natural.
8. **(opcional) Levar pro dia a dia:** incorpore o **widget** num site/página sua, ou ligue
   o agente a um **número de telefone** pelas opções de *Phone* da plataforma.

**Exemplo de system prompt (cole e ajuste):**
```
Você é o assistente pessoal do Gustavo. Fala português do Brasil, de forma natural,
direta e calorosa — como um amigo competente, não como um robô formal.

Regras de conversa por voz:
- Respostas CURTAS e faladas (1–3 frases). Nada de listas longas ou markdown.
- Se a pergunta for ambígua, pergunte de volta em vez de chutar.
- Se você não souber ou não tiver a ferramenta, diga isso com honestidade.
- Pode ser interrompido a qualquer momento; quando isso acontecer, pare e ouça.

Por enquanto você só conversa (sem acesso a email/agenda/arquivos). Se pedirem uma ação
que você ainda não consegue fazer, explique que essa função será ativada em breve.
```

> ✅ **Fim da Fase 1:** você já tem um "Jarvis" que conversa por voz em PT-BR com o
> cérebro do Claude. As Fases 2 e 3 (ações e autonomia) entram depois, por cima disto.

**Pegadinhas da Fase 1:**
- **Custo é por minuto/créditos** de conversa — comece no plano free/baixo pra testar.
- Se a voz soar "lida demais", troque a voz ou baixe a expressividade; se travar, é
  latência de rede/modelo — teste o **Flash v2.5** e um LLM rápido (Sonnet/Haiku).
- Mantenha o prompt pedindo **respostas curtas** — resposta longa em voz cansa e atrasa.

### Fase 2 — Ações rápidas: email + agenda + briefing 🔌 — passo a passo

> Meta da fase: o agente da Fase 1 passa a **ler sua agenda e seus emails** e **agir**
> (criar evento, rascunhar/responder email) — tudo por voz, em segundos. E te dá um
> **briefing diário**.
>
> ✅ Boa notícia: o **ElevenLabs Agents tem MCP nativo** (Tools → MCP), então dá pra
> plugar Gmail e Google Calendar sem montar servidor próprio. (A própria ElevenLabs usa
> isso no produto deles, o **11ai**.)

**5. Conecte as ferramentas (MCP) — comece em modo LEITURA.**
   No seu agente: **Tools → Add MCP server**. Conecte:
   - **Google Calendar** (ler eventos; depois, criar).
   - **Gmail** (ler/resumir; depois, rascunhar/enviar).
   - Caminhos possíveis (escolha um):
     - MCP "pronto" via **Composio/Zapier/SureTriggers** (mais rápido de plugar), ou
     - um **MCP de Gmail/Calendar** próprio (mais controle — ver `docs/08-mcp.md`).
   - Na **autorização**, dê **escopo mínimo** e, no começo, **somente leitura**.

**6. Descreva bem cada ferramenta.** O agente decide quando chamar pela *descrição*.
   Ex.: `proxima_reuniao` → "retorna o próximo evento da agenda de hoje"; `resumir_emails`
   → "resume os N emails não lidos mais recentes". Descrição ruim = ele não usa na hora.

**7. Ponha freio nas ações que mudam o mundo.** Ler é livre; **criar evento, enviar/
   responder email → o agente CONFIRMA por voz antes** ("quer que eu envie?"). Configure
   isso no system prompt e, se a plataforma permitir, exija confirmação na própria tool.

**8. Teste por voz:**
   - *"Qual minha próxima reunião?"* → lê do Calendar.
   - *"Tenho email importante hoje?"* → resume do Gmail.
   - *"Marca dentista quinta às 15h."* → ele confirma e cria o evento.

**9. Briefing diário (cron):** crie um **gatilho agendado** (no SureTriggers/Make/n8n,
   ou no Managed Agents da Fase 3) que toda manhã junta **agenda + emails não lidos +
   tarefas** e te entrega — por **email**, ou fazendo o agente **te ligar** e falar o
   resumo. Mantenha curto: "3 compromissos, 2 emails que pedem ação, 1 prazo hoje".

**Acréscimo ao system prompt (cole junto ao da Fase 1):**
```
Agora você tem ferramentas: ler agenda (Google Calendar) e ler/resumir email (Gmail).
- Para CONSULTAS (ler agenda, resumir emails), use a ferramenta direto e responda curto.
- Para AÇÕES que mudam algo (criar evento, enviar/responder email), SEMPRE confirme em
  voz antes de executar ("confirma que envio?") e só faça após o "sim".
- Nunca invente dados de agenda/email: se a ferramenta não retornar, diga que não achou.
```

> ✅ **Fim da Fase 2:** assistente de voz que **consulta e age** na sua agenda e email,
> com confirmação pro que é irreversível, + briefing diário automático.

**Pegadinhas da Fase 2:**
- **Permissão é tudo.** Comece read-only; só libere "enviar/criar" depois de confiar.
- **OAuth/escopos do Google** podem dar trabalho na 1ª vez — siga o conector escolhido.
- **Confirmação verbal** evita o pesadelo de mandar email errado "na sua voz".
- **Tarefas rápidas só.** Se a ação for longa (montar um relatório, gerar vídeo), isso é
  Fase 3 (background) — não trave a conversa.

### Fase 3 — Autonomia pesada (o "Jarvis" de verdade) 🤖
8. Cria a **camada trabalhadora** com **Managed Agents** (recomendado p/ rodar 24/7 sem
   você gerir servidor) ou **Agent SDK** no seu PC.
9. Dá ao agente de voz **uma ferramenta nova: `despachar_tarefa(descrição)`**. Quando
   você pede algo pesado, ele NÃO faz na conversa — ele chama essa ferramenta, responde
   *"beleza, tô fazendo, te aviso quando terminar"*, e o trabalho vai pra fila.
10. A camada trabalhadora pega a tarefa e executa com **autonomia** (`/goal`: "vídeo
    gerado E salvo no Drive E email enviado"), usando as ferramentas:
    - **vídeo** → habilidades de mídia (`docs/14`) ou API de vídeo;
    - **site** → Claude Code gera o código e dá deploy (Vercel);
    - **entrega** → salva no Drive + manda email (MCP).
11. Ao terminar, ela **te notifica** (email/push, ou faz a plataforma de voz te ligar).

---

## 🔐 Segurança e guardrails (NÃO pule — autonomia é faca de dois gumes)

Um agente que manda email "como você", mexe no seu Drive, gasta API e publica sites
**precisa de freios**:

- **Confirmação para o irreversível.** Mandar email externo, apagar arquivo, gastar
  dinheiro, publicar algo → o agente deve **confirmar com você por voz** antes. Ações
  reversíveis/internas podem ser automáticas.
- **Credenciais com escopo mínimo.** Token só de Calendar/Gmail/Drive que precisa, nunca
  a chave-mestra. Use o **cofre de credenciais** do Managed Agents; nunca chave no código.
- **Limite de gasto.** Defina teto de tokens/$ por dia. Tarefa autônoma + paralelismo
  **queima dinheiro rápido** (ver pegadinhas em `reference/loops-e-goals.md`).
- **Sandbox.** A camada trabalhadora roda em ambiente isolado, não na sua máquina com
  acesso total.
- **Log de tudo.** Toda ação autônoma registrada, pra você auditar o que ele fez.
- ⚠️ **Lembrete pessoal:** você já teve **API keys vazadas em prints** (Anthropic,
  Supabase, GitHub, Telegram). Antes de dar autonomia a um agente, **rotacione essas
  chaves** e guarde tudo em variável de ambiente/cofre.

---

## 💸 Custo (ordem de grandeza, confirme atual)

- **Voz**: plataformas cobram por **minuto de conversa** (STT+TTS).
- **Cérebro**: tokens da Claude API por mensagem.
- **Trabalhadora**: tokens por tarefa — tarefas longas/multi-passos custam mais.
- Comece com **um** agente e limites baixos; escale depois de medir.

---

## ⚠️ Pegadinhas

- **Não unifique as duas escalas de tempo.** É o erro nº1 — voz trava enquanto faz tarefa
  longa. Sempre despache o pesado pra background.
- **Fluidez é da plataforma de voz, não do Claude.** Se a conversa está travada, o
  gargalo é STT/TTS/turn-taking — ajuste lá, não no prompt.
- **Latência do cérebro importa.** Pra conversa, prefira um modelo rápido (Sonnet/Haiku);
  deixe o Opus pras tarefas pesadas em background.
- **Autonomia precisa de alvo conferível.** Sem `/goal` com critério externo, o agente
  "acha" que terminou cedo demais (ver `reference/loops-e-goals.md`).
- **"Faça um vídeo" é vago.** Quanto mais autônomo, mais o system prompt precisa de
  regras claras de qualidade/entrega, senão vem qualquer coisa.

---

## 🔗 Peças desta recipe no repo

- Camadas (Code/SDK/API/Managed Agents): [`docs/13-sdk-e-api.md`](../docs/13-sdk-e-api.md)
- Autonomia (`/loop`, `/goal`): [`reference/loops-e-goals.md`](../reference/loops-e-goals.md)
- Conectar serviços (MCP): [`docs/08-mcp.md`](../docs/08-mcp.md)
- Delegar (subagents): [`docs/05-subagents.md`](../docs/05-subagents.md)
- Gerar mídia (vídeo/imagem/áudio): [`docs/14-habilidades-de-midia.md`](../docs/14-habilidades-de-midia.md)
- Buildar app/site: [`recipes/construir-app-com-claude-code.md`](./construir-app-com-claude-code.md)
- Modelos (qual usar): [`reference/modelos-claude.md`](../reference/modelos-claude.md)

## 📚 Referências oficiais (confirme antes de depender)

- Claude API / Agent SDK: https://docs.claude.com
- Claude Managed Agents (beta): https://platform.claude.com
- Plataformas de voz: ElevenLabs Agents (`elevenlabs.io`), Vapi (`vapi.ai`),
  LiveKit Agents (`livekit.io`), Pipecat (`pipecat.ai`) — comparar latência/preço/idioma PT-BR.
- ElevenLabs — LLMs suportados (Claude): https://elevenlabs.io/docs/eleven-agents/customization/llm
- ElevenLabs — Claude na Conversational AI: https://elevenlabs.io/blog/introducing-claude-37-sonnet-in-elevenlabs-conversational-ai
- ElevenLabs — vozes em português: https://elevenlabs.io/text-to-speech/portuguese
- Guia "voice agent com Claude + ElevenLabs em ~15 min": https://www.mindstudio.ai/blog/build-voice-agent-claude-code-elevenlabs
- ElevenLabs — MCP em Agents (Tools): https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp
- ElevenLabs — 11ai (assistente de voz que age via MCP): https://elevenlabs.io/blog/introducing-11ai
- ElevenLabs — integrar voz com Google Calendar: https://elevenlabs.io/blog/integrating-ai-voice-tools-with-google-calendar
- Comparativos 2026 (Vapi vs ElevenLabs vs LiveKit): https://softcery.com/lab/choosing-the-right-voice-agent-platform-in-2026 ·
  https://www.retellai.com/blog/vapi-vs-elevenlabs
</content>
</invoke>
