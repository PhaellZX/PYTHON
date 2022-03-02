from random import choice
nome1 = str(input('Digite o nome do 1° aluno(a): '))
nome2 = str(input('Digite o nome do 2° aluno(a): '))
nome3 = str(input('Digite o nome do 3° aluno(a): '))
nome4 = str(input('Digite o nome do 4° aluno(a): '))
aluno = [nome1, nome2, nome3, nome4]
print(f'O aluno escolhido para apagar o quadro negro foi {choice(aluno)}')
