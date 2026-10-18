# UX Reverse Engineering

**Engenharia reversa de experiências digitais, contextualizada para o produto que você está construindo.**

Skill de inteligência de produto, UX research e implementação para **Claude Code**, **OpenAI Codex** e distribuição por **plugin ChatGPT**. Parte do contexto do chat e do repositório, encontra oportunidades na jornada, pesquisa apps com experiências comparáveis, reconstrói os mecanismos possíveis e entrega soluções originais, técnicas, éticas e mensuráveis.

> **Não é um catálogo de screenshots nem um prompt para copiar concorrentes.** É um método operacional para transformar boas experiências observáveis em princípios transferíveis, com evidências, limites e testes.

## O que faz

1. **Entende o projeto:** resgata público, JTBD, metas, fluxos existentes, stack e decisões do histórico e do código.
2. **Detecta oportunidades:** aponta gargalos de ativação, engajamento, retenção, conversão, confiança e acessibilidade.
3. **Pesquisa referências:** benchmarks diretos e cross-industry por **problema comportamental**, não só concorrência.
4. **Faz engenharia reversa:** gatilhos, elegibilidade, microinterações, feedback, lógica hipotética, estados e exceções.
5. **Traduz para o projeto:** cria uma solução original aderente a negócio, recursos, usuário e design system.
6. **Especifica e valida:** fluxos, contratos técnicos, testes, eventos, hipóteses, métricas, privacidade e experimentos.

### Casos que inspiraram o método

| Produto | Mecanismo investigado | O que podemos reaproveitar, sem copiar |
| --- | --- | --- |
| Duolingo | Retorno, progresso, hábito e reengajamento | Relevância contextual, metas conscientes, feedback de progresso e controles de notificação |
| iFood | Proposta de valor no contexto, benefícios e feedback | Clareza sobre valor, momento da decisão e convite honesto para avaliar a experiência |

**Nota de rigor:** exemplos provenientes dos vídeos são ilustrativos. A skill não presume acesso a código interno ou comprova impacto causal de terceiros. Distingue comportamento observado, documentação pública, inferências e desconhecidos.

## Como instalar

O projeto mantém três entradas nativas, geradas do mesmo material de referência:

| Plataforma | Caminho pronto no repositório | Uso |
| --- | --- | --- |
| Claude Code | `.claude/skills/ux-reverse-engineering/` | Copiar para projeto ou `~/.claude/skills/`; pode usar `/ux-reverse-engineering` |
| Codex | `.agents/skills/ux-reverse-engineering/` | Copiar para projeto ou local de skills suportado pelo seu Codex |
| Plugin ChatGPT/Codex | `.codex-plugin/plugin.json` + `skills/ux-reverse-engineering/` | Base de pacote de plugin; disponibilização/instalação dependem do produto e permissões |

**Instalação por projeto, Claude Code:**

```bash
mkdir -p /caminho/do/seu-projeto/.claude/skills
cp -R .claude/skills/ux-reverse-engineering /caminho/do/seu-projeto/.claude/skills/
```

**Instalação por projeto, Codex:**

```bash
mkdir -p /caminho/do/seu-projeto/.agents/skills
cp -R .agents/skills/ux-reverse-engineering /caminho/do/seu-projeto/.agents/skills/
```

**Pacotes ZIP individuais:** após `python3 scripts/build.py --zip`, consulte `dist/`. A pasta única `ux-reverse-engineering/` é portátil e pode ser distribuída pelos canais que aceitam upload de skills; o ZIP de plugin inclui manifesto e pasta `skills/`.

Veja instruções detalhadas, inclusive comandos Windows, em [`docs/installation.md`](docs/installation.md). Para ChatGPT comum, a disponibilidade de instalação direta de uma skill ou plugin depende dos recursos da conta e do canal; este repositório **não instala automaticamente** um plugin na sua conta.

## Utilização

A skill pode ser detectada automaticamente no contexto de UX, ou invocada explicitamente:

```text
/ux-reverse-engineering
Estou implementando o primeiro acesso de um app de educação. Descubra como apps de referência resolvem a ativação e proponha um fluxo adequado à nossa stack.
```

```text
Use a skill UX Reverse Engineering em modo profundo.
Analise nosso checkout, pesquise 3 referências, explique mecanismos verificáveis e entregue a especificação com edge cases, acessibilidade e eventos.
```

