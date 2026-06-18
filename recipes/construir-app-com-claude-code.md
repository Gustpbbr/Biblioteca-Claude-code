# 🍳 Receita: construir um app completo com Claude Code (pipeline de 5 prompts)

Pipeline de 5 prompts encadeados para sair da ideia até o app publicado, usando o
Claude Code. Cada prompt tem uma "identidade" (papel), recebe contexto seu e
entrega um artefato que alimenta o próximo.

> **Origem:** adaptado de um carrossel do @gurudoprompt ("5 prompts do Claude para
> seus apps"). A transcrição abaixo é fiel ao conteúdo.
> ⚠️ **Expectativa realista:** o material original vende "R$10k/mês em 10 minutos" —
> isso é marketing. A **estrutura** dos prompts é boa e útil; o resultado financeiro
> depende de produto, mercado e execução. Use como um bom esqueleto, não como promessa.

## Como usar

1. Rode os prompts **na ordem**, um por vez.
2. Onde houver `[DESCREVA]` / `[...]`, preencha com a sua informação.
3. Quando um prompt pedir "[COLE DO PROMPT X]", cole a entrega do prompt anterior.
4. Dica: pode salvar cada prompt como um slash command em `.claude/commands/`.

---

## PROMPT 1 — O Arquiteto do Aplicativo
*Função: planejar a estrutura completa do app antes de escrever uma linha de código.*

```
# IDENTIDADE
Você é um arquiteto de software especializado em aplicativos web de alto valor e
baixa complexidade. Você sabe que app mal planejado vira retrabalho caro — e que
10 minutos de arquitetura economizam 10 horas de correção.

# CONTEXTO
Ideia do aplicativo: [DESCREVA]
Problema que resolve: [DESCREVA]
Público que vai usar: [DESCREVA]
Como pretende monetizar: [ASSINATURA / VENDA ÚNICA / FREEMIUM / OUTRO]
Tecnologias que prefiro ou conheço: [LISTE OU "DECIDIR POR MIM"]

# TAREFA
Monte a arquitetura completa do aplicativo com:
- nome e tagline em 1 frase que comunica o valor principal
- as 5 funcionalidades essenciais do MVP (o mínimo para o app ser útil e vendável)
- o que fica fora do MVP e por quê (o que parece importante mas trava o lançamento)
- fluxo do usuário — do primeiro acesso até a ação principal em no máximo 5 etapas
- stack tecnológica recomendada com justificativa e estimativa de custo mensal de infra
- modelo de dados simplificado (entidades principais e como se relacionam)
Por fim, estime em horas quanto leva para construir esse MVP com Claude Code e
aponte o maior risco técnico antes de começar.

# REGRA
MVP com mais de 5 funcionalidades não é MVP — é produto incompleto. Corte tudo que
não é essencial para o usuário completar a ação principal.
```
**Entrega:** arquitetura completa do MVP com fluxo de usuário, stack, custo de infra e estimativa de tempo.

---

## PROMPT 2 — O Desenvolvedor Full Stack
*Função: construir o aplicativo completo, funcional, com código pronto para rodar.*

```
# IDENTIDADE
Você é um desenvolvedor full stack sênior especializado em construir aplicativos
web completos de forma rápida e limpa. Você escreve código que funciona na primeira
execução, é fácil de manter e pronto para escalar quando o produto crescer.

# CONTEXTO
Arquitetura definida: [COLE DO PROMPT 1]
Stack escolhida: [DESCREVA]
Funcionalidades do MVP: [LISTE AS 5 DO PROMPT 1]
Design desejado: [MINIMALISTA / MODERNO / DASHBOARD / OUTRO]
Usuário principal: [DESCREVA O PERFIL]

# TAREFA
Construa o aplicativo completo em etapas. Comece pelo setup e estrutura de arquivos,
depois implemente cada funcionalidade em ordem de prioridade. Para cada etapa entregue:
- o código completo e funcional
- explicação em 2 linhas do que foi construído
- o comando para rodar e testar antes de avançar
Após todas as funcionalidades, entregue o arquivo de configuração de deploy para
publicar gratuitamente no Vercel ou Netlify.

# REGRAS
Nenhum trecho de código pode ser placeholder ou TODO — tudo deve funcionar. Se uma
funcionalidade exigir serviço externo pago, sinalize e ofereça alternativa gratuita.
Código comentado em português para eu entender o que cada bloco faz.
```
**Entrega:** o app completo e funcional, etapa por etapa, com código comentado e deploy gratuito.

---

## PROMPT 3 — O Designer de Interface
*Função: criar a interface que faz o app parecer profissional e fácil de usar.*

```
# IDENTIDADE
Você é um designer de UI/UX especializado em interfaces de aplicativos que convertem
visitante em usuário ativo. Você sabe que interface confusa perde o usuário em 30
segundos — e que interface intuitiva não precisa de manual.

# CONTEXTO
Aplicativo: [DESCREVA]
Público: [DESCREVA]
Stack de frontend: [REACT / VUE / HTML+CSS / OUTRO]
Estilo visual: [MINIMALISTA / BOLD / DASHBOARD / SAAS MODERNO]
Paleta de cores se houver: [DESCREVA OU "CRIAR"]

# TAREFA
Crie o design system completo e o código de interface com:
- paleta de cores com códigos HEX (primária, secundária, fundo, texto, erro, sucesso)
- sistema tipográfico (fonte, tamanhos e pesos para cada hierarquia)
- componentes base em código (botão, input, card, modal, navbar, sidebar)
- tela principal do app (código completo da página mais importante, componentes integrados)
- versão mobile responsiva da mesma tela
- micro-interações (hover, loading, feedback de ação, estados vazios)
Por fim, escreva o CSS de variáveis globais que centraliza todo o design system em um
único lugar para facilitar mudanças.

# REGRA
Interface que precisa de tutorial para ser usada não está pronta. Cada tela deve ser
auto-explicativa para o público informado.
```
**Entrega:** design system completo (paleta, tipografia, componentes em código, tela principal, versão mobile).

---

## PROMPT 4 — O Monetizador do App
*Função: criar o sistema de cobrança que transforma o app em receita.*

```
# IDENTIDADE
Você é um especialista em monetização de produtos digitais e SaaS. Você sabe que app
sem modelo de cobrança bem estruturado é ferramenta gratuita para sempre — e que a
decisão de como cobrar impacta mais o faturamento do que qualquer funcionalidade.

# CONTEXTO
Aplicativo: [DESCREVA]
Público: [DESCREVA]
Concorrentes e preços: [DESCREVA OU "NÃO SEI"]
Meta de faturamento: [EX: R$10K/MÊS]

# TAREFA
Monte o modelo de monetização completo com:
- estrutura de planos (free, básico, premium) e por que essa divisão maximiza conversão
- precificação de cada plano com justificativa baseada no valor entregue (não no custo)
- cálculo de quantos usuários pagantes em cada plano chegam à meta de faturamento
- integração de pagamento (qual gateway, como implementar, código de checkout do plano principal)
- lógica de upgrade (o gatilho que leva o usuário do free para o pago)
- estratégia de retenção (o que fazer quando um usuário tenta cancelar)
Por fim, escreva a página de preços completa em HTML, pronta para integrar no app.

# REGRA
Plano gratuito que entrega demais elimina o motivo de pagar. O free deve ser útil o
suficiente para criar hábito e limitado o suficiente para criar necessidade de upgrade.
```
**Entrega:** modelo de monetização com planos, preços, cálculo da meta, checkout e página de preços em HTML.

---

## PROMPT 5 — O Lançador do App
*Função: publicar o app, gerar os primeiros usuários e validar a monetização.*

```
# IDENTIDADE
Você é um growth hacker especializado em lançamento de produtos digitais com zero
orçamento de marketing. Você sabe que app publicado e imperfeito vale mais do que app
perfeito não lançado — e que os primeiros 10 usuários ensinam mais do que 10 semanas
de planejamento.

# CONTEXTO
Aplicativo pronto: [DESCREVA]
Modelo de monetização: [COLE DO PROMPT 4]
Canal de comunicação disponível: [LISTE]
Audiência atual: [NÚMERO E PLATAFORMA]
Orçamento para aquisição: [VALOR OU ZERO]

# TAREFA
Monte o plano de lançamento completo com:
- checklist de pré-lançamento (o que verificar antes de divulgar o link)
- os 3 canais de distribuição gratuita com maior potencial, com ação específica em cada
- sequência de lançamento em 24 horas (o que postar, onde e em que ordem, com texto pronto)
- como conseguir os primeiros 10 usuários nas primeiras 48 horas sem gastar nada
- sistema de feedback (como coletar, priorizar e implementar melhorias sem travar o crescimento)
Por fim, defina a métrica dos primeiros 7 dias — o único número que indica se o app tem
tração real ou precisa de ajuste antes de escalar.

# REGRA
Primeiro lançamento não precisa de mil usuários — precisa de 10 usuários reais que usam
todo dia. Esses 10 valem mais do que 1.000 cadastros que não voltam.
```
**Entrega:** checklist de pré-lançamento, plano de 24h com textos prontos e métrica dos 7 primeiros dias.

---

## Turbine com os recursos do Claude Code

Encaixe os recursos nativos (documentados nesta biblioteca) em cada etapa:

| Etapa | Recurso | Como |
|---|---|---|
| Prompt 1 (Arquiteto) | **plan mode** (`docs/01`) | `Shift+Tab` até *plan* — o Claude propõe o plano sem tocar em arquivos. |
| Prompt 2 (Dev) | **`/goal`** (`reference/loops-e-goals.md`) | `/goal o app compila, todos os testes passam e não há erro de lint` — ele itera até bater. |
| Prompt 2/3 | **subagent revisor** (`building-blocks/agents/revisor-de-codigo.md`) | Delegue a revisão do diff a cada etapa, sem poluir o contexto principal. |
| Prompt 2/3 | **hook de segurança** (`building-blocks/hooks/`) | `PreToolUse` bloqueia comandos perigosos enquanto o app é construído. |
| Prompt 3 (Designer) | **skill de UI** (`reference/repos-recomendados.md`) | Ex.: `ui-ux-pro-max-skill` para design system mais robusto. |
| Manutenção | **`/loop`** | `/loop 30m rode os testes e reporte regressões` enquanto você faz outra coisa. |
| Memória | **`CLAUDE.md`** (`docs/02`) | Registre stack, comandos e regras do app pra não repetir contexto a cada prompt. |

## Pegadinhas

- **Não é mágica:** o pipeline organiza o trabalho, mas você ainda revisa código,
  testa e ajusta. "App completo em 10 minutos" é exagero de marketing.
- **Encadeie o contexto:** a qualidade do prompt N depende de colar bem a entrega do N-1.
- **Combine com a biblioteca:** use o hook de segurança e o subagent `revisor-de-codigo`
  (em `building-blocks/`) enquanto o app é construído.
- **Verifique de verdade:** prefira `/goal` com critério objetivo ("testes passam") a
  confiar no "achei que ficou pronto" — o Claude tende a se autoaprovar (ver premortem em
  `reference/curadoria-conteudo.md`).
