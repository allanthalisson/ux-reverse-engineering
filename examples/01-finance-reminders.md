# Exemplo de resposta | Finanças pessoais e reengajamento

**Cenário ilustrativo**, não relato de pesquisa ao vivo.

## Contexto
App financeiro que importa transações para categorização. O usuário deseja acompanhar orçamento semanal sem registrar cada movimento manualmente. Não foram fornecidos stack, dados de instrumentação nem preferências de lembretes, portanto são hipóteses.

## Oportunidade
Usuários com 3 ou mais transações pendentes podem perder visão do orçamento. Precisam de um caminho curto para concluir a revisão, não de mensagens genéricas diárias.

## Benchmark exploratório
- Duolingo, citado no vídeo do briefing como referência de reengajamento. **Status:** ilustração fornecida; lógica interna inferida, não verificada.
- Apps de tarefas com resumo periódico (a pesquisar, candidatos não validados).
- Serviços financeiros com revisões semanais voluntárias (a pesquisar, candidatos não validados).

## Mecanismo transferível
Lembrar somente quando houver uma ação relevante, em período permitido, com destino direto à tarefa e controles de frequência.

## Proposta
A pessoa escolhe se quer revisão semanal e quando receber lembretes. Se houver itens pendentes no horário permitido, o app envia uma notificação com contagem e CTA para a fila. Se tudo estiver atualizado, não envia. Se a pessoa já revisou depois do agendamento, cancela o envio. Preferências podem ser desativadas em um toque.

### Máquina de estados
```
consentimento desligado -> suprimido
consentimento ligado + 0 pendências -> inativo
consentimento ligado + pendências -> elegível
horário permitido + elegível -> programado
pendências resolvidas -> cancelado
entrega -> exibido -> aberto/ignorado
abertura -> fila de revisão -> concluído/parcial/erro
```

### Critérios de aceite
1. Usuários sem permissão não recebem lembrete push.
2. Preferências persistem entre dispositivos autorizados.
3. Ao categorizar antes do envio, a notificação pendente não é entregue.
4. A notificação não revela valores individuais em tela bloqueada.
5. Sem rede, a revisão mostra estado de sincronização e não duplica alterações.
6. Leitor de tela consegue acessar ação e fechar banner.

### Métrica
Primária: pessoas elegíveis que concluem categorização de todas as transações pendentes na semana, com denominador de pessoas elegíveis no grupo. Guardrails: desativação de push, reclamações e redução de uso voluntário.

### Risco
Frequência excessiva ou constrangimento; não usar frases que culpam o usuário. A eficácia será testada.
