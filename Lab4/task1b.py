#Task 1b
#Adjacency list

def addEdge(adj, u, v, w):
     
    adj[u].append((v, w))
    return adj
 
def printGraph(adj, V, fo):
     
    for i in range(V+1):
      fo.write(str(i)+':')
      
      for j in adj[i]:
        fo.write(f' {j}')
        
      fo.write('\n')
      

def main():
    fi = open('input1b_3.txt', 'r')
    fo = open('output1b_3.txt', 'w')

    n, m = map(int, fi.readline().split())  #vertices, edges
    adjList = [[] for i in range(n+1)]  #Creates nested lists for each vertex

    for i in range(m):
      u, v, w = map(int, fi.readline().split())
      adjList = addEdge(adjList, u, v, w)
    
    printGraph(adjList, n, fo)
    fo.close()


main()