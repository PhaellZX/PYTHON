# clase exemplo #
class Livro:
  def __init__(self, titulo, autor, paginas):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas
      self.preco = paginas * 0.5

  def info(self):
    print(f'Titulo: {self.titulo}; Autor: {self.autor}; Preco: R${self.preco}')
