# Auditor Júnior — apresentação

- **Estado:** roteiro aprovado pelo usuário
- **Idioma:** português brasileiro
- **Público:** pessoas sem familiaridade com machine learning ou configuração de agentes
- **Formato assumido:** apresentação com participação guiada pelo apresentador (perguntas, escolhas e votação rápida); não depende de botões clicáveis no arquivo.
- **Objetivo:** explicar como uma pessoa cria, ensina, testa, acompanha e coloca em uso um agente de auditoria.
- **Direção visual aprovada:** explicador desenhado à mão com estrutura profissional em azul: fundo claro, diagramas de traço leve, hierarquia organizada, azul como cor principal e verde-azulado como acento; usar analogias visuais simples, manter respiro e variar a composição conforme a ideia de cada slide.
**Imagens de referência obrigatórias:** nenhuma.

## Slide 1 — Auditor Júnior: ensine o agente a seguir o seu padrão

- Uma aplicação self-service para criar agentes voltados a tarefas de auditoria.
- O usuário define o trabalho, fornece exemplos e escolhe como usar o agente.
- Promessa da apresentação: explicar o caminho do início ao uso, sem exigir conhecimento técnico.
- **Ideia visual / papel:** capa com uma trilha simples: definir → ensinar → testar → acompanhar → usar.
- **Interação:** abrir com a pergunta “Que tarefa de auditoria você gostaria de explicar uma vez e repetir com consistência?”.

## Slide 2 — Primeiro, escolha uma tarefa

- Um agente é um ajudante de software configurado para realizar uma tarefa delimitada.
- O usuário começa criando o agente e escolhendo o tipo de aplicação.
- Exemplos de tipo: Situação Monitorada e Classificação.
- A tarefa escolhida orienta o que entra e o que o agente deve entregar.
- **Ideia visual / papel:** explicação de conceito com uma tarefa no centro e os próximos passos ao redor.
- **Interação:** cada pessoa escolhe mentalmente uma tarefa repetitiva que gostaria de delegar.

## Slide 3 — Diga o que o agente deve fazer

- O usuário define a finalidade e o tipo de aplicação do agente.
- A configuração deixa explícito qual decisão ou análise deve ser feita.
- Uma boa definição evita instruções vagas como “analise tudo”.
- O agente precisa saber o que observar e qual formato de resposta é esperado.
- **Ideia visual / papel:** exemplo de antes e depois, de uma instrução vaga para uma instrução específica; exemplo didático, sem afirmar uma tela real do produto.
- **Interação:** escolher qual das duas instruções explica melhor a tarefa.

## Slide 4 — Mostre quais informações entram

- O usuário seleciona os tipos de entrada necessários ao trabalho.
- As entradas podem incluir arquivos, data-base e CNPJ.
- Cada tipo de aplicação pode precisar de informações diferentes.
- O agente usa esse contexto para produzir sua resposta.
- **Ideia visual / papel:** diagrama de entradas chegando a um agente, com ícones simples para arquivo, calendário e CNPJ.
- **Interação:** para uma tarefa hipotética, o público escolhe quais entradas seriam necessárias.

## Slide 5 — Ensine com exemplos do padrão ouro

- Para cada exemplo, o usuário mostra uma entrada e a saída que considera correta.
- Esses exemplos transformam “faça com qualidade” em um padrão observável.
- Exemplos variados ajudam a mostrar diferenças importantes entre casos.
- O conjunto de exemplos funciona como gabarito para comparar resultados.
- **Ideia visual / papel:** comparação lado a lado entre entrada, resposta do agente e resposta esperada, com um caso fictício.
- **Interação:** votação rápida sobre qual resposta segue melhor o padrão definido.

## Slide 6 — Melhorar o agente é ajustar suas instruções

- O sistema compara as respostas produzidas com os exemplos esperados.
- Com base nos erros, ajusta as instruções do agente para buscar respostas melhores.
- O ciclo é simples: observar → corrigir a orientação → avaliar de novo.
- O foco descrito aqui é otimizar as instruções do agente com exemplos, não treinar um modelo do zero.
- **Ideia visual / papel:** ciclo ilustrado de melhoria, sem números de desempenho inventados.
- **Interação:** o público sugere qual orientação faltou em uma resposta fictícia.

## Slide 7 — Validação cruzada: testar em exemplos diferentes

- Cross-validation, ou validação cruzada, é uma forma de testar o agente em partes diferentes dos exemplos.
- Alguns exemplos ajudam a orientar os ajustes; outros ficam reservados para testar.
- Ao alternar os grupos, fica mais fácil perceber se o agente generaliza para casos que não viu naquele ajuste.
- Analogia: estudar com exercícios e depois fazer provas com questões diferentes.
- **Ideia visual / papel:** sequência visual de grupos de exemplos alternando entre ajuste e teste.
- **Interação:** antes de revelar o próximo passo, o público escolhe quais exemplos deveriam ficar de fora do ajuste.

## Slide 8 — Acompanhe a qualidade com o passar do tempo

- Avaliar um agente não termina quando ele é criado.
- Acompanhamentos mostram se a qualidade se mantém ou se começa a cair.
- Mudanças nos dados ou nos tipos de caso podem revelar novas falhas.
- Os resultados ajudam a decidir quando revisar as instruções e os exemplos.
- **Ideia visual / papel:** linha do tempo com avaliações sucessivas e um ponto de atenção, sem sugerir alertas automáticos não especificados.
- **Interação:** observar dois momentos fictícios e apontar onde vale investigar uma queda.

## Slide 9 — Use o agente no fluxo de trabalho

- Depois de criado e otimizado, o agente pode ser usado pela interface do aplicativo.
- Também pode ser executado em horários definidos por agendamentos.
- Outros sistemas ou scripts podem chamar o agente pela API.
- O mesmo agente pode atender usos manuais e automatizados.
- **Ideia visual / papel:** um agente conectado a três caminhos: interface, agenda e API.
- **Interação:** o público escolhe qual caminho combina com três situações apresentadas pelo narrador.

## Slide 10 — Um ciclo claro: definir, ensinar, testar e acompanhar

- Defina o tipo de aplicação, a tarefa e as entradas.
- Mostre exemplos do padrão esperado.
- Ajuste as instruções e teste com validação cruzada.
- Acompanhe a qualidade e use o agente pela interface, por agendamento ou pela API.
- **Ideia visual / papel:** resumo visual da jornada em cinco etapas, fechando o ciclo do agente.
- **Interação:** cada pessoa escolhe uma tarefa pequena que seria um bom primeiro agente.
