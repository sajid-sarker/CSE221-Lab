#Task 1
#Dijkstra algorithm
import heapq

def main():
  f1 = open('input1_2.txt', 'r')
  f2 = open('output1_2.txt', 'w')

  n, m = map(int, f1.readline().split())

  G = {i:[] for i in range(1, n+1)}

  for i in range(m):
    u, v, w = map(int, f1.readline().split()) # start node, end node, weight
    G[u].append((v, w))

  s = int(f1.read())
  
  sp = dijkstra(G, s)
  for i in range(1, len(sp)):
    if sp[i] == float('inf'):
      print('-1', end = ' ', file = f2)
    else:
      print(sp[i], end = ' ', file = f2)
  
  f1.close()
  f2.close()


def dijkstra(G, s):
  pq = []
  heapq.heapify(pq)

  # We must store it in the form (distance, node) otherwise 
  # we will get the node with smallest number when popping
  heapq.heappush(pq, (0, s))  

  dist = [float('inf')] * (len(G)+1)
  dist[s] = 0

  while pq:
    d, u = heapq.heappop(pq)
    
    for v, w in G[u]:
      if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        heapq.heappush(pq, (dist[v], v))

  return(dist)   

main()