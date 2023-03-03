from algoritmos.a_estrela import a_estrela
from algoritmos.dijkstra import dijkstra
from algoritmos.dfs import dfs


from hanoi import Hanoi

if __name__ == "__main__":
  
  problema = Hanoi(5,3)

#   res_aStar = a_estrela(problema) 
#   res_djikstra = dijkstra(problema)
  res_dfs = dfs(problema)

#   print(f"A* = {res_aStar}")
#   print(f"Djikstra {res_djikstra}")
  print(f"DFS {res_dfs}")
