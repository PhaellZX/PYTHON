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

plt.scatter(featuresAll, targets, color='red', alpha =1.0)
plt.rcParams['figure.figsize'] = [10,8]
plt.title('Iris Dataset scatter Plot')
plt.xlabel('Features')
plt.ylabel('Targets')
plt.show()
