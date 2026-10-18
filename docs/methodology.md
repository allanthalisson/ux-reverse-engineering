# Metodologia: Experience Reverse Engineering

## Tese
Um benchmark serve para ampliar o espaço de soluções, não para declarar que a implementação original é superior. A engenharia reversa de UX é a reconstrução **parcial e auditável** de comportamentos observáveis, hipóteses de mecanismo e condições de funcionamento.

## Algoritmo humano/agentivo

```text
Contexto do projeto e intenção do usuário
          ↓
Jornada atual + oportunidades + prioridades
          ↓
Perguntas de investigação por mecanismo
          ↓
Benchmarks diretos e cross-industry + contrarreferências
          ↓
Observação documentada e ledger de evidências
          ↓
Decomposição de gatilho / estado / regra / feedback / recuperação
          ↓
Princípio transferível + riscos + condições necessárias
          ↓
Soluções originais para o projeto
          ↓
Especificação, instrumentação, testes e experimento
          ↓
Aprendizado, iteração e decisão
```

## Conjunto de perguntas para investigação profunda
1. O que o usuário queria resolver antes de ver o estímulo?
2. Como o app detecta ou poderia detectar que o momento é adequado?
3. O que o usuário ganha agora, e que esforço/custo assume?
4. Qual ação é privilegiada por hierarquia, timing e microcopy?
5. Qual é a alternativa legítima, reversão e controle de preferências?
6. Que estados de loading/erro/rede/sem dados aparecem ou precisam existir?
7. O mecanismo exige escala, marca, dados sensíveis ou infraestrutura ausentes no nosso projeto?
8. Que fonte comprova a observação? O que continua inferido?
9. O efeito alegado é causal ou uma hipótese de produto?
10. Que teste menor e ético nos dirá se a translação funciona com nossos usuários?

## Antimimetismo
Transfira problema e princípio, não o código, texto, identidade, cores, ícones e comportamento coercitivo. Quando múltiplas referências convergem em uma mecânica, apresente a abstração e alternativas específicas para o nosso domínio.

## Escalonamento adaptativo
`rápido` atende dúvidas táticas sem sobrepesquisa; `profundo` faz investigação e estrutura formal; `auditoria` começa por implementação observada; `implementação` faz mudanças no código só dentro do escopo autorizado. A skill não precisa ser acionada a toda mensagem.
