#Task 2
#Minimum Spanning Tree using Kruskal's algorithm with UFDS
import heapq

def main():
  f1 = open('input2_2.txt', 'r')
  f2 = open('output2_2.txt', 'w')

  n, m = map(int, f1.readline().split())  #no. of cities, roads

  #Sorts the edges in ascending order using min heap.
  pq = []
  heapq.heapify(pq)
  for i in range(m):
    u, v, w = map(int, f1.readline().split())
    heapq.heappush(pq, (w, u, v))

  parent = [i for i in range(n+1)]
  
  total = kruskal(pq, parent)
  print(total, file=f2)
  f1.close()  
  f2.close()

def kruskal(pq, parent):
  totalCost = 0
  mst = {i:[] for i in range(1, len(parent))}

  while pq:
    cost, u, v = heapq.heappop(pq)
    parent1 = getParent(parent, u)
    parent2 = getParent(parent, v)

    if (parent1 != parent2):  
      parent[parent2] = parent1
      totalCost += cost
      mst[u].append(v)
      mst[v].append(u)

  return totalCost

def getParent(parent, n): #Returns the parent of selected node
  p = parent[n]
  if p == n:
    return p
  else:
    return getParent(parent, p)


main()  