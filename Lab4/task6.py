#Task 6
#Flood fill

def main():
  fin = open('input6_1.txt', 'r')
  fout = open('output6_1.txt', 'w')

  rows, cols = map(int, fin.readline().split())
  grid = []
  for i in range(rows):   #Create grid
    arr = [j for j in fin.readline().strip()]
    grid.append(arr)
  

  mx = maximumDiamonds(grid)
  fout.write(str(mx))
  fout.close()

def flood_fill(G,  row, col):
  #Base case
  if row < 0 or row>=len(G) or col<0 or col>=len(G[0]) or G[row][col] == '#':
     return 0

  diamonds = 0
  
  if G[row][col] == 'D': 
    diamonds += 1 #if D is in starting node

  G[row][col] = '#' #Changes the node to set it as visited

  #Checks in right, left, up, down directions respectively
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  #Counts how many diamonds can be found in each direction
  for dr, dc in directions:
    diamonds += flood_fill(G, row + dr, col + dc)
    
  return diamonds

def maximumDiamonds(G):
    maxDiamonds = 0
    rows, cols = len(G), len(G[0])  #No. of rows and columns
    
    for r in range(rows):
        for c in range(cols):
            if G[r][c] == '.':
                maxDiamonds = max(maxDiamonds, flood_fill(G, r, c))
    
    return maxDiamonds

main()