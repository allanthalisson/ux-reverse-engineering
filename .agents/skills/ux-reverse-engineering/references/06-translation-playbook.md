# 06 | Translação: de benchmark à solução original

## Evite transplante ingênuo
Não transportar cor, mascote, gamificação, paywall ou notificações de um aplicativo famoso sem examinar necessidade, motivação, frequência de uso e restrições do produto destinatário. A experiência deve usar os recursos do nosso produto, respeitando marca e expectativas locais.

## Processo de tradução
1. **Mecânica fonte:** o que o usuário vê/faz, em que contexto.
2. **Intenção declarada/inferida:** reduzir esforço? comunicar benefício? sugerir ação? reforçar aprendizado?
3. **Necessidade humana:** previsibilidade, competência, controle, segurança, progresso, pertencimento, economia de tempo.
4. **Condições necessárias:** retorno frequente, dados atualizados, permissões, orçamento, incentivos, suporte, confiança prévia.
5. **Incompatibilidades:** uso esporádico, tarefas sensíveis, ausência de dados, risco de ansiedade, legislação, monetização distinta.
6. **Abstração:** uma frase sem marca e sem componente visual, como "um lembrete opt-in no momento em que existe uma tarefa relevante pendente".
7. **Soluções alternativas:** desenhar pelo menos 2 possibilidades em modo profundo, incluindo opção de menor intrusão.
8. **Recomendação:** escolher alternativa com racional, vantagem ao usuário, trade-offs, confiança, custo e hipótese verificável.

## Transferir princípio, não apresentação
| Padrão observado | Abstração | Adaptação responsável | Evitar |
| --- | --- | --- | --- |
| streak e progresso | feedback de avanço significativo | progresso de hábitos definidos pelo próprio usuário | culpa por interrupção |
| upsell contextual | proposta de valor no momento relevante | benefícios e custo total claramente expostos | escassez falsa |
| pedido de avaliação | feedback próximo ao evento vivenciado | convite neutro a qualquer avaliação | filtrar apenas respostas positivas |
| ordem do fluxo | reduzir esforço da ação prioritária | preencher informações previsíveis com consentimento | preseleção onerosa |

## Níveis de entrega
- **Conceito:** problema, mecanismo, proposta, trade-off, evidências.
- **Fluxo:** objetivo, atores, pré-condições, decisões, estados, microcopy, erros, acessibilidade.
- **Produto:** componentes, estados, política, dados/eventos, configurações, métrica, rollout.
- **Engenharia:** arquivos reais, contrato de API, idempotência, testes, observabilidade, release flag.

## Barreira anti-dark-pattern
Se a eficácia potencial depender de enganar, envergonhar, forçar, ocultar preço, usar avaliações seletivas ou tornar saída difícil, substituir por alternativa que preserve autonomia e clareza; documentar o porquê. Ganho potencial de conversão não autoriza violar esse requisito.
