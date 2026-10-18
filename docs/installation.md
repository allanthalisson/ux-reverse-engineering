# Instalação, distribuição e manutenção

## Requisitos
- Claude Code ou Codex com suporte a skills locais; ChatGPT com fluxo de plugins/skills compatível, quando habilitado.
- Acesso ao diretório do projeto, quando a skill deve examinar arquivos.
- Ferramenta de pesquisa web ou navegador **opcional**. Sem ela, análises externas devem ser qualificadas como não verificadas.

## Claude Code
Copie o diretório autossuficiente `.claude/skills/ux-reverse-engineering/` deste projeto para `SEU_PROJETO/.claude/skills/ux-reverse-engineering/`. Para uso pessoal em diversos projetos, instale em `~/.claude/skills/ux-reverse-engineering/`. Inicie nova sessão para que a skill seja descoberta, se necessário. Use `/ux-reverse-engineering` ou peça recomendações de UX diretamente.

## Codex
Copie `.agents/skills/ux-reverse-engineering/` para `SEU_PROJETO/.agents/skills/ux-reverse-engineering/`. No ambiente Codex, peça "Use a skill ux-reverse-engineering" ou descreva problema de UX. Se a instalação global suportada por sua versão for diferente, consulte a documentação do cliente e use o mesmo conteúdo `SKILL.md` com suas referências.

## Plugin para ecossistema ChatGPT
O manifesto `.codex-plugin/plugin.json` aponta para `./skills/`, contendo o diretório autossuficiente. Gere o bundle com `python3 scripts/build.py --zip`: `dist/chatgpt-plugin-ux-reverse-engineering.zip`. A estrutura segue o modelo de pacote de plugins OpenAI. **Preparar o bundle não equivale a publicar na loja nem instalar na sua conta**; o processo de disponibilização varia entre contas, interfaces e revisão de publicação.

## Upload de Skill genérica
`dist/claude-ux-reverse-engineering.zip` e `dist/codex-ux-reverse-engineering.zip` contêm uma pasta top-level `ux-reverse-engineering/` com exatamente um `SKILL.md` e os arquivos auxiliares. Podem servir de origem para canais que aceitam upload de skills customizadas, conforme as restrições de cada plataforma.

## Windows PowerShell
```powershell
New-Item -ItemType Directory -Force -Path "C:\meu-app\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".agents\skills\ux-reverse-engineering" "C:\meu-app\.agents\skills\"
```

Para Claude, troque `.agents` por `.claude`.

## Customização
Edite `source/platforms/claude.md` ou `source/platforms/codex.md` para instruções específicas e `source/references/*` para a metodologia. Edite `source/templates/*` para formatos. Execute build + validate; evite mudanças manuais em `.claude/`, `.agents/` e `skills/`.

## GitHub
O projeto é um repositório Git convencional. Após criar um repositório remoto vazio em sua conta:
```bash
git init
git add .
git commit -m "feat: initial UX reverse engineering skill"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/ux-reverse-engineering.git
git push -u origin main
```
Não inclua arquivos confidenciais do seu app ao publicar. Os vídeos fornecidos como inspiração não fazem parte deste repositório para evitar redistribuição sem autorização.


### Publicação alternativa com GitHub CLI

Se você já tem `gh` instalado e autenticado, use `./scripts/publish-github.sh ux-reverse-engineering --private` a partir do diretório do projeto. O script **só age quando chamado explicitamente**, verifica que a árvore de trabalho está limpa e que o remote `origin` ainda não existe. Use `--public` somente se quiser tornar públicos todos os arquivos desse repositório.
