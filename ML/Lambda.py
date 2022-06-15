# LAMBDA

soma = lambda a, b : a + b
subtrair = lambda  a, b : a - b
multiplicar = lambda  a, b : a * b
dividir = lambda a, b : a / b

print('1 - SOMA\n'
      '2 - SUBTRAÇÃO\n'
      '3 - MULTIPLICAÇÃO\n'
      '4 - DIVISÃO\n'
      '(qualquer número) - SAIR')

opcao = int(input('Escolha uma das opções: '))

if opcao == 1:
    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Digite o 2° número: '))

    print()
    print(f'RESULTADO DA SOMA: {soma(n1,n2):.2f}')
elif opcao == 2:
    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Digite o 2° número: '))

    print()
    print(f'RESULTADO DA SUBTRAÇÃO: {subtrair(n1, n2):.2f}')
elif opcao == 3:
    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Digite o 2° número: '))

    print()
    print(f'RESULTADO DA MULTIPLICAÇÃO: {multiplicar(n1, n2):.2f}')
elif opcao == 4:
    n1 = float(input('Digite o 1° número: '))
    n2 = float(input('Digite o 2° número: '))

    print()
    print(f'RESULTADO DA DIVISÃO: {dividir(n1, n2):.2f}')
else:
    print('bye... :)')