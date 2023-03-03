from no import No

class Hanoi():
# Respectivamente estado inicial e final, vazios pois os tamanhos deles dependem da quantidade de torres determinadas posteriormentes >=3 
	I_state = []
	
	F_states = []
	#construtor
	def __init__(self, numDisk, numTowers):

		tower = list(range(1, numDisk + 1))
		#ordenamos nossas torres em ordem decrescente pois no jogo das Torres de Hanoi os maiores   discos ficam em baixo ou seja são os primeiros discos das nossa torres/listas
		tower.sort(reverse = True)

		# Lista do estado inicial
		self.I_state = self.setInitState(numTowers,tower)

		# Lista de possiveis estados finais
		self.F_states = self.setFinalState(numTowers, tower)


		for i in range(len(self.I_state)):
			self.I_state[i] = tuple(self.I_state[i])
		for pos in self.F_states:
			for j in range(len(pos)):
				pos[j] = tuple(pos[j])

			
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
	
	def setInitState(self, numTowers, tower):
		I_state = []
		for i in range(numTowers):
			I_state.append([])

		I_state[0] = tower

		return I_state
	
	def setFinalState(self, numTowers, tower):
		F_states = []
		for i in range(numTowers - 1):
			F_states.append([])
		
		k = 1
		for pos in F_states:
			for j in range(numTowers):
				pos.append([])
			pos[k] = tower
			k+=1
		return F_states



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
		for pos in self.F_states:
			if(no.estado == pos):
				return True
			else:
				return False
  