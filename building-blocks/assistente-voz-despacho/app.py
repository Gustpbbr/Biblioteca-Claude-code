"""
Tool de despacho — Fase 3 do assistente de voz (ver recipes/assistente-de-voz.md).

O QUE FAZ
  Expõe 2 "tools" HTTP que o agente de voz (ElevenLabs/Vapi) chama:
    POST /tarefas       -> cria um job e responde NA HORA com job_id (NÃO espera o trabalho)
    GET  /tarefas/{id}  -> status do job (pra você perguntar "como tá meu vídeo?")
  O trabalho PESADO roda em background (aqui é um stub) — é onde você pluga o
  Claude Agent SDK ou os Claude Managed Agents + ferramentas (vídeo, Drive, Gmail).

POR QUE EXISTE
  Conversa de voz é em milissegundos; gerar vídeo/site leva minutos. Não dá pra fazer
  os dois no mesmo loop. Este endpoint é o "recepcionista": registra o pedido e libera
  a conversa na hora. O "funcionário" (worker) faz o trabalho e te notifica depois.

COMO RODAR
    pip install -r requirements.txt
    uvicorn app:app --reload --port 8000
    # exponha publicamente (ex.: `ngrok http 8000`) e aponte a tool `criar_tarefa`
    # do seu agente de voz para  https://SEU-HOST/tarefas  (método POST)

⚠️ ESQUELETO ILUSTRATIVO — antes de produção:
    - Fila em memória → troque por Redis/DB (reinício apaga os jobs).
    - SEM autenticação → exija um token (header) nos endpoints.
    - Worker stubado → pluge o agente real no TODO de `executar_tarefa`.
    - Defina TETO DE GASTO por job e LOG de todas as ações (ver recipe, seção Segurança).
"""
from __future__ import annotations

import os
import uuid
import asyncio
from datetime import datetime, timezone
from enum import Enum

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title="Despacho do assistente de voz")

# --- "Banco" de jobs (em memória; troque por Redis/DB) -----------------------
JOBS: dict[str, dict] = {}

# Token simples de proteção (defina DISPATCH_TOKEN no ambiente). Vazio = sem checagem.
DISPATCH_TOKEN = os.environ.get("DISPATCH_TOKEN", "")


class Status(str, Enum):
    fila = "na_fila"
    rodando = "rodando"
    pronto = "pronto"
    erro = "erro"


class NovaTarefa(BaseModel):
    titulo: str
    descricao: str          # o que o usuário pediu, em linguagem natural
    tipo: str = "generica"  # ex.: "video", "site", "relatorio"


def _auth(token: str | None) -> None:
    if DISPATCH_TOKEN and token != DISPATCH_TOKEN:
        raise HTTPException(status_code=401, detail="token inválido")


@app.post("/tarefas")
async def criar_tarefa(t: NovaTarefa, x_token: str | None = Header(default=None)):
    """Chamada pela tool `criar_tarefa` do agente de voz. Responde NA HORA."""
    _auth(x_token)
    job_id = uuid.uuid4().hex[:8]
    JOBS[job_id] = {
        "id": job_id,
        "status": Status.fila,
        "titulo": t.titulo,
        "descricao": t.descricao,
        "tipo": t.tipo,
        "resultado": None,
        "erro": None,
        "criado_em": datetime.now(timezone.utc).isoformat(),
    }
    # dispara o trabalho em background e RETORNA imediatamente
    asyncio.create_task(executar_tarefa(job_id))
    # resposta curta pro agente falar: "tô fazendo, te aviso"
    return {"job_id": job_id, "status": Status.fila,
            "mensagem": f"Tarefa '{t.titulo}' recebida. Vou fazer e te aviso."}


@app.get("/tarefas/{job_id}")
async def status_tarefa(job_id: str, x_token: str | None = Header(default=None)):
    """Chamada pela tool `status_tarefa` — pra perguntar 'como tá meu vídeo?'."""
    _auth(x_token)
    job = JOBS.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="job não encontrado")
    return job


async def executar_tarefa(job_id: str) -> None:
    """O TRABALHADOR. Aqui entra o agente autônomo de verdade."""
    job = JOBS[job_id]
    job["status"] = Status.rodando
    try:
        # ───────────────────────────────────────────────────────────────────
        # TODO: troque este stub pelo agente real. Duas opções (ver docs/13):
        #
        #  A) Claude Managed Agents (hospedado): crie uma sessão via API
        #     (/v1/agents · /v1/sessions) com:
        #       - system prompt do trabalhador (qualidade + regras de entrega)
        #       - ferramentas: gerar vídeo (docs/14) / buildar site (Claude Code +
        #         deploy Vercel) / salvar no Drive / mandar email (MCP)
        #       - Outcome (rubrica) = critério conferível de "pronto"
        #         ex.: "vídeo gerado E salvo no Drive E email enviado"
        #
        #  B) Claude Agent SDK (no seu servidor): rode o loop você mesmo com as
        #     mesmas ferramentas e um grader separado pra decidir o "pronto".
        #
        # ⚠️ Aplique teto de gasto por job e logue cada ação.
        # ───────────────────────────────────────────────────────────────────
        resultado = await _stub_trabalho(job)        # <- REMOVER em produção

        job["resultado"] = resultado
        job["status"] = Status.pronto
        await notificar(job)                          # email/push ou ligação de voz
    except Exception as e:                            # noqa: BLE001
        job["status"] = Status.erro
        job["erro"] = str(e)
        await notificar(job)                          # avise também quando FALHA


async def _stub_trabalho(job: dict) -> dict:
    """Simula um trabalho longo. Apague quando plugar o agente real."""
    await asyncio.sleep(5)
    return {"drive_url": "https://drive.google.com/...", "email_enviado": True}


async def notificar(job: dict) -> None:
    """Fecha o ciclo: avise você quando terminar (ou falhar).

    TODO: implemente um destes:
      - email/push (mais simples), ou
      - ligação de voz ativa (outbound call do ElevenLabs/Vapi) pro seu número,
        com o agente falando: 'terminei seu vídeo, mandei no email'.
    """
    print(f"[notificar] job {job['id']} -> {job['status']}")
