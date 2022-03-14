from sklearn import tree
# Apredizado Supersionado
# Obs: o sklearn não trabalha com strings, só com inteiros
lisa = 1
irregular = 0
maca = 1
laranja = 0
pomar = [[150,lisa],[130,lisa],[180,irregular],[160,irregular]]
resultado = [maca,maca,laranja,laranja]

classificador = tree.DecisionTreeClassifier() # Busca por arvore
classificador = classificador.fit(pomar, resultado) # Fazer ánalise
peso = input('Entre com o peso: ')
superficie = input('Entre com a superficie: (1 - lisa/ 0 - irregular)')

resultadoUsuario = classificador.predict([[peso, superficie]])

if resultadoUsuario == 1:
    print('É uma maçã')
else:
    print('É uma laranja')