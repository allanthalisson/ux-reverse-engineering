# 09 | Hipóteses, experimentação e métricas

## Hipótese falsificável
Para `[segmento]` que tenta `[job]`, oferecer `[mecanismo]` em `[momento]` deve melhorar `[resultado do usuário + métrica]` comparado a `[controle]`, sem piorar `[guardrails]`, porque `[hipótese causal]`.

## Instrumentação e validade
- Definir unidade de análise (usuário, sessão, pedido), evento de exposição, elegibilidade e denominador.
- Métrica primária orientada a resultado do usuário e do produto; não medir apenas cliques em estímulo.
- Guardrails: opt-outs, reclamações, desistência, desinstalação, chargebacks, acessibilidade, erros, latência, tickets.
- Avaliar cohort, novidade, sazonalidade, canais de aquisição, diferentes dispositivos, rede, países e experimentos simultâneos.
- Quando possível, A/B aleatorizado consistente com unidade e não contaminação; plano de tamanho amostral/poder com analista e prazo realista.
- Se A/B inviável, teste de usabilidade, entrevista, piloto, análise por tarefas ou série temporal, reconhecendo limitações causais.
- Eventos devem respeitar privacidade e retenção de dados. Não inventar números, lifts ou resultados externos.

## Exemplo de especificação
**Hipótese:** usuários que aceitaram lembretes semanais e têm tarefas pendentes recebem um lembrete relevante, melhorando conclusão semanal sem aumentar desligamento de push.

**Primária:** usuários elegíveis com tarefa concluída em até 7 dias / usuários elegíveis expostos, mais comparação com controle com mesma janela.

**Guardrails:** taxa de opt-out de push, feedback "não útil", abandono do app em 30 dias, reclamações, entregas duplicadas.

**Logs:** evento de elegibilidade, exposição/envio, abertura, ação concluída, controle atualizado; timezone, janela, persistência e duplicação.

**Critério de parada:** definido antes, incluindo incidentes de privacidade, experiência negativa e incidentes operacionais; jamais analisar continuamente e declarar vitória só em pico temporário.

## Revisão pós-teste
Registrar conclusão e incerteza, perfil da amostra, efeito estimado e incerteza, guardrails, hipóteses alternativas, decisões `lançar | iterar | descartar`, e melhorias no catálogo interno de aprendizados. Se não há dados, recomendar validação em vez de fingir.
