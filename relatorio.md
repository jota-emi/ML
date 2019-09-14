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
O modelo utilizado para o desenvolvimento do algoritmo foi o Multilayer Perceptron (MLP), cuja estrutura deriva do Perceptron convencional. A arquitetura do MLP é baseada no próprio cérebro humano, inspirando-se em estruturas como dentritos e neurônios, formando assim as chamadas Redes Neurais Artificiais. Esse tipo de rede neural é constituída por pelo menos três camadas. A primeira delas é a camada de entrada, responsável por captar os dados iniciais e processa-los, aplicando atributos que chamamos de pesos, gerando assim como saída um número real para cada componente. Como toda rede neural está conectada, as saídas da camada de entrada serão utilizadas como entradas na segunda parte do modelo. O nível intermediário das MLPs se dá nas camadas escondidas, as quais recebem as saídas da camada inicial e repetem o seu procedimento, processando os dados e gerando novos valores. Ao final, os valores gerados nas camadas escondidas passam por uma regra de propagação, o que efetivamente classificará cada dado, gerando como resposta o resultado da previsão.   


* Explicar o modelo de _machine learning_ (ML) que você está trabalhando. 
* Explicar as etapas do treinamento e teste. 
* Caso tenha selecionado atributos, explicar a motivação para a seleção de tais atributos. 

## Códigos 

* Mostrar trechos de códigos mais importantes e explicações.  

## Experimentos 

* Descrever em detalhes os tipos de testes executados. 
* Descrever os parâmentros avaliados. 
* Explicar os resultados. 