```text
Use a skill UX Reverse Engineering em modo implementação.
Inspecione este repositório, compare o fluxo de notificações com padrões relevantes e implemente apenas a alternativa consentida e mensurável, com testes.
```

Modos: `rápido` para questão pontual, `profundo` para dossiê comparativo, `auditoria` para fluxo existente e `implementação` quando autorizado editar arquivos. Na ausência de web/navegador, entrega hipóteses claramente rotuladas, sem inventar pesquisa.

## O que a skill entrega

- Cartão de contexto e mapa de oportunidades priorizadas.
- Matriz de 3 a 5 benchmarks, com fonte e nível de confiança quando possível.
- Engenharia reversa dos 2 a 3 benchmarks mais relevantes (modo profundo).
- Princípio de UX transferível, riscos e adaptação criativa.
- User journey, wireflow textual, máquina de estados, microcopy e acessibilidade.
- Especificação de UI/API/dados/eventos, critérios de aceite e plano de rollout.
- Hipótese, métrica principal, guardrails e desenho de experimento.

## Arquitetura

```text
ux-reverse-engineering/
├── .claude/skills/ux-reverse-engineering/  # Claude Code, autossuficiente
├── .agents/skills/ux-reverse-engineering/  # Codex, autossuficiente
├── .codex-plugin/plugin.json              # manifesto plugin ChatGPT/Codex
├── skills/ux-reverse-engineering/         # Skill no bundle do plugin
├── source/
│   ├── platforms/                         # Entradas SKILL.md específicas
│   ├── references/                        # 13 protocolos compartilhados
│   └── templates/                         # 6 modelos de saída, evidência e decisão
├── docs/                                  # instalação, avaliação, ética
├── examples/                              # cenários e resultados ilustrativos
├── scripts/build.py                       # compilação e ZIPs
├── scripts/validate.py                    # validação, integridade e sincronização
├── tests/                                  # testes automatizados
└── .github/workflows/validate.yml         # CI para bundles
```

As três distribuições são autocontidas: todos os `references/` e `templates/` necessários estão dentro da própria pasta da skill. A fonte única evita divergência. **Não edite as cópias geradas manualmente; edite `source/` e execute o build.**

## Segurança, rigor e ética

- Nunca afirmar acesso a algoritmos, dados internos ou código proprietário de apps de terceiros.
- Guardar rastro de fontes e status: `observado`, `documentado`, `inferido`, `desconhecido`.
- Não transformar popularidade em evidência causal de sucesso.
- Não copiar identidade visual, microcopy protegida, conteúdo de telas ou designs exatos.
- Não incentivar FOMO enganoso, manipulação de avaliações, bloqueio de cancelamento, custos ocultos ou notificações abusivas.
- Evitar vazamento de PII, secrets e dados privados em pesquisas externas.
- UX acessível, reversível, com opt-out e feedback útil por padrão.

Saiba mais em [`docs/methodology.md`](docs/methodology.md) e [`docs/quality-rubric.md`](docs/quality-rubric.md).

## Desenvolver e validar

Requer **Python 3.10+**, sem bibliotecas de terceiros:

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build.py --zip
```

O CI executa validação e testes a cada push/PR. Os pacotes ZIP são artefatos locais e não precisam entrar no versionamento.

Para publicar na sua conta do GitHub, consulte `docs/installation.md` ou use `./scripts/publish-github.sh ux-reverse-engineering --private` com GitHub CLI autenticado. O script não é executado automaticamente.

## Limites

Isto é uma skill baseada em instruções e arquivos, **não** um serviço de crawling, banco de dados de interfaces ou agente em execução contínua. O acesso a pesquisas atuais, imagens, navegador, código e execução depende das ferramentas e permissões do ambiente que a hospeda. A qualidade da avaliação depende da evidência obtida e de dados do produto. Não há garantia de melhoria de KPI sem validação real.

## Referências oficiais

- [Agent Skills (formato aberto)](https://agentskills.io/)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Plugins: Skills](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI Plugins: Package](https://developers.openai.com/api/docs/guides/agents-api/tools/plugins)

## Licença

MIT. Consulte [LICENSE](LICENSE). Contribuições: [CONTRIBUTING.md](CONTRIBUTING.md).
