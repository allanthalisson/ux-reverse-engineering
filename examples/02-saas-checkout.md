# Exemplo de resposta | Plano premium de SaaS colaborativo

**Cenário ilustrativo**, sem acesso atual a interfaces de concorrentes.

## Diagnóstico
Produto colaborativo que cobra por assento e apresenta recursos avançados. Usuários precisam avaliar se a assinatura gera valor em relação ao custo e se é fácil desfazer a decisão.

## Referência de mecanismo
O vídeo do iFood traz situações de apresentação contextual de benefícios do Clube iFood. A percepção de valor no momento de necessidade pode ser transferível, mas **não há demonstração de impacto causal nem código interno**. Propor outras referências diretas, como planos de SaaS por assento, a validar com documentação pública de preços.

## Hipótese de produto
Quando a pessoa tenta convidar um sexto membro para um workspace com limite de cinco, exibir opções de expansão com custo total explícito evita surpresa e simplifica decisão. Exibir restrições antes de a pessoa inserir dados desnecessários.

## Fluxo de UX
`Convidar membro → checar limite → limite disponível: fluxo padrão | limite excedido: modal com comparação de planos, cobrança, alternativa de remover membro e contato com admin → confirmar ou cancelar`.

### Regras propostas
| Estado | UI | Próximo passo |
| --- | --- | --- |
| limite não alcançado | formulário normal | enviar convite |
| limite excedido, sem permissão de pagar | informar admin e caminho de solicitação | solicitar alteração |
| limite excedido, com permissão | opções e custos, renovação e cancelamento claros | decidir |
| indisponibilidade do serviço | mensagem sem cobrar e fallback | tentar novamente |
| cancelamento | retorno sem perda de dados editados | continuar plano atual |

## Não adotar
Contagem regressiva ou "última chance" sem prazo real; opção de cobrança pré-selecionada; dificultar saída para pressionar compra.

## Métricas
Capacidade efetiva de convidar colegas, tempo de decisão, conversão legítima, suporte sobre cobrança, disputas e cancelamento precoce. Não tratar upsell sozinho como indicador de boa UX.
