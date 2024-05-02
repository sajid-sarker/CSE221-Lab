#Task 1b
#BFS approach

def bfs(G, u, visited, inDeg):
  
  visited.add(u)
  q = [u]

  while q:
    u = q.pop()
    result.append(u)

    for v in G[u]:
      inDeg[v] -=1
      
      if v not in visited and inDeg[v] == 0:
        visited.add(v)
        q.append(v)

def main():
  global result
  result = []

  fin = open('input1_1.txt', 'r')
  fout = open('output1b_1.txt', 'w')

  n,m = map(int, fin.readline().split())

  G = {i:[] for i in range(1, n+1)}
  
  inDeg = [0]*(n+1) #Initially, each node has 0 in degree edges

  for i in range(m):
      #Here, we simultaneously create the adj list and we 
      #count the number of in degree edges that each node has
      u, v = map(int, fin.readline().split())
      G[u].append(v)
      inDeg[v] += 1

  visited = set()

  for i in range(1,n+1):
      #We only start dfs when there is no prerequisite/ in degree edge
      if inDeg[i] == 0 and i not in visited:  
          bfs(G, i, visited, inDeg)

  #If it fails to visit all nodes/vertex.
  if len(result) < n:
      fout.write('IMPOSSIBLE')
  else:
      #Print list to output format
      fout.write(str(result).strip('[]').replace(',',''))

  fin.close()
  fout.close()


main()