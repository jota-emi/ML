# Agrupamento e análise de perfil de alunos com rede SOM   

## Introdução
Este trabalho foi desenvolvido por João Marcos Viana Silva, com orientação do prof. Orivaldo Santana. 
A atividade tinha como objetivo analisar a relação existente (ou não) entre a quantidade de questões submetidas por um aluno da disciplina de Lógica de Programação, ministrada na Escola de Ciências e Tecnologia da UFRN, e sua aprovação ou reprovação ao final do semestre. Com isso, seria possível traçar o perfil do aluno e orientá-lo para melhor desempenho na disciplina, além de conseguir uma análise mais efetiva sobre o real impacto que a submissão de questões pelo sistema LOP tem numa eventual aprovação. 
A base de dados utilizada possui 947 entradas, foi gerada e disponibilizada pelo professor e equipe do Sistema LoP, 
nela estão contidas dezenas de atributos relacionados a quantidade de questões submetidas a cada semana pelos alunos que cursaram a disciplina no período entre 2017 e 2019, assim como sua a situação final.

## Metodologia 
O modelo utilizado para o desenvolvimento do algoritmo foi o Self-Organizing Map (SOM), que também pode ser chamado de Mapa de Kohonen, sendo uma rede neural de aprendizagem não-supervisionada. Isto é, a rede não leva em consideração uma saída pré-estabelecida, tendo assim como objetivo analisar as entradas e encontrar padrões entre elas, agrupando-as em grupos com características comuns, o que chamamos de Clusters. As redes do tipo SOM possuem duas camadas em sua estrutura, a primeira delas é a de entrada, responsável por captar os dados iniciais, que podem ter N-dimensões, e aplicando neles atributos matemáticos que chamamos de pesos. A partir disso, o algoritmo irá fazer um mapeamento daqueles dados, formando a segunda camada, ou camada de saída. Esse mapa é basicamente uma matriz, com duas dimensões, onde cada posição representa um grupo de dados similares, ou seja, o algoritmo processa os dados da camada de entrada, procurando padrões, e os posiciona em um índice. A idéia é que os neurônios que estão mais próximos uns dos outros tenham respostas parecidas para entradas semelhantes. Depois, o processo é repetido diversas vezes, enquanto o algoritmo vai ajustando seus pesos e encontrando o índice "vencedor" para cada dado 


A rede SOM é uma rede neural de 2 camadas que aceita padrões de N-dimensões como entrada e os mapeia para um conjunto de neurônios de saída, o qual representa o espaço dos dados a serem agrupados. O mapa (camada) de saída, que é tipicamente bi-dimensional, representa as posições dos neurônios em relação aos seus vizinhos. A idéia é que neurônios topologicamente próximos respondam de maneira semelhante a entradas semelhantes. Para isso todos neurônios da camada de entrada são todos conectados aos neurônios de saída.





A primeira delas é a camada de entrada, responsável por captar os dados iniciais e processa-los, aplicando atributos que chamamos de pesos, gerando assim como saída um número real para cada componente. Como toda rede neural está conectada, as saídas da camada de entrada serão utilizadas como entradas na segunda parte do modelo. O nível intermediário das MLPs se dá nas camadas escondidas, as quais recebem as saídas da camada inicial e repetem o seu procedimento, processando os dados, corrigindo os pesos e gerando novos valores. Ao final, os valores gerados nas camadas escondidas passam por uma regra de propagação, o que efetivamente classificará cada dado, gerando como resposta o resultado da previsão.   

A cada interação dos dados com as camadas o algoritmo vai tentanto corrigir os erros e ajustar os pesos para aproximar cada vez mais o valor daquele considerado o ideal, que representa a classe do qual ele pertence. Sendo assim, é necessário que a rede neural interaja com uma série de dados antes de ser capaz de realizar sua previsão mais embasada. Esse processo é chamado de treinamento. Somente após isso, o algoritmo estará hábil para realizar os testes, onde classificará dados que não teve contato previamente, checando assim sua acurácia.
Para nossa atividade 75% dos dados foram usados para o treinamento da rede neural, enquanto os 25% restantes foram reservados para os testes.

Devido a imensa quantidade de dados e atributos na base de dados do sistema LoP, fez-se necessário realizar uma espécie de filtragem manual, selecionando um grupo de atributos que julgamos ter mais influência na previsão. Assim, o processo se torna mais rápido e mais eficiente, já que o algoritmo não precisa analisar dados que podem não ter influência alguma na aprovação ou não do aluno. Além disso, o objetivo do trabalho é ter um diagnóstico para o aluno já na primeira unidade, enquanto ainda há tempo para uma mudança de postura. Então, não é viável utilizar dados referentes a metade final do semestre.

Após uma série de testes, os atributos que mais se mostraram relevantes foram:
* **notaProva1** - Referente a nota do aluno na primeira prova;
* **igualACeml123** - Quantidade de submissões em que o aluno atingiu 100% de acerto;
* **subListaExer45** - Quantidade de submissões do aluno nas listas de exercícios durante as semanas 4 e 5.

Analisando tais atributos, podemos concluir que a nota da primeira prova é o mais forte indicador do desempenho do aluno, seguido pela quantidade de quetões certas nas primeiras listas, o que indica que alunos com mais acertos nas listas tendem a ter melhor desempenho. Por fim, a quantidade de submissões durante a quarta e quinta semanas, geralmente o período da primeira avaliação, revela o quanto o aluno está se preparando.

## Códigos 
A atividade foi desenvolvida integralmente na linguagem Python, utilizando as bibliotecas Pandas e Keras.

* <h3>Seleção de atributos</h3>
~~~ python
#notaProva1
#igualACem123
#subListaExer45
X = dataset.iloc[:,[2,20,48]].values
y = dataset.iloc[:, 11].valuesse( activation = 'relu', units = 6, kernel_initializer = 'uniform' ))
~~~
As colunas 2,20 e 48 correspondem respectivamente a notaProva1, igualACeml123 e subListaExerc45.

* <h3> Separação Treinamento/Teste</h3>
~~~ python
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
~~~
25% dos dados reservados para a fase de testes.
* <h3> Criação das Camadas</h3>
~~~ python
#Adicionando a camada de entrada e a primeira camada escondida
classifier.add(Dense( activation = 'relu', input_dim = 3, units = 3, kernel_initializer = 'uniform'))

#Adicionando segunda camada escondida
classifier.add(Dense( activation = 'relu', units = 6, kernel_initializer = 'uniform' ))

#Adicionando camada de saída
classifier.add(Dense( activation = 'sigmoid', units = 1, kernel_initializer = 'uniform'))
~~~
Acima podemos ver que foram usadas três atributos para entrada (**input_dim = 3**), e três neurônios na camada (**units = 3**).
Já na segunda camada escondida, seis neurônios foram setados, enquanto a camada de sáida é formada pela propagação 'sigmoid'.

* <h3>Treinamento</h3>
~~~ python
# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 60)
~~~
O treinamento foi realizado em 60 épocas, ou seja, repetido 60 vezes, enquanto o **batch_size = 10**

## Experimentos 
* <h3>Matriz de Confusão</h3>
~~~ python
Matriz de Confusão:
[[43  7]
 [13 49]]
Taxa de acerto:
0.8214285714285714
112
~~~
A matriz de confusão representa a quantidade de valores para os quais o algoritmo obteve um resultado de **43 Verdadeiros Positivos e 49 Verdadeiros Negativos**, correspondentes aos acertos e **7 Falsos Positivos e 13 Falsos Negativos**, totalizando uma taxa de acerto de **82%**  

Com isso, o resultado obtido pela rede neural baseada em MLP com os parâmetros utilizados pode ser considerado satisfatório. O valor de 82% não é tão considerável quanto poderia ser. Entretanto, considerando o ruído da base de dados aliado a complexidade do problema, torna o resultado bom, capaz de dar um diagnóstico rápido para o aluno. Além disso, vários valores diferentes foram testados para as variáveis do modelo, concluindo assim que a quantidade de épocas e neurônios utilizada foi mais eficente.

