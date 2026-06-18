# 🧰 Tool de despacho — assistente de voz (Fase 3)

Esqueleto da **tool de despacho** que separa a *conversa de voz* (rápida) do *trabalho
pesado* (lento, em background). Faz par com a recipe
[`recipes/assistente-de-voz.md`](../../recipes/assistente-de-voz.md) (Fase 3).

## O que faz
- `POST /tarefas` — o agente de voz chama, recebe um `job_id` **na hora** e responde
  *"tô fazendo, te aviso"*. Não espera o trabalho terminar.
- `GET /tarefas/{job_id}` — status do job ("como tá meu vídeo?").
- Roda o trabalho pesado em background, onde você **pluga o agente real**
  (Claude Managed Agents ou Agent SDK + ferramentas de vídeo/site/Drive/Gmail).

## Como rodar
```bash
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
# exponha publicamente (ex.: ngrok http 8000) e aponte a tool `criar_tarefa`
# do agente de voz (ElevenLabs/Vapi) para  https://SEU-HOST/tarefas  (POST)
```

Teste rápido:
```bash
curl -X POST localhost:8000/tarefas \
  -H 'content-type: application/json' \
  -d '{"titulo":"Vídeo sobre X","descricao":"faz um vídeo de 30s sobre X","tipo":"video"}'
# -> {"job_id":"ab12cd34", ...}  (depois consulte GET /tarefas/ab12cd34)
```

## Onde plugar o agente real
Em `app.py`, função `executar_tarefa` → bloco `TODO`. Veja `docs/13-sdk-e-api.md`
(Managed Agents vs Agent SDK) e `reference/loops-e-goals.md` (critério de "pronto").

## ⚠️ Antes de produção
- Fila **em memória** → troque por Redis/DB (reinício apaga os jobs).
- **Sem auth** → defina `DISPATCH_TOKEN` no ambiente e mande no header `x-token`.
- **Teto de gasto** por job + **log** de cada ação (ver Segurança na recipe).
- Trate **falha/retry** — o `notificar` já é chamado também no estado `erro`.
