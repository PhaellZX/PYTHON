from random import shuffle
nome1 = str(input('Digite o nome do 1° aluno(a): '))
nome2 = str(input('Digite o nome do 2° aluno(a): '))
nome3 = str(input('Digite o nome do 3° aluno(a): '))
nome4 = str(input('Digite o nome do 4° aluno(a): '))
aluno = [nome1, nome2, nome3, nome4]
shuffle(aluno)
print(f'Ordem de apresentação: {aluno}')