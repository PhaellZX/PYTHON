from time import sleep

class Professor:
    def __init__(self, mat_prof, nome, materia, horas):
        self.mat_prof = mat_prof
        self.nome = nome
        self.materia = materia
        self.horas = horas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, materia):
        self.__materia = materia

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, horas):
        self.__horas = horas


class Lista_Professor:
    def __init__(self):
        self.lista_professor = []

    def inserir_professor(self, professor):
        self.lista_professor.append(professor)
        sleep(1)
        print('\nCadastrado Efetuado com sucesso!!\n')
        sleep(1)

    def mostrar_professor(self, matricula):
        for professores in self.lista_professor:
            if matricula == professores.mat_prof:
                sleep(1)
                print(f'\n{professores.mat_prof} {professores.nome} {professores.materia} {professores.horas} Horas\n')
                sleep(1)
                break
        if matricula != professores.mat_prof:
            sleep(1)
            print('\nMatricula não encontrado!\n')
            sleep(1)

    def listar_professor(self):
        print('\n------PROFESSORES--------')
        for professores in self.lista_professor:
            print(f'{professores.mat_prof} {professores.nome} {professores.materia} {professores.horas} Horas')
        print()
        input('Pressione ENTER para voltar ao menu...\n')

    def apagar_professor(self, matricula):
        for professores in self.lista_professor:
            if matricula == professores.mat_prof:
                self.lista_professor.pop(matricula - 1)
                sleep(1)
                print('Professor(a) removido com sucesso!')
                sleep(1)
                break
        if matricula != professores.mat_prof:
            sleep(1)
            print('Matricula não encontrado!')
            sleep(1)

class Aluno:
    def __init__(self, mat_aluno, nome, turma, notas):
        self.mat_aluno = mat_aluno
        self.nome = nome
        self.turma = turma
        self.notas = notas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def turma(self):
        return self.__turma

    @turma.setter
    def turma(self, turma):
        self.__turma = turma

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas):
        self.__notas = notas


class Lista_Aluno:
    def __init__(self):
        self.lista_aluno = []

    def inserir_aluno(self, aluno):
        self.lista_aluno.append(aluno)
        sleep(1)
        print('Aluno(a) Cadastrado!!')
        sleep(1)

    def mostrar_aluno(self, matricula):
        for alunos in self.lista_aluno:
           if matricula == alunos.mat_aluno:
              sleep(1)
              print(f'{alunos.mat_aluno} {alunos.nome} {alunos.turma} {alunos.notas} {((alunos.notas[0] + alunos.notas[1] + alunos.notas[2])/3)}')
              sleep(1)
              break

        if matricula != alunos.mat_aluno:
            sleep(1)
            print('Matricula não encontrado!')
            sleep(1)
        print()

    def listar_aluno(self):
        for alunos in self.lista_aluno:
            print(f'{alunos.mat_aluno} {alunos.nome} {alunos.turma} | NOTAS: {alunos.notas} MEDIA -> {((alunos.notas[0] + alunos.notas[1] + alunos.notas[2])/3)}')
        print()
        input('Pressione ENTER para voltar ao menu...\n')

    def apagar_aluno(self, matricula):
        for alunos in self.lista_aluno:
            if matricula == alunos.mat_aluno:
                self.lista_aluno.pop(matricula - 1)
                sleep(1)
                print('Aluno(a) removido com sucesso!')
                sleep(1)
                break
        if matricula != alunos.mat_aluno:
            sleep(1)
            print('Matricula não encontrado!')
            sleep(1)
