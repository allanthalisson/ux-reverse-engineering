# Exemplo de resposta | Feedback após uma entrega

**Cenário ilustrativo.** O briefing cita um padrão relacionado ao iFood, mas não comprova regra interna de avaliações.

## Necessidade
Solicitar retorno quando a experiência já ocorreu e oferecer recuperação de falhas, sem manipular quem pode deixar avaliação.

## Engenharia reversa possível
Momento pós-entrega → evento disponível → convite neutro a avaliar → resposta → publicar/usar feedback seguindo políticas transparentes. A escolha de momento é uma hipótese; qualquer sistema de filtro de avaliações deve ser tratado criticamente e não replicado.

## Solução adaptada
- Conclusão do serviço confirmada → convite acessível e opcional após intervalo apropriado.
- Pergunta neutra: "Como foi a experiência?". Escala equilibrada e comentário opcional.
- Qualquer nota pode ser enviada. Canal de suporte é oferecido a quem relata problema, mas não impede avaliação legítima.
- Pular avaliação e silenciar convites disponíveis. Uma avaliação por entrega, com edição nas regras anunciadas.

## Estados
Aguardando conclusão, elegível, convidado, dispensado, respondido, offline, falha de envio, suporte solicitado. Respeitar idempotência e não disparar convite para entrega cancelada.

## Guardrails
Volume de reclamações, participação por segmento, taxa de feedback negativo recebido, abuso/spam e percepção de confiança. Não premiar notas altas com benefícios sem transparência.
