from Classes import *
from Menu import menu

lp = Lista_Professor()
la = Lista_Aluno()
mat_p = 1
mat_a = 1
while True:
    menu()
    opcao = int(input())
    if opcao == 1:
        lp.listar_professor()

    elif opcao == 2:
        matricula = int(input('Digite o número da matricula: '))
        lp.mostrar_professor(matricula)

    elif opcao == 3:
        nome = str(input('Digite o nome do professor: '))
        materia = str(input('Digite o nome da Matéria: '))
        horas = int(input('Digite as horas trabalhadas: '))
        p = Professor(mat_p, nome, materia, horas)
        lp.inserir_professor(p)
        mat_p += 1
    elif opcao == 4:
        matricula = int(input('Digite o número da matricula: '))
        lp.apagar_professor(matricula)
    if opcao == 5:
        la.listar_aluno()

    elif opcao == 6:
        matricula = int(input('Digite o número da matricula: '))
        la.mostrar_aluno(matricula)

    elif opcao == 7:
        nome = str(input('Digite o nome do Aluno: '))
        turma = str(input('Digite o nome da Turma: '))
        nota = []
        n1 = int(input('Digite a 1° nota: '))
        nota.append(n1)
        n2 = int(input('Digite a 2° nota: '))
        nota.append(n2)
        n3 = int(input('Digite a 3° nota: '))
        nota.append(n3)
        a = Aluno(mat_a, nome, turma, nota)
        la.inserir_aluno(a)
        mat_a += 1
    elif opcao == 8:
        matricula= int(input('Digite o número da matricula: '))
        la.apagar_aluno(matricula)

    elif opcao == 0:
        print('saindo...')
        break


