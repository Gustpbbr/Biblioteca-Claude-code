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

## 🪜 Passo a passo (em 3 fases)

> Faça em fases. Cada fase **funciona sozinha** e já é útil — não tente a autonomia
> total no dia 1.

### Fase 1 — Conversa fluida (uma tarde) ✅
1. Cria uma conta numa plataforma de voz (comece por **ElevenLabs Agents** ou **Vapi**).
2. Cria um "agent" lá e escolhe **Claude** como modelo (LLM), com sua `ANTHROPIC_API_KEY`.
3. Escreve o **system prompt** (quem ele é, tom, que ele é seu assistente pessoal).
4. Testa pelo telefone/web. **Pronto: você já conversa por voz, fluido.**

### Fase 2 — Ações rápidas (ler/responder) 🔌
5. Conecta **MCP** de leitura: Google Calendar e Gmail (ver `docs/08`).
6. Dá ao agente de voz as **ferramentas rápidas**: "ler próxima reunião", "resumir
   últimos emails", "criar evento". São respostas de segundos → cabem na conversa.
7. Monta o **briefing diário**: um `/loop` (ou cron do Managed Agents) que toda manhã
   junta agenda + emails + tarefas e te manda (email ou te liga).

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
</content>
</invoke>
