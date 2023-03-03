def no_caminho(no):
  caminho = [no.estado]
  while no.no_pai is not None:
    caminho.append(no.estado)
    no = no.no_pai
  caminho.reverse()
  return caminho

def vertice_caminho(no):
  caminho = []
  while no.no_pai is not None:
    if no.aresta is not None: caminho.append(no.aresta)
    no = no.no_pai
  caminho.reverse()
  return caminho

class Visitados:
  def __init__(self):
    # Conjuntos (Sets) em python e {1, 2, 3}
    # necessita ser uma tupla ou string por ser comparável com ==
    self.visitados = []
  
  def adicionar(self, no):
    self.visitados.append(tuple(no.estado))
  
  def foi_visitado(self, no):
    return tuple(no.estado) in self.visitados

  def tamanho(self):
    return len(self.visitados)