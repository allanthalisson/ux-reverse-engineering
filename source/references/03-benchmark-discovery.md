# 03 | Busca e seleção de benchmarks

## Buscar o padrão, não a marca
Traduza a oportunidade para um mecanismo abstrato, por exemplo:
- `retenção` → hábito, feedback de progresso, reengajamento contextual, preferência de frequência;
- `checkout` → eliminação de incerteza, transparência de custo, reduzir esforço de decisão;
- `fidelidade` → benefício progressivo, valor de recorrência, clareza de contrapartidas;
- `feedback` → convite contextual, recuperação de falhas, canal honesto e não seletivo;
- `colaboração` → presença, permissões, histórico, sincronização e resolução de conflito.

## Funil de descoberta
1. Defina o JTBD, segmento, plataforma, região e tipo de decisão.
2. Identifique **3 a 5 candidatos**: referência direta, cross-industry, alternativa mais simples e possível contrarreferência.
3. Utilize fontes legítimas: documentação oficial, help center, páginas de produto, release notes, vídeos demonstrativos, reviews datados, pesquisas, telas públicas e experiência própria autorizada.
4. Valide que a funcionalidade **existe na versão/região/plano** relevantes e registre data. Designs mudam rapidamente e podem variar em experimentos A/B.
5. Aprofunde 2 a 3 candidatos em modo profundo. Prefira diversidade de mecanismos à repetição de apps famosos.
6. Registrar também motivo de exclusão de candidatos irrelevantes.

## Critérios de benchmark
- Correspondência do problema do usuário (mais relevante que mesma vertical).
- Similaridade das condições: frequência de uso, risco, complexidade e dispositivo.
- Acesso a evidências inspecionáveis e atualizadas.
- Possibilidade de transferir o mecanismo sem depender de escala, marca ou dados não disponíveis.
- Sinais de qualidade de experiência sem confundir popularidade, receita ou adoção com benefício ao usuário.
- Conformidade ética, legal, acessibilidade e cultural.

## Pesquisa responsável
- Nunca afirmar resultado de busca sem ferramenta/fonte de fato consultada.
- Não compartilhar telas com informações pessoais de contas de terceiros.
- Respeitar propriedade intelectual, termos de serviço, robots aplicável e limites de acesso; não contornar paywall, MFA, rate-limit ou proteção técnica.
- Não coletar analytics privados nem fazer engenharia de código proprietário a partir de artefatos ilegítimos.
- Cite link específico, descrição do que demonstra, data observada e grau de confiança.

## Quando falta navegador ou internet
Fornecer análise conceitual com referências **ilustrativas** e marcar `não verificado nesta execução`. Oferecer plano de verificação/roteiro de teste manual. Não inventar layout de telas, números de conversão ou comportamento atual de app.

## Matriz comparativa
| Produto | Problema resolvido | Mecânica observada | Fonte/data | Condição de validade | Transferibilidade | Limite |
| --- | --- | --- | --- | --- | --- | --- |
| Duolingo | rotina de estudo | lembretes e progresso, em determinadas versões | fonte | opt-in e frequência | alta para rotina | excesso de notificação |
