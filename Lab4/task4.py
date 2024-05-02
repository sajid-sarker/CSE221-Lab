#Task 4
#Cycle finding

def main():
  fin = open('input4_5.txt', 'r')
  fout = open('output4_5.txt', 'w')

  n, m = map(int, fin.readline().split())  #vertices, edges
  adjList = [[] for i in range(n+1)]  #Adjacency List with unweighted directed edges

  for i in range(m):
    u, v = map(int, fin.readline().split()) 
    adjList[u].append(v) 

  if isCyclic(adjList): fout.write('Yes')
  else: fout.write('No')

  fin.close()
  fout.close()

def dfs(graph, u, visited, stack):  #visited = vertices visited
  visited[u] = True
  stack[u] = True   #stack is for the vertices visited during current dfs run
  for v in graph[u]:
    if visited[v] == False:
      if dfs(graph, v, visited, stack):
        return True
    elif stack[v] == True:  #If node already in stack, then cycle exists
      return True
  stack[u] = False #We remove it from stack so that it maintains correctness on the way back
  return False  
  
def isCyclic(graph):
  n = len(graph)
  visited = [False]*(n+1)
  stack = [False]*(n+1)
  for node in range(1,n):
    if visited[node] == False:
      if dfs(graph, node, visited, stack):
        return True
      
  return False


main()