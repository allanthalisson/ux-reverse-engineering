# 10 | Exemplos de operação da skill

> Estes exemplos nascem do briefing dos vídeos fornecidos e são **ilustrações**, não reprodução verificada de código interno ou auditoria de UX atual de terceiros.

## A. Duolingo → hábito e reengajamento
**Questão:** como promover continuidade de uma prática recorrente sem perturbar usuários?

**Nos vídeos:** apresenta-se lógica de horários, histórico, progresso e mensagens de reengajamento. Atribuir regras internas específicas somente como **inferências**, não como código de produção.

**Mecanismo abstrato:** utilizar sinal de tarefa relevante + momento autorizado + feedback de progresso + controle da frequência.

**Translação:** no app de finanças, identificar transações não categorizadas e oferecer revisão em horário escolhido pelo usuário, com opção adiar e desligar. Não copiar mascote/streak nem induzir culpa. Exigir opt-in para push; frequência limitada; somente notificar se ação é pertinente.

**Estados:** sem transações → sem notificação; pendentes + consentimento → elegível; horário permitido → agendar; ação concluída antes do envio → cancelar; desativação → suprimir; falha de envio → registrar; abertura → revisão com foco no item pendente.

**Métrica:** proporção de itens categorizados por elegível na janela, guardrails de opt-out e avaliações de utilidade. Eficácia deve ser testada.

## B. iFood → benefício contextual e avaliação honesta
**Questão:** quando exibir benefícios de assinatura e quando solicitar avaliação para não interromper a tarefa?

**Nos vídeos:** ilustram-se gatilhos relacionados ao Clube iFood, valor percebido, FOMO e solicitação de feedback em momento conectado à jornada de pedido. Não assumir algoritmo, testes de desempenho ou implementação atual.

**Mecanismo abstrato A:** apresentar uma proposta de valor no ponto em que o usuário entende exatamente custo, benefício e alternativa.

**Translação A:** em app de SaaS colaborativo, oferecer plano adicional ao atingir uma necessidade real de colaboração; preço, renovação, limites e botão `continuar no plano atual` visíveis. Nunca inventar escassez.

**Mecanismo abstrato B:** pedir avaliação depois da experiência ser observável, sem enviesar notas ou ocultar opiniões negativas.

**Translação B:** após entrega real de serviço, permitir nota e comentário honestos a todos, com encaminhamento paralelo de problemas para resolução, nunca condicionando publicação à avaliação positiva.

**Guardrails:** reclamações, cancelamento de assinatura, tickets sobre cobrança, proporção de feedback negativo recebido, tempo para concluir tarefa. Priorizar transparência.

## C. Novo projeto: app de educação profissional
**Contexto fictício:** microaulas assíncronas, adultos sem rotina fixa, objetivo: aprendizado sustentável.

**Oportunidade:** retorno às aulas interrompidas.

**Candidatos de benchmark:** Duolingo (retorno), plataformas de leitura com continuar de onde parou, apps de mindfulness com cadência voluntária. Verificar mecanicamente o que está disponível antes de descrever telas.

**Proposta:** resumo da última lição + botão de retomada + preferência de aviso semanal, sem streak punitivo.

**Fluxo:** login → curso em andamento → progresso salvo → CTA "Retomar do ponto anterior" → feedback de conclusão → sugestão de próximo passo; retorno offline e falha de sincronização tratados.

**Validação:** conclusão de lições iniciadas, retorno por cohorts, abandonos, opt-out e satisfação com retomada.

## D. Novo projeto: marketplace de serviços
**Contexto fictício:** comparar profissionais sem dominar termos técnicos.

**Oportunidade:** reduzir incerteza na escolha.

**Benchmarks:** comparação de planos SaaS, status/logística do iFood e marketplaces com transparência de reputação. Não inferir que avaliações representam população total sem critérios de coleta.

**Proposta:** comparação lado a lado de prazo, preço total estimado, verificações relevantes, políticas e suporte; revelar limites dos dados e deixar ação reversível até confirmação.

**Estados:** sem ofertas, oferta expirada, valores indefinidos, divergência de disponibilidade, denúncia e suporte. **Métricas:** contratação concluída com baixa taxa de disputa/reembolso.

## E. Padrão de resposta ruim e sua correção
**Ruim:** "Copie a notificação do Duolingo, usa algoritmo de IA e aumenta retenção 35%."

**Correto:** "O vídeo sugere uma estratégia de reengajamento contextual. Não temos acesso ao sistema de decisão nem a medição causal. Podemos testar lembretes opt-in ligados a tarefas pendentes e medir conclusão e desativação.".
