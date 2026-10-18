# Avaliação comportamental e QA

## Objetivo
Os testes automatizados do repositório asseguram estrutura, frontmatter e consistência das cópias. **Não comprovam** que um modelo ativará a skill, fará boa pesquisa ou desenhará melhor UX. A avaliação qualitativa deve executar casos reais na plataforma alvo.

## Protocolo de testes manuais
1. Instale o mesmo bundle no Claude Code e no Codex em projetos de teste comparáveis.
2. Execute os 6 cenários de [`examples/04-skill-evaluation-cases.json`](../examples/04-skill-evaluation-cases.json), com e sem instrução explícita de ativação.
3. Registre plataforma, modelo, data, prompt, ferramentas habilitadas, fontes reais e resposta completa.
4. Aplique 8 critérios de [`quality-rubric.md`](quality-rubric.md), total máximo 24, e marque gates eliminatórios.
5. Rode de novo com projeto real e arquivos reais. Verifique se o agente lê o fluxo existente em vez de inventar arquitetura.
6. Faça inspeção por UX designer e engenheiro, e revisão de acessibilidade e privacidade, principalmente em padrões persuasivos.
7. Só declare qualidade comprovada após repetir em casos diversos com consistência e sem falsos positivos.

## Casos essenciais de regressão
- Sem rede: não inventar fatos atuais.
- Competidor sem código aberto: não atribuir código interno.
- Pedido de padrão manipulativo: recusar tática enganosa e propor alternativa.
- Alteração trivial: não disparar processo longo.
- Código presente: respeitar stack, testes e autorização.
- Fluxos com dinheiro/saúde: reforçar consentimento, clareza e risco.
- Múltiplos mercados: contextualizar localização/região do benchmark.

## Métricas para melhorar a skill
- Acerto de ativação contextual (precision/recall em amostra etiquetada).
- % de afirmações sobre terceiros rastreáveis a evidência.
- % de hipóteses claramente rotuladas.
- Completude de edge cases no fluxo.
- Taxa de soluções com alternativa não intrusiva e controle do usuário.
- Viabilidade técnica verificada por engenheiros.
- Acurácia do relatório sobre testes e modificações executados.
