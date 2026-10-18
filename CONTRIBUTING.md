# Contribuindo

## Fluxo de contribuição
1. Abrir issue com problema concreto, caso de uso ou evidência verificável.
2. Alterar **apenas** `source/`, docs, exemplos, testes e scripts de manutenção.
3. Se adicionar nova regra, documentar por que resolve um caso real e seu risco de regressão/uso abusivo.
4. Rodar `python3 scripts/build.py`, `python3 scripts/validate.py`, `python3 -m unittest discover -s tests -v`.
5. Commitar as distribuições regeneradas para instalações sem build.

## Política de evidência
Não enviar prints com dados pessoais, conteúdo protegido sem permissão, códigos internos de terceiros nem depoimentos fabricados. Benchmarks devem ser datados e com limites claros. Capturas de terceiros são material de pesquisa, não parte automaticamente licenciável do repositório.

## Padrões
- Nome da skill: `ux-reverse-engineering`.
- Frontmatter `name` + `description` em cada `SKILL.md`.
- Manter referências autocontidas nas três versões.
- Não adicionar dependências externas aos scripts se Python stdlib atender.
- Documentar quando um recurso depende de tool/browser que pode não existir.
