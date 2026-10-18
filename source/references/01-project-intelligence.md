# 01 | Project intelligence e context awareness

## Objetivo
Reconstruir o contexto útil do projeto **sem um questionário genérico**. A conversa é a fonte primária de intenção do usuário; arquivos reais são a fonte primária de arquitetura e implementação; pesquisas externas ajudam apenas a conhecer soluções de mercado. Não tratar suposições como decisões já tomadas.

## Extrair silenciosamente
1. **Proposta de valor:** quem tem que resultado, em que contexto, usando que produto.
2. **Jobs to Be Done:** situação, motivação, progresso desejado, alternativas atuais.
3. **Públicos:** novos/recorrentes, power users, acessibilidade, cultura/região, poder aquisitivo quando relevante, consentimento.
4. **Momento da jornada:** descoberta, cadastro, primeira vitória, uso frequente, colaboração, pagamento, pausa, churn, suporte, encerramento.
5. **Desenho do fluxo:** telas atuais, sequências, permissões, dependências, erros, dados e políticas.
6. **Contexto de tecnologia:** web/mobile/híbrido; frontend; backend; estado; analytics; design system; experimentação; testes; dispositivos.
7. **Objetivos e restrições:** KPIs, prazos, plataformas, restrições legais, operacionais, de acessibilidade e orçamento.
8. **Feedback observável:** relatos de usuários, analytics, tickets, sessão/heurísticas, experimentos, decisões anteriores.

## Ordem para coletar evidências locais (se houver repositório)
- README, PRODUCT.md, PRD, backlog, protótipos, docs e AGENTS/CLAUDE de produto.
- Rotas/páginas/componentes/fluxos e arquivos de tokens/design system.
- Eventos de analytics, consentimento, preferências, i18n, feature flags, testes.
- Capturas/arquivos fornecidos no chat.
- Nunca usar credenciais, tokens, `.env` ou dados identificáveis para pesquisa externa.

## Cartão de contexto, atualizado mentalmente durante a tarefa
| Campo | Valor | Base | Confiança |
| --- | --- | --- | --- |
| Problema central | ... | fala usuário/documento | alta/média/baixa |
| Usuário e situação | ... | ... | ... |
| Jornada afetada | ... | ... | ... |
| Arquitetura e restrições | ... | ... | ... |
| Objetivo e métricas | ... | ... | ... |
| Lacunas e riscos | ... | não informado | baixa |

## Regras
- Preferir transições como `antes → durante → depois`, não apenas listas de telas.
- Reconstruir a intenção discutida no chat, mas não alucinar lembranças de outras conversas indisponíveis.
- Não bloquear toda a atividade esperando que o usuário detalhe persona, stack ou KPI; trabalhar com premissas explícitas.
- Perguntar somente se a lacuna impede ação segura/correta ou define escopo incompatível.
- Atualizar recomendações se o usuário mudar público, monetização ou restrição.
