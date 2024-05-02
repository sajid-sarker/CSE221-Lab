#Task 1
import numpy as np

def main():
  fi = open('input1a_2.txt', 'r')
  fo = open('output1a_2.txt', 'w')

  n, m = map(int, fi.readline().split())  #vertices, edges
  matrix = np.zeros((n+1, n+1), dtype=int)

  for i in range(m):
    u, v, w = map(int, fi.readline().split())
    matrix[u][v] = w
  
  displayMatrix(matrix, fo)
  fo.close()

def displayMatrix(arr, fo):
  for row in range(len(arr)):
    for col in range(len(arr[row])):
      fo.write(str(arr[row][col]) + ' ')
    fo.write('\n')

main()