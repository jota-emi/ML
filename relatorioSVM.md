# Utilização de SVM para classificar a posição de um individuo a partir de imagens 

## Introdução
Este trabalho foi desenvolvido por João Marcos Viana Silva, com orientação do prof. Orivaldo Santana. 
A atividade tinha como objetivo desenvolver um algoritmo capaz de classificar em duas categorias (em pé ou sentado) a posição em que uma pessoa estava em uma foto. Tal classificação abre o caminho para resolução de diversos tipos de problemas, como por exemplo, controle de equipamentos a partir de gestos, uso em videogames ou qualquer outro contexto que análise de posição seja importante. Além disso, a atividade exigiu a criação de uma base de dados própria, processo que é importante na ciência de dados em geral, proporcionando um conhecimento e preparo extra ao aluno. Sendo assim, a base foi gerada a partir de frames de um vídeo produzido pelo autor, aplicadas a uma API do TensorFlow chamada PoseEstimation, capaz de extrair as posições em pixels de onde estariam cada parte do corpo da pessoa na imagem. Ao final, a base continha 46 imagens, em que em 50% delas o individuo estava em pé e nos outros 50% estava sentado. 

## Metodologia

O modelo utilizado para o desenvolvimento do algoritmo foi o Multilayer Perceptron. Esse 
* Explicar o modelo de _machine learning_ (ML) que você está trabalhando. 
* Explicar as etapas do treinamento e teste. 
* Caso tenha selecionado atributos, explicar a motivação para a seleção de tais atributos. 

## Códigos 

* Mostrar trechos de códigos mais importantes e explicações.  

## Experimentos 

* Descrever em detalhes os tipos de testes executados. 
* Descrever os parâmentros avaliados. 
* Explicar os resultados. 
