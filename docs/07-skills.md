# 07 — Skills (Agent Skills)

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Confira sempre `https://code.claude.com/docs/en/skills` antes de depender de detalhes.

## O que é

Uma **Skill** é uma capacidade reutilizável empacotada como uma **pasta com um arquivo
`SKILL.md`**. Resumindo o conceito (de uma palestra da Anthropic, Barry Zhang & Mahesh
Murag — *"Don't build agents, build skills"*):

> **"Skills são só pastas."**

Cada skill é uma pasta contendo:
- **`SKILL.md`** (obrigatório) — frontmatter YAML (nome, descrição) + as instruções.
- **Arquivos auxiliares** (opcionais) — templates, exemplos, scripts (ex.: `apply_template.py`),
  docs de apoio (ex.: `docs.md`).

O ponto-chave é a **eficiência de contexto**: o Claude só "vê" a *descrição* da skill no
começo; o conteúdo completo só é **carregado sob demanda** quando a skill é relevante.
Isso é diferente do `CLAUDE.md`, que carrega sempre.

> Lema útil: **CLAUDE.md é orientação (carrega sempre). Skills carregam sob demanda.**

## Quando usar

| Quer… | Use |
|---|---|
| Encapsular um procedimento repetível (deploy, gerar carrossel, revisar PR) | Skill |
| Que o Claude **descubra e use sozinho** a capacidade quando fizer sentido | Skill (model-invoked) |
| Acionar manualmente um fluxo | `/nome-da-skill` |
| Só dar contexto/规则 que vale sempre | `CLAUDE.md` (não skill) |
| Empacotar várias skills + agents + hooks + MCP pra distribuir | **Plugin** (ver `docs/09`) |

Skill vs slash command: hoje `.claude/skills/deploy/SKILL.md` e `.claude/commands/deploy.md`
ambos criam `/deploy` e se comportam igual — mas **skills são o caminho recomendado** (commands
em `.claude/commands/` continuam funcionando, mas são o jeito antigo).

## Como configurar / usar

### Onde a skill pode viver
- **Projeto:** `.claude/skills/<nome>/SKILL.md` (versionado, compartilhado com o time)
- **Usuário:** `~/.claude/skills/<nome>/SKILL.md` (pessoal, todos os projetos)
- **Plugin:** dentro de um plugin (`skills/<nome>/SKILL.md`)

### Estrutura mínima
```
.claude/skills/
└── carousel/
    ├── SKILL.md          # obrigatório
    ├── template.html     # auxiliar (opcional)
    └── gerar.py          # script (opcional)
```

### `SKILL.md` (exemplo)
```markdown
---
name: carousel
description: Gera um carrossel de Instagram (PNG) a partir de um tema. Use quando
  o usuário pedir um carrossel, post ou criativo para redes sociais.
# disable-model-invocation: true   # (opcional) só roda quando chamada por /carousel
---

# Gerador de Carrossel

1. Pergunte o tema e a quantidade de slides.
2. Use `template.html` como base de layout.
3. Rode `gerar.py` para exportar os PNGs.
```

- A **`description`** é o que o Claude lê para decidir usar a skill sozinho — escreva-a
  deixando claro **o que faz** e **quando usar**.
- `disable-model-invocation: true` faz a skill rodar **só** quando você chama `/carousel`
  (o Claude não a invoca automaticamente).

### Como o Claude descobre e invoca
- **Model-invoked:** o Claude usa a skill automaticamente quando a tarefa casa com a
  `description` (a menos que desabilitado).
- **Manual:** você digita `/nome-da-skill`.
- **Skills aninhadas:** skills em subpastas abaixo do diretório de trabalho carregam
  automaticamente e aparecem com **nome qualificado** (ex.: `apps/web:deploy`).
- **Contexto dinâmico:** dá pra injetar saída de comando antes do Claude ler a skill,
  com a sintaxe `` !`comando` `` no `SKILL.md`.

### Como instalar skills de terceiros
- **Plugins/marketplace (oficial):** `/plugin marketplace add <org>/<repo>` e depois
  `/plugin install <nome>` (ver `docs/09`).
- **CLI da comunidade `skills`:** `npx skills add <owner/repo>`
  (ex.: `npx skills add remotion-dev/skills`). ⚠️ É ferramenta **da comunidade**, não
  oficial — revise o que está instalando.

> Portabilidade: skills seguem a **spec Agent Skills** (`agentskills.io`), então as mesmas
> pastas funcionam em outros agentes compatíveis (Codex, Cursor, etc.).

## Exemplo (skill oficial de marca, do talk da Anthropic)

```
anthropic_brand/
├── SKILL.md          # "use as cores/tom da marca ao gerar materiais"
├── docs.md           # guidelines detalhadas
├── slide-decks.md    # padrões de apresentação
└── apply_template.py # script que aplica o template
```
O Claude carrega `SKILL.md` só quando vai produzir algo de marca; os arquivos pesados
(`docs.md`, `slide-decks.md`) entram só se necessário.

## Pegadinhas ⚠️

- **A `description` é tudo.** Se ela for vaga, o Claude não saberá quando usar a skill
  (model-invocation falha silenciosamente). Diga o gatilho ("use quando…").
- **Skill ≠ command ≠ CLAUDE.md.** Skill carrega sob demanda; CLAUDE.md sempre; command
  é o formato antigo (use skill).
- **Pasta, não arquivo solto.** Uma skill é uma **pasta** com `SKILL.md` dentro — não um
  `.md` solto em `.claude/skills/`.
- **`npx skills add` é de terceiros.** Não confunda com recurso oficial; audite antes.
  Para distribuição confiável, prefira plugins/marketplace.
- **Segurança de supply-chain.** Skills podem conter scripts. Leia o código de skills de
  terceiros antes de instalar (lembre do incidente de jun/2026 na pesquisa).

## Referências oficiais

- Skills: https://code.claude.com/docs/en/skills
- Plugins (distribuição de skills): https://code.claude.com/docs/en/plugins
- Spec Agent Skills (portabilidade): https://agentskills.io/specification

> Curadoria relacionada: ver "skills" em `reference/curadoria-conteudo.md` e o catálogo
> em `reference/repos-recomendados.md` (superpowers, stop-slop, obsidian-skills,
> ui-ux-pro-max, banana-claude, Remotion, knowledge-work-plugins, etc.).
</content>
