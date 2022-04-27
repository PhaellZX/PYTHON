class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco


class Carrinho:
    def __init__(self):
        self.lista_produtos = []

    def inserir_produto(self, produto):
        self.lista_produtos.append(produto)

    def remover_produto(self, n):
        for prod in self.lista_produtos:
            if n == prod.codigo:
                self.lista_produtos.pop(n)
                print('PRODUTO REMOVIDO DO CARRINHO!\n')


    def mostrar_produto(self):
        print('-------CARRINHO--------')
        for prod in self.lista_produtos:
            print(f'{prod.codigo}|{prod.nome} -> {prod.preco:.2f}')
        print('-----------------------')
        print(f'TOTAL: R${self.soma():.2f}')
        print()

    def soma(self):
        s = 0
        for prod in self.lista_produtos:
            s += prod.preco
        return s

    def gerar_Nota(self):
        with open('Nota_Fiscal.csv','w') as nota:
            nota.write('-----NOTA FISCAL------\n')
            for prod in self.lista_produtos:
                nota.write(str(prod.codigo) + '|' + str(prod.nome) + ' -> ' + str(prod.preco) + '\n')
            nota.write('----------------------\n')
            nota.write(f'VALOR TOTAL: R$' + str(self.soma()))
        self.mostrar_produto()
        print('NOTA FISCAL GERADA!!')