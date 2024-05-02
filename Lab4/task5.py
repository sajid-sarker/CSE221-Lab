#Task 5
#Shortest path

def main():
  global fin, fout
  fin = open('input5_5.txt', 'r')
  fout = open('output5_5.txt', 'w')

  n, m, d= map(int, fin.readline().split())  #vertices, edges
  adjList = [[] for i in range(n+1)]  #Adjacency List with unweighted undirected edges

  for i in range(m):
    u, v = map(int, fin.readline().split()) 
    adjList[u].append(v) 
    adjList[v].append(u)

  path, time = shortestPath(adjList, 1, d)
  
  #Output in file
  fout.write(f'Time: {time}\nShortest Path: ')
  for i in path: fout.write(f'{i} ')
  fout.close()

def shortestPath(G, s, dest):
  n = len(G)
  visited = [False]*(n+1) 
  q = [(s, [s], 0)] #Vertex, path to vertex, time
  visited[s] = True
  
  while q:
    u, path, time = q.pop(0)

    if u == dest:
      return path, time
    
    for v in G[u]:  #Checking adjacent nodes
      if not visited[v]:
        visited[v] = True
        q.append((v, path+[v], time+1))


main()