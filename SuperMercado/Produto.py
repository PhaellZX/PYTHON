class Produto:
    def __init__(self, id, nome, tipo, preco):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

    def consultarProduto(self):
       print(f'ID do Produto: {self.id} | Nome do produto: {self.nome} | Tipo: {self.tipo} | Preço: {self.preco:.2f}')