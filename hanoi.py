from no import No

class Hanoi():
# Respectivamente estado inicial e final, vazios pois os tamanhos deles dependem da quantidade de torres determinadas posteriormentes >=3 
  I_state = []
  
  F_state = []
  #construtor
  def __init__(self, numDisk, numTowers):
    for i in range (numTowers):
# "alocando" a quantidade de torres desejadas nos estados cada torre é uma lista que em python se comporta como pilha se provando útil para dar pop no disco de cima pois as torres de hanoi são LIFO (last-in first-out) 
      self.I_state.append([])
      self.F_state.append([])
#torres = listas cujo o tamanho "altura" correspondem ao numero de discos determinado anteriormente
      tower = []
      size = 0
      for i in range(1, numDisk + 1):
        tower.append(i)
        size+=1
        
#ordenamos nossas torres em ordem decrescente pois no jogo das Torres de Hanoi os maiores   discos ficam em baixo ou seja são os primeiros discos das nossa torres/listas
      tower.sort(reverse = True)

#self.I_state[0] representa a torre da posiçao 0/inicial como a torre com todos os discos ordenados self.F_state[-1] ja que em python se usa [-1] para pegar o ultimo elemnto de uma lista representa a ultima torre vulgo a final com todos os discos ordenados
      self.I_state[0] = tower
    

      for i in range(len(self.I_state)):
        self.I_state[i] = tuple(self.I_state[i])
        self.F_state[i] = tuple(self.F_state[i])

    self.F_state[-1] = tuple(tower)



        
#função para iniciar nosso no raiz
  def iniciar(self):
    self.raiz = No(estado=self.I_state, custo=self.custo(), heuristica=self.heuristica())
    return self.raiz
#checamos o estado criando uma copia das torres e ordenando  corretamente ao compararmos com as originais podemos descobrir se  a torre esta ordenana de uma maneira invalida ex: discos maiores em cima de menores
  def check_state(self, no: No):
    corrigido = []
    if no is None:
        return False

    for tower in no.estado:
      aux = list(tower)
      aux.sort(reverse = True)
      corrigido.append(aux)

    return no.estado == corrigido
      
  def movimento(self, destino, origem , no: No):
    currState  = []
    
    for tower in no.estado:
      currState.append(list(tower))
    if len(currState[origem]) > 0:
      disk = currState[origem].pop()
      currState[destino].append(disk)
    else:
        return None
      
    return No(estado = currState,no_pai=no,custo=self.custo(),heuristica=self.heuristica())
 
  def gerar_sucessores(self, no: No):
    estado = no.estado
    sucessores =  []
    for origem in range(len(estado)):
      for destino in range(len(estado)):
        if destino != origem:
          sucessor = self.movimento(destino, origem, no)
          #no = sucessor
          if self.check_state(sucessor): 
            sucessores.append(sucessor)


    return sucessores
   
# heuristica que foi dada o no é usado como none pois na hora de iniciar não terá um no ainda
  def heuristica(self, no: No = None):
    if no == None:
      return 0
    return -len(no.estado[-1])
#custo é sempre 1
  def custo(self):
    return 1
#checagem para ver se estamos no estado final
  def testar_objetivo(self, no: No):
    copy = no.estado
    for i in range(len(copy)):
        copy[i] = tuple(copy[i])
    return no.estado == self.F_state
  