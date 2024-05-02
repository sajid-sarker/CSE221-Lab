#Task 3
#DFS traversal in undirected and unweighted graph

def main():
  global fin, fout
  fin = open('input3_4.txt', 'r')
  fout = open('output3_4.txt', 'w')

  n, m = map(int, fin.readline().split())  #vertices, edges
  adjList = [[] for i in range(n+1)]  #Adjacency List with undirected

  for i in range(m):
    u, v = map(int, fin.readline().split()) 
    adjList[u].append(v)  
    adjList[v].append(u)  
  
  visited = [False]*(n+1)
  dfs(adjList, 1, visited)
  fout.close()

def dfs(graph, u, visited):
  visited[u] = True
  fout.write(f'{u} ')
  for v in graph[u]:
    if visited[v] == False:
      dfs(graph, v, visited)


main()