from algoritmos.auxiliar import Visitados
from queue import PriorityQueue

def a_estrela(problema):
    no = problema.iniciar()
    fila = FilaPrioridade()
    fila.push(0,no)

    visitados = Visitados()
    visitados.adicionar(no)

    while not fila.esta_vazio():
        
        no = fila.pop()
        visitados.adicionar(no)

        # faz o teste objetivo. Se chegou no resultado final
        # retorna o No correspondente
        resultado = problema.testar_objetivo(no)
        if(resultado):
            return (visitados.tamanho(), no)

        # função sucessores define os Nós sucessores
        nos_sucessores = problema.gerar_sucessores(no)
        # para cada sucessor, se armazena se ainda não visitado
        for no_sucessor in nos_sucessores:
            # pula estado_filho se já foi expandido
            if not visitados.foi_visitado(no_sucessor):
                no_sucessor.custo = no.custo + problema.custo()
                no_sucessor.heuristica = problema.heuristica(no_sucessor)
                a_estrela_n = (no_sucessor.custo + no_sucessor.heuristica)

                fila.push(a_estrela_n, no_sucessor)

    return (visitados.tamanho(), None)

class FilaPrioridade:
  def __init__(self):
    self.fila = PriorityQueue()
  def push(self, valor, item):
    self.fila.put((valor, item))
  
  def pop(self):
    if(self.esta_vazio()):
      return None
    else:
      (_, no) = self.fila.get()
      return no

  def esta_vazio(self):
    return self.fila.qsize() == 0