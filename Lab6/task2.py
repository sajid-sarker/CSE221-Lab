#Task 2
# We find the shortest path to each node from A and B.
# Then we compare each and choose the max value for each node.
# Finally, from the max values to reach the node, we choose the smallest overall.
# This is the Time needed. The node that corresponds with this time is also output.

import heapq

def main():
  f1 = open('input2_2.txt', 'r')
  f2 = open('output2_2.txt', 'w')

  n, m = map(int, f1.readline().split())

  G = {i:[] for i in range(1, n+1)}

  for i in range(m):
    u, v, w = map(int, f1.readline().split()) # start node, end node, weight
    G[u].append((v, w))

  s, t = map(int, f1.readline().split())
  
  spA = dijkstra(G, s)
  spB = dijkstra(G, t)

  minValue = float('inf')
  minIndex = 0

  for i in range(1, n+1):
    mx = max(spA[i], spB[i]) 
    if mx < minValue: 
      minValue = mx
      minIndex = i

  if minValue == float('inf'): print('IMPOSSIBLE', file = f2)
  else: 
    print('Time ' + str(minValue), file = f2)
    print('Node ' + str(minIndex), file = f2)

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