#Task 2

import heapq

def main():
  fin = open('input2_3.txt', 'r')
  fout = open('output2_3.txt', 'w')

  n, m = map(int, fin.readline().split())

  D = {i:[] for i in range(1, n+1)}

  inDeg = [0]*(n+1)
  for i in range(m):
      s, d = map(int, fin.readline().split())
      D[s].append(d)
      inDeg[d] += 1

  visited = set()
  global result, pq
  result = []
  pq = []
  heapq.heapify(pq)
  for i in range(1, n+1):
      if inDeg[i] == 0 and i not in visited:
          bfs(D, i, visited, inDeg)

  #if it fails to visit all nodes/ver.
  if len(result) < n:
      fout.write('IMPOSSIBLE')
  else:
      fout.write(str(result).strip('[]').replace(',',''))

  fin.close()
  fout.close()

def bfs(G, s, visited, Indeg):
    visited.add(s)
    heapq.heappush(pq, s)

    while pq:
        u = heapq.heappop(pq)
        result.append(u)

        for v in G[u]:
            Indeg[v] -= 1

            if v not in visited and Indeg[v] == 0:
                visited.add(v)
                heapq.heappush(pq, v)

main()