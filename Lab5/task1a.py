#Task 1a
#DFS approach

def dfs(G, v, visited, inDeg):
    visited.add(v)
    result.append(v)

    for neighbour in G[v]:
        #Decrease in degree count of child node by 1
        inDeg[neighbour] -= 1

        if neighbour not in visited and inDeg[neighbour] == 0:
            dfs(G, neighbour, visited, inDeg)

def main():
  global result

  fin = open('input1_3.txt', 'r')
  fout = open('output1a_3.txt', 'w')

  n,m = map(int, fin.readline().split())

  G = {i:[] for i in range(1, n+1)}
  result = []

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
          dfs(G, i, visited, inDeg)

  #If it fails to visit all nodes/vertex.
  if len(result) < n:
      fout.write('IMPOSSIBLE')
  else:
      #Print list to output format
      fout.write(str(result).strip('[]').replace(',',''))

  fin.close()
  fout.close()

main()