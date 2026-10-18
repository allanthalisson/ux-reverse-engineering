# Orientações para manter este repositório (Codex)

Projeto: pacote cross-platform de skill para engenharia reversa de UX.

- A fonte da verdade é `source/`; **não** modificar manualmente as distribuições geradas em `.agents/`, `.claude/` e `skills/`.
- Após mudanças, rodar `python3 scripts/build.py`, `python3 scripts/validate.py` e `python3 -m unittest discover -s tests -v`.
- Toda referência material a apps terceiros deve ser verificável e rotulada como observado, documentado, inferido ou desconhecido.
- Não incluir vídeos do usuário, imagens proprietárias, logs, credenciais ou dados pessoais no pacote.
- Preferir texto em português, com estrutura clara. Preservar compatibilidade das skills nas duas plataformas.
- Manter `SKILL.md` operacional e os detalhes nos `references/` para carregamento progressivo.
- Não inventar métricas nem implementar padrões manipulativos.
