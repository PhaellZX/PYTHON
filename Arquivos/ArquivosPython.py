# Como Criar e Modificar arquivos
valores_celular = [820, 2230, 1500, 3500, 5000]

'''
'r'  -> Usado somente para ler algo
'w'  -> Usado somente para escrever algo
'r+' -> Usado somente para ler e escrever algo
'a'  -> Usado somente para acrescentar algo
'''
'''
with open('valores_celulares.txt','w') as arquivo:  ESCREVENDO
    for valor in valores_celular:
        arquivo.write(str(valor) + '\n')
'''
'''
with open('valores_celulares.txt','a') as arquivo:  ADICIONANDO
    for valor in valores_celular:
        arquivo.write(str(valor) + '\n')
'''
'''
with open('valores_celulares.txt','r') as arquivo:  LENDO O ARQUIVO
    for valor in arquivo:
        print(valor)
'''
with open('valores_celulares.txt','r+') as arquivo:  # LENDO E ESCREVENDO
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')