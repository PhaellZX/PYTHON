#Plotando um gráfico de dispersão
import matplotlib.pyplot as plt
#Importa os datasets que vem com o scikit learn
from sklearn import datasets

#Guarda na variável iris o dataset iris
iris = datasets.load_iris()

#Armazena a matriz de recurso (feature) em "x"
features = iris.data[: , [0,1,2,3]]
print(features)

#Armazena o vetor de resposta em "y"
targets = iris.target
print(targets)

featuresAll = [] # Lista que pega os dados de cada posição e soma
for observation in features:
    featuresAll.append([observation[0] + observation[1] + observation[2] + observation[3]])
print(featuresAll)

#Encontrando o relacionamento entre o comprimento e a largura da pétala
petal_len = []
petal_width = []
for feature in features:
    petal_len.append(feature[2]) #Comprimento da pétala
    petal_width.append(feature[3]) #Largura da pétala

groups = ('Iris-setosa','Iris-versicolor','Iris-virginica')
colors = ('blue', 'green','red')
data = ((petal_len[:50], petal_width[:50]), (petal_len[50:100], petal_width[50:100]),
        (petal_len[100:150], petal_width[100:150]))

for item, color, group in zip(data,colors,groups):
    #item = (petal_len[:50], petal_width[:50]), (petal_len[50:100], petal_width[50:100]),
    #(petal_len[100:150], petal_width[100:150])
    x0, y0 = item
    plt.scatter(x0, y0,color=color,alpha=1)
    plt.title('Iris Dataset scatter Plot')

plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.show()