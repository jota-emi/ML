# Previsão de aprovação de alunos usando MLP 

## Introdução
Este trabalho foi desenvolvido por João Marcos Viana Silva, com orientação do prof. Orivaldo Santana. 
A atividade tinha como objetivo conseguir prever logo nas primeiras semanas, com uma margem considerável de aceitação, 
a aprovação ou não de um aluno da disciplina de Lógica de Programação, ministrada na Escola de Ciências e Tecnologia da UFRN.
Com isso, seria possível orientar melhor os alunos em situação crítica, para que o prognóstico possa ser revertido, 
além de conseguir uma análise mais efetiva sobre quais atributos do aluno mais impactam numa eventual aprovação. 
A base de dados utilizada foi gerada e disponibilizada pelo professor e equipe do Sistema LoP, 
nela estão contidas dezenas de atributos relacionados a resolução de questões por parte dos alunos que cursaram a disciplina no período entre 2017 e 2019, como quantidade e notas.

## Metodologia 
O modelo utilizado para o desenvolvimento do algoritmo foi o Multilayer Perceptron (MLP), cuja estrutura deriva do Perceptron convencional. A arquitetura do MLP é baseada no próprio cérebro humano, inspirando-se em estruturas como dentritos e neurônios, formando assim as chamadas Redes Neurais Artificiais. Esse tipo de rede neural é constituída por pelo menos três camadas. A primeira delas é a camada de entrada, responsável por captar os dados iniciais e processa-los, aplicando atributos que chamamos de pesos, gerando assim como saída um número real para cada componente. Como toda rede neural está conectada, as saídas da camada de entrada serão utilizadas como entradas na segunda parte do modelo. O nível intermediário das MLPs se dá nas camadas escondidas, as quais recebem as saídas da camada inicial e repetem o seu procedimento, processando os dados, corrigindo os pesos e gerando novos valores. Ao final, os valores gerados nas camadas escondidas passam por uma regra de propagação, o que efetivamente classificará cada dado, gerando como resposta o resultado da previsão.   

A cada interação dos dados com as camadas o algoritmo vai tentanto corrigir os erros e ajustar os pesos para aproximar cada vez mais o valor daquele considerado o ideal, que representa a classe do qual ele pertence. Sendo assim, é necessário que a rede neural interaja com uma série de dados antes de ser capaz de realizar sua previsão mais embasada. Esse processo é chamado de treinamento. Somente após isso, o algoritmo estará hábil para realizar os testes, onde classificará dados que não teve contato previamente, checando assim sua acurácia.
Para nossa atividade 75% dos dados foram usados para o treinamento da rede neural, enquanto os 25% restantes foram reservados para os testes.

Devido a imensa quantidade de dados e atributos na base de dados do sistema LoP, fez-se necessário realizar uma espécie de filtragem manual, selecionando um grupo de atributos que julgamos ter mais influência na previsão. Assim, o processo se torna mais rápido e mais eficiente, já que o algoritmo não precisa analisar dados que podem não ter influência alguma na aprovação ou não do aluno. Além disso, o objetivo do trabalho é ter um diagnóstico para o aluno já na primeira unidade, enquanto ainda há tempo para uma mudança de postura. Então, não é viável utilizar dados referentes a metade final do semestre.

Após uma série de testes, os atributos que mais se mostraram relevantes foram:
* **notaProva1** - Referente a nota do aluno na primeira prova;
* **igualACeml123** - Quantidade de submissões em que o aluno atingiu 100% de acerto;
* **subListaExer45** - Quantidade de submissões do aluno nas listas de exercícios durante as semanas 4 e 5;
Analisando tais atributos, podemos concluir que a nota da primeira prova é o mais forte indicador do desempenho do aluno, seguido pela quantidade de quetões certas nas primeiras listas, o que indica que alunos com mais acertos nas listas tendem a ter melhor desempenho. Por fim, a quantidade de submissões durante a quarta e quinta semanas, geralmente o período da primeira avaliação, revela o quanto o aluno está se preparando.

## Códigos 

* Mostrar trechos de códigos mais importantes e explicações.  

## Experimentos 

* Descrever em detalhes os tipos de testes executados. 
* Descrever os parâmentros avaliados. 
* Explicar os resultados. 
