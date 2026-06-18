# CLAUDE.md — Biblioteca Claude Code

Memória do projeto para o próprio Claude Code ao trabalhar neste repositório.

## O que é este repositório

Uma **biblioteca de referência sobre o Claude Code**, em Português (BR), feita
para ser reutilizada em todos os outros projetos do usuário. Documenta todas as
funcionalidades do Claude Code e oferece peças prontas (commands, hooks, agents,
skills, templates) para copiar em outros projetos.

## Princípios de conteúdo

- **Idioma:** Português (BR). Termos técnicos consagrados podem ficar em inglês
  (ex: "hooks", "slash commands"), mas a explicação é sempre em PT-BR.
- **Precisão acima de tudo:** antes de documentar uma funcionalidade, conferir
  com a documentação oficial atual do Claude Code. Não escrever de memória sobre
  detalhes que possam ter mudado. Usar o agente `claude-code-guide` e/ou busca web.
- **Formato consistente dos docs:** cada arquivo em `docs/` segue
  **O que é → Quando usar → Como configurar → Exemplo → Pegadinhas → Referências oficiais**.
- **Peças prontas devem ser reais e testáveis**, não pseudocódigo. Cada peça em
  `building-blocks/` traz um cabeçalho explicando o que faz e como instalar.

## Estrutura

- `docs/` — referência explicativa (numerada de 01 a 13)
- `building-blocks/` — componentes reutilizáveis (commands, agents, hooks, skills, settings, claude-md)
- `recipes/` — guias práticos passo a passo
- `reference/` — cheatsheets e tabelas de consulta rápida

## Fluxo de trabalho

- Construir "esqueleto primeiro, depois preencher": a estrutura existe com stubs;
  o conteúdo é preenchido seção por seção, com revisão do usuário.
- Branch de desenvolvimento: `claude/portuguese-greeting-vcgid2`.
- Commits descritivos; push para a branch de desenvolvimento.
