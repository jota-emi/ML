# Utilização de SVM para classificar a posição de um individuo a partir de imagens 

## Introdução
Este trabalho foi desenvolvido por João Marcos Viana Silva, com orientação do prof. Orivaldo Santana. 
A atividade tinha como objetivo desenvolver um algoritmo capaz de classificar em duas categorias (em pé ou sentado) a posição em que uma pessoa estava em uma foto. Tal classificação abre o caminho para resolução de diversos tipos de problemas, como por exemplo, controle de equipamentos a partir de gestos, uso em videogames ou qualquer outro contexto que análise de posição seja importante. Além disso, a atividade exigiu a criação de uma base de dados própria, processo que é importante na ciência de dados em geral, proporcionando um conhecimento e preparo extra ao aluno. Sendo assim, a base foi gerada a partir de frames de um vídeo produzido pelo autor, aplicadas a uma API do TensorFlow chamada PoseEstimation, capaz de extrair as posições em pixels de onde estariam cada parte do corpo da pessoa na imagem. Ao final, a base continha 64 imagens, em que em 50% delas o individuo estava em pé e nos outros 50% estava sentado. 

## Metodologia
O modelo utilizado para o desenvolvimento do algoritmo foi o Support Vector Machine (SVM). EXPLICAR SVM

No nosso caso, o processamento dos dados foi feito da seguinte forma, cada imagem possuia atributos correspondentes as posições X e Y de cada parte do corpo utilizada pelo PoseEstimation, são elas:

* Nariz;
* Olho esquerdo;
* Olho direito;
* Orelha esquerda;
* Orelha direita;
* Ombro esquerdo;
* Ombro direito;
* Cotovelo esquerdo;
* Cotovelo direito;
* Pulso esquerdo;
* Pulso direito;
* Quadril esquerdo;
* Quadril direito;
* Joelho esquerdo;
* Joelho direito;
* Tornozelo esquerdo;
* Tornozelo direito.

Para o treinamento do algoritmo foram reservadas cerca de 75% das imagens geradas. Ou seja, 3/4 das imagens foram utilizadas para que o algoritmo pudesse compará-las e encontrar padrões entre os atributos de cada uma das classificações. Sendo assim, os 30% restantes foram usandos na fase de testes, em que a SVM recebe novos dados e faz a previsão dos mesmos, podendo acertar ou errar.
## Códigos 

* Mostrar trechos de códigos mais importantes e explicações.  

## Experimentos 

* Descrever em detalhes os tipos de testes executados. 
* Descrever os parâmentros avaliados. 
* Explicar os resultados. 
