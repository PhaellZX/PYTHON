from sklearn import datasets
iris = datasets.load_iris()
print('Iris')
print(f'tipo de váriavel-> {type(iris)}')
print('Cada linha é uma observação (também conhecida como: amostra, exemplo, instância, registro)\n'
      'Cada coluna é um recurso (também conhecido como: feature, preditor, atributo, variável\n'
      'independente, entrada, regressor, covariável).')
print(iris.data)
print(f'nomes dos quatro recursos (features)-> {iris.feature_names}')
print(f'classes alvo da classificação-> {iris.target_names}')
print(f' a seguir imprime inteiros representando as espécies de cada observação: 0, 1 e 2 representam espécies diferentes-> {iris.target}')
print(f'Verifique os tipos de recursos e resposta-> {type(iris.data)}') # Ou type(iris.target)
print(f'Verifique o formato das features ( primeira dimensão = número de observações, segunda dimensão = número de features )-> {iris.data.shape}')
print(f'Verifique o formato da resposta (dimensão única correspondente ao número de observações) {iris.target.shape}')
print('Armazena a matriz de recurso (feature) em “x”')
x = iris.data
print('Armazena o vetor de resposta em “y”')
y = iris.target
print(f' X -> {x}')
print()
print(f' Y -> {y}')
