from algoritmos.auxiliar import Visitados

# Breadth-First Search - Busca em Largura
def bfs(problema):
  no = problema.iniciar()

  fila = Fila()
  fila.push(no)

  visitados = Visitados()

  while not fila.esta_vazio():
    no = fila.pop()
    visitados.adicionar(no)

    # faz o teste objetivo. Se chegou no resultado final
    # retorna o No correspondente
    if(problema.testar_objetivo(no)):
      return (visitados.tamanho(), no)
    
    # função sucessores define os Nós sucessores
    nos_sucessores = problema.gerar_sucessores(no)

    # para cada sucessor, se armazena se ainda não visitado
    for no_sucessor in nos_sucessores:
      # pula estado_filho se já foi expandido
      if not visitados.foi_visitado(no_sucessor): fila.push(no_sucessor)

  return (visitados.tamanho(), None)

class Fila:
  def __init__(self):
    self.fila = []
  
  def push(self, item):
    self.fila.append(item)
  
  def pop(self):
    if(self.esta_vazio()):
        return None
    else:
        return self.fila.pop(0)

  def esta_vazio(self):
    return len(self.fila) == 0