#Task 2
#Undirected and unweighted graph traversal using BFS
import numpy as np

def main():
  global fin, fout
  fin = open('input2_4.txt', 'r')
  fout = open('output2_4.txt', 'w')

  n, m = map(int, fin.readline().split())  #vertices, edges
  matrix = np.zeros((n+1, n+1), dtype=int)

  for i in range(m):
    u, v = map(int, fin.readline().split()) 
    matrix[u][v] = matrix[v][u] = 1    #Adjacency Matrix with undirected

  BFS(matrix, 1)
  fout.close()

def BFS(graph, startingNode):
  num = len(graph)
  visited = set()   #Can also use visited = [False] * num_nodes
  q = [startingNode]
  visited.add(startingNode)
  
  while q:
    u = q.pop(0)
    fout.write(f'{u} ')
    
    for neighbor in range(1, num):  #Checking adjacent nodes
      if graph[u][neighbor]==1 and neighbor not in visited:
        visited.add(neighbor)   #visited[neighbor] = True
        q.append(neighbor)

main()