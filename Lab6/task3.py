#Task 3

# In this task, we basically choose the edge with lowest weight
# then we pick the max value from this selection. 
# By sticking with the lowest values, we can use the safest route even if it's longer.


import heapq

def main():
  f1 = open('input3_1.txt', 'r')
  f2 = open('output3_1.txt', 'w')

  n, m = map(int, f1.readline().split())

  G = {i:[] for i in range(1, n+1)}

  for i in range(m):
    u, v, w = map(int, f1.readline().split()) # start node, end node, weight
    G[u].append((v, w))
  
  sp = dijkstra(G, 1)
  print(max(sp), file = f2)
  
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
  dist[0] = -1

  while pq:
    d, u = heapq.heappop(pq)
    
    for v, w in G[u]:
      if w < dist[v]:
        dist[v] = w
        heapq.heappush(pq, (w, v))

  return(dist)   

main()