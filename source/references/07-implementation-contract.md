# 07 | Contrato de implementação UX + engenharia

## A entrega não é um screenshot
Um fluxo completo deve especificar intenção, transições, contrato de UI, fontes de dados, permissões, logging, edge cases, accessibility, feedback, observabilidade e critérios de aceite. Ajustar ao stack inspecionado. Não introduzir dependências sem justificativa e aprovação pertinente.

## Estrutura de especificação
1. **Objetivo da feature e escopo:** problema, personas, não objetivos, definição de sucesso.
2. **User stories / jobs:** situação, ação, resultado desejado; restrições.
3. **Fluxo principal:** navegação e estados em sequência, com passos do usuário e respostas do sistema.
4. **Máquina de estados:** `idle → eligible → prompted → dismissed/accepted → completed/failed`; transições de retry, expiração, bloqueios.
5. **Regras de negócio:** tabela `condição | ação | fallback | risco`.
6. **Interface:** hierarquia, microcopy inclusiva, CTAs, labels, acessibilidade, estados e padrões do design system.
7. **Contrato de dados:** entidades, validações, TTL, timezone, consentimentos, migração e fontes de verdade.
8. **Eventos de analytics:** nome, definição, ator, contexto não sensível, exposição, denominador e idempotência.
9. **Políticas:** opt-in/opt-out, limites de frequência, preferência, retenção, privacidade, exclusão.
10. **Testes:** unitário, integração, e2e, acessibilidade, rede lenta, offline, localização, rollback.
11. **Release:** feature flag, segmento elegível, monitoramento, rollback, suporte e documentação.

## Biblioteca de estados e edge cases
- Primeiro acesso; não elegível; permissão negada; retorno após pausa; dado ausente/desatualizado; ação duplicada; stale response; navegação para trás; sessão expirada; multiplataforma.
- Loading progressivo, skeleton só quando ajuda; vazio útil; erro recuperável; reenvio idempotente; latência e offline honestos; timeout.
- Custo visível, opções predefinidas não enganosas, reversibilidade, confirmação em ações destrutivas, mensagens acessíveis.
- Teclado, foco, contraste, reduzido movimento, nomes acessíveis, leitor de tela, alvos de toque adequados, idioma/RTL quando aplicável.

## Modelo de analytics exemplificativo (não impor valores)
```
ux_exposure: {feature_id, variant, entry_point, occurred_at}
ux_action: {feature_id, action, variant, occurred_at}
ux_outcome: {feature_id, outcome, duration_bucket, occurred_at}
ux_preference_change: {feature_id, preference_kind, new_state, occurred_at}
```
Evitar nome, e-mail, telefone, texto livre sensível ou dados financeiros pessoais no evento. Determinar requisitos de LGPD e minimização de dados para o projeto.

## Critérios de aceite mínimos
- Dado um usuário não elegível, não renderizar estímulo inadequado.
- Dado opt-out explícito, não reativar por padrão e respeitar preferências nos demais dispositivos.
- Dada falha de rede, mostrar estado real e opção apropriada de retry; nenhuma cobrança ou ação duplicada.
- Dada variação de texto e acesso por teclado/leitor de tela, toda ação permanece compreensível.
- Dada intervenção, logging registra exposição e desfecho sem violar privacidade.
- A experiência preserva consistência com o design system e internacionalização do projeto.

## Quando codificar
Somente se o usuário pedir implementação (ou sua solicitação implicar claramente edição de projeto). Antes de editar: inspecionar arquivos, plano de mudança, pontos de teste, regressões. Depois: executar lint/test/build disponíveis e declarar exatamente o que foi/ não foi verificado. Nunca alegar execução fictícia de testes ou deploy.
