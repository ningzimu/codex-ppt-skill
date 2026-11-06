## Slide 1: Auditor Júnior: ensine o agente a seguir o seu padrão

Hoje eu vou mostrar o Auditor Júnior como uma maneira de transformar uma tarefa de auditoria em um agente configurado para trabalhar de acordo com os exemplos e as instruções da própria equipe. Vou explicar essa jornada em linguagem simples, sem pressupor conhecimento prévio de programação ou machine learning.

Para começar: qual tarefa você gostaria de repetir com mais consistência? Guardem essa ideia; ao longo dos slides vamos passar pelas etapas de definir, ensinar, testar, acompanhar e usar o agente.

## Slide 2: Tudo começa com uma tarefa bem definida

Um agente é um ajudante de software preparado para fazer uma tarefa específica. No Auditor Júnior, a pessoa cria esse agente e escolhe o tipo de aplicação. Situação Monitorada e Classificação são dois exemplos.

Pensem numa tarefa que se repete na rotina de vocês. O agente não recebe uma missão vaga para “fazer auditoria”; ele é configurado para um trabalho delimitado. Essa escolha inicial também ajuda a decidir quais informações serão necessárias na etapa seguinte.

## Slide 3: Diga o que o agente deve fazer

Aqui vemos a diferença entre “Analise tudo” e “Classifique pelos critérios e explique a decisão”. A segunda instrução dá ao agente uma tarefa mais concreta. O exemplo é didático: a equipe precisaria fornecer os critérios que valem para o seu trabalho.

Vamos votar rapidamente: qual instrução orienta melhor? O objetivo é deixar claro o que observar e como apresentar o resultado. Depois, os exemplos ajudam a mostrar se a resposta está seguindo essa orientação.

## Slide 4: Mostre quais informações entram

O agente também precisa receber o contexto necessário para fazer o trabalho. Dependendo da tarefa, isso pode incluir arquivos, uma data-base ou um CNPJ. O usuário configura os tipos de entrada que fazem sentido para aquela aplicação.

Olhem os três exemplos no slide. Para a tarefa que vocês escolheram, quais informações seriam necessárias? Não existe uma lista única para todos os agentes; as entradas acompanham o trabalho definido.

## Slide 5: Ensine com exemplos do padrão ouro

Um exemplo padrão ouro junta uma entrada com a resposta que a equipe considera correta. Isso torna o padrão mais concreto do que simplesmente pedir “faça com qualidade”. A equipe fornece exemplos para mostrar tanto os casos comuns quanto as diferenças que importam.

Este caso do arquivo anexado é fictício. Vamos votar: A ou B? A resposta coerente com a entrada é “Arquivo recebido”. No uso real, a equipe é quem define qual saída está correta para cada situação; o exemplo serve para demonstrar como essa referência é apresentada.

## Slide 6: Melhorar o agente é ajustar suas instruções

A melhoria acontece em um ciclo: comparar a resposta com o padrão esperado, ajustar as instruções e avaliar de novo. Se o agente erra de uma forma recorrente, a orientação pode ser esclarecida para reduzir aquela ambiguidade.

No fluxo descrito para o Auditor Júnior, a otimização trabalha nas instruções do agente com base nos exemplos e nas avaliações. Não é necessário treinar um modelo do zero. A meta é buscar respostas mais alinhadas ao padrão definido, sem prometer que todos os erros desaparecerão.

## Slide 7: Validação cruzada: testar em exemplos diferentes

A validação cruzada é uma forma de usar os exemplos em rodadas diferentes. Em uma rodada, alguns ajudam no ajuste e outros ficam reservados para testar; depois, os grupos se revezam. Assim, verificamos também casos que não participaram daquele ajuste específico.

A analogia é estudar com exercícios e depois fazer uma prova com questões separadas. Isso ajuda a perceber se o agente está seguindo a regra geral ou apenas reproduzindo exemplos que acabou de ver. É uma avaliação mais cuidadosa, não uma garantia de que todo caso futuro será tratado corretamente.

## Slide 8: Acompanhe a qualidade ao longo do tempo

A avaliação continua depois que o agente é criado. Com o passar do tempo, novas avaliações ajudam a observar se a qualidade se mantém ou se começa a cair. O slide mostra duas possibilidades ilustrativas e não representa uma métrica real do produto.

Se aparecer uma queda, a próxima pergunta é o que mudou: os casos, os dados ou o padrão esperado? A equipe pode investigar e revisar as instruções e os exemplos quando necessário. Acompanhar a qualidade ajuda a perceber quando vale reavaliar o agente.

## Slide 9: Use o agente no fluxo de trabalho

Depois de criado e otimizado, o agente pode ser utilizado pela interface do aplicativo. Também pode ser executado em horários definidos por agendamentos, ou chamado por outros sistemas e scripts por meio de uma API.

Pensem em três situações: alguém inicia uma análise manualmente; uma tarefa precisa rodar em um horário combinado; ou outro sistema precisa solicitar uma análise. Qual caminho combina com cada situação? A ideia é escolher a forma de uso que se encaixa no fluxo da equipe.

## Slide 10: Um ciclo claro: definir, ensinar, testar e acompanhar

Vamos recapitular: escolhemos o tipo de aplicação e as entradas, mostramos exemplos do padrão esperado, ajustamos as instruções, testamos com validação cruzada e acompanhamos a qualidade. Quando o agente está pronto, podemos usá-lo pela interface, por agendamentos ou pela API.

Para fechar, escolham uma tarefa pequena que seria um bom primeiro agente. Começar com um escopo claro e exemplos úteis dá à equipe uma base concreta para avaliar o resultado e decidir os próximos passos.
