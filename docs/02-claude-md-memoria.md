# 02 — CLAUDE.md (memória)

> Verificado em 2026-06-18 contra a doc oficial (via agente `claude-code-guide`).
> Ref: `code.claude.com/docs/en/memory`.

## O que é

O **`CLAUDE.md`** é a **memória do projeto**: um (ou vários) arquivo Markdown que o Claude
Code **carrega automaticamente no início da sessão** e usa como contexto/orientação
persistente. É **advisory** (orientação que o modelo *deve* seguir, mas não é garantido) —
diferente de **hooks**, que são determinísticos.

> Lema: **CLAUDE.md é orientação (carrega sempre). Skills carregam sob demanda. Hooks são determinísticos.**

## Quando usar

| Quer registrar… | Onde |
|---|---|
| Regras/contexto do projeto pro time | `./CLAUDE.md` (ou `./.claude/CLAUDE.md`) |
| Preferências suas neste projeto | `CLAUDE.local.md` (→ `.gitignore`) |
| Preferências suas em todos os projetos | `~/.claude/CLAUDE.md` |
| Regra que só vale pra parte do código | `.claude/rules/` com `paths:` (path-scoped) |
| Algo que **tem** que acontecer sempre | ❌ não é memória → use **hook** (`docs/06`) |

## Como configurar / usar

### Onde vive (e ordem de carga)
- **Managed/MDM** (imposto pela organização)
- **Usuário:** `~/.claude/CLAUDE.md`
- **Projeto:** `./CLAUDE.md` **ou** `./.claude/CLAUDE.md` (qualquer um serve)
- **Aninhado:** `CLAUDE.md` em subpastas — carrega **sob demanda** quando o Claude lê
  arquivos daquela pasta (não no início).
- **`CLAUDE.local.md`** (raiz): preferências pessoais do projeto — **não deprecado**;
  coloque no `.gitignore`.

### Imports com `@`
Dentro do `CLAUDE.md`, `@caminho/arquivo` **importa** outro arquivo (expande inline,
carregado no início):
```markdown
# Preferências individuais
@~/.claude/minhas-regras.md

# Padrões do projeto
@./docs/convencoes.md
```

### Comandos úteis
- **`/init`** — gera um `CLAUDE.md` inicial analisando o projeto.
- **`/memory`** — abre o `CLAUDE.md` pra editar.

### Path-scoping de verdade
Para regras que só valem em certos caminhos, use **`.claude/rules/`** com frontmatter
`paths:` (carrega só ao tocar arquivos que casam o glob). `CLAUDE.md` aninhado **não** é
path-scoped — ele carrega quando o Claude lê arquivos naquela pasta.

## Exemplo (`CLAUDE.md` enxuto)
```markdown
# Projeto X

## Stack
- Next.js + TypeScript + Supabase.

## Regras
- Sempre rode `npm run lint` antes de propor um commit.
- Nunca leia/edite `.env*`.
- Commits em PT-BR, imperativo, curtos.

## Comandos
- Testes: `npm run test`
- Dev: `npm run dev`

@./docs/convencoes-de-codigo.md
```

## Pegadinhas ⚠️

- **Mantenha curto (< ~200 linhas).** Arquivos grandes consomem contexto e **reduzem a
  aderência** — o Claude segue menos. Veja `reference/claude-md-boas-praticas.md`.
- **`#` NÃO adiciona à memória.** Use `/memory`. (Erro comum.)
- **É advisory, não garantia.** Para algo obrigatório/determinístico, use **hook**.
- **Aninhado ≠ path-scoped.** Path-scoping real é `.claude/rules/` com `paths:`.
- **Segredos não vão no CLAUDE.md** (ele entra no contexto). Use `settings` `deny` pra
  proteger `.env`.

## Referências oficiais

- Memória / CLAUDE.md: https://code.claude.com/docs/en/memory
- Boas práticas: `reference/claude-md-boas-praticas.md`
- Template pronto: `building-blocks/claude-md/template-generico.md`
- (relacionado) Rules path-scoped: `docs/03` · Anatomia: `reference/anatomia-projeto-claude.md`
</content>
