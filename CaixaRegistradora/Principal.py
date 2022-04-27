from Classes import *
from Menu import menu
from time import sleep

car = Carrinho()
contCod = 0
while True:
    menu()
    opcao = int(input())
    if opcao == 1:
        nome = str(input('Digite o nome de produto: '))
        preco = float(input('Digite o preço do produto: '))
        prd = Produto(contCod, nome, preco)
        car.inserir_produto(prd)
        contCod += 1
        print('PRODUTO ADICIONADO NO CARRINHO!\n')
    elif opcao == 2:
        car.mostrar_produto()
        codigo = int(input('Digite o código do produto: '))
        car.remover_produto(codigo)
    elif opcao == 3:
        car.mostrar_produto()
    elif opcao == 0:
        print('Finalizando compras...')
        sleep(2)
        car.gerar_Nota()
        print('Volte Sempre! :)')
        break
    else:
        print('\nValor Inválido!!\n')

