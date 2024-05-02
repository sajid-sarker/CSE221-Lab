#Task 3
#SCC finding using Kosaraju Algorithm
# 1. Create G and transpose of G graphs
# 2. Run dfs in initial graph
# 3. Using the REVERSE order of step 2 dfs, run dfs in transpose of G


def main():
  global fin, fout
  fin = open('input3_3.txt', 'r')
  fout = open('output3_3.txt', 'w')

  n, m = map(int, fin.readline().split())

  G = {i:[] for i in range(1, n+1)} #Original graph
  T = {i:[] for i in range(1, n+1)}  #Transpose graph

  for m in range(m):  
    u, v = map(int, fin.readline().split())

    #Transpose is just the same graph 
    #but direction of edges are flipped
    G[u].append(v)   
    T[v].append(u)

  kosaraju(G, T, n)

  fin.close()
  fout.close()


def dfs(G, u, visited, stack):
  visited[u] = True
  for v in G[u]:
    if not visited[v]:
      dfs(G, v, visited, stack)

  stack.append(u)
  return stack

def connected(G, u, visited, scc = []):
  visited[u] = True 
  scc.append(u)
  for v in G[u]:
    if not visited[v]:
      scc = connected(G, v, visited, scc)
  return scc

def kosaraju(G, T, n):
  visited = [False]*(n+1)
  stack = []
  for i in range(1, n+1):
    if not visited[i]:
      stack = dfs(G, i, visited, stack)

  visited = [False]*(n+1)

  #As we pop out of stack we are receiving value
  #in the topological sorted order
  while stack:
    u = stack.pop()
    if not visited[u]:
      scc = []  
      temp = connected(T, u, visited, scc)
      temp.sort()
      for item in temp: 
        print(item, end=' ', file= fout)
      print(file = fout)


main()