# 04 | Protocolo de engenharia reversa de experiências

**Pergunta central:** qual sistema de decisões e feedback transforma uma intenção do usuário em um resultado percebido, e o que precisaria ser diferente no nosso produto?

## Anatomia de um mecanismo
1. **Entrada:** evento que coloca o usuário no fluxo, canal e expectativa anterior.
2. **Contexto:** o que o sistema precisa saber (preferências autorizadas, estado, localização apenas se necessário, sessão, dispositivo).
3. **Elegibilidade:** quando aparece, por que para aquela pessoa, restrições, frequência e consentimento.
4. **Promessa/affordance:** como o benefício é comunicado; custos, condições e alternativas visíveis.
5. **Microinterações:** ações possíveis, feedback, animação, latência, acessibilidade, reversão.
6. **Regra de decisão:** `se [estado] e [consentimento] então [exibir] senão [alternativa]`, hipótese inferida, não código real de terceiro.
7. **Estados:** inicial, carregando, completo, vazio, erro, indisponível, offline, bloqueado, expiração, retorno.
8. **Resultado:** tarefa concluída e feedback; como o usuário sabe que deu certo.
9. **Controles:** desativar, desfazer, adiar, editar preferência, sair, contestar ou suporte.
10. **Instrumentação e riscos:** eventos, guardrails, vieses, experimentos e trade-offs.

## Técnicas de reconstrução
- Walkthrough com várias situações plausíveis, jamais atribuindo estados não vistos ao app real.
- Diagrama textual: `[gatilho] -> [elegibilidade] -> {decisão} -> [UX] -> [resposta] -> [resultado]`.
- Tabela de decisão; máquina de estados; mapeamento de microcopy; fluxos de recuperação.
- Comparar usuários novos/recorrentes, primeiro sucesso/falha, opt-in/opt-out, acessibilidade, plataformas e países.
- Explorar explicações concorrentes: impacto de marca? desconto real? contexto? sazonalidade? variação de grupo de experimento?

## Camadas de inferência
- **Observado:** tela/comportamento diretamente acessado em uma versão/contexto registrado.
- **Documentado:** explicação em fonte oficial/pública identificável.
- **Inferido:** hipótese racional a partir do que foi observado; plausível, não comprovada.
- **Desconhecido:** arquitetura, regras, algoritmos, conversão, segmentação ou efeito causal sem evidência.

## Antipadrões de análise
- "Usam o algoritmo X" sem evidências; trocar por "é compatível com regra/hipótese X".
- "Duolingo aumentou retenção em 40%" sem estudo verificável e população comparável.
- Tomar script encenado, mock ou vídeo conceitual como transcrição de lógica proprietária.
- Atribuir sucesso a uma única interface ignorando oferta, marca, operação, oferta comercial ou seleção de usuários.
- Usar screenshots como licença para copiar design ou assets.

## Saída mínima de uma engenharia reversa
**Contexto → jornada reconstruída → mecanismo → evidência/limites → regra hipotética → princípio transferível → riscos → alternativa adaptada.**
