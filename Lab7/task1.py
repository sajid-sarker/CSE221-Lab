#Task 1
#Union Find Disjoint Set

def main():
  f1 = open('input1_2.txt', 'r')
  f2 = open('output1_2.txt', 'w')

  n, k = map(int, f1.readline().split())  #no. of people, queries
  
  parent = [i for i in range(n+1)] #Stores the parent of each node
  friends = [1]*(n+1) #Stores the no. of nodes connected aside from parent

  for i in range(k):
    a, b = map(int, f1.readline().split())  

    parent1 = getParent(parent, a)
    parent2 = getParent(parent, b)
    
    # Here we aren't doing union by size. We just link root of B 
    # to root of A without checking anything. 
    if (parent1 != parent2):  
      parent[parent2] = parent1
      friends[parent1] = friends[parent1] + friends[parent2]

    print(friends[parent1], file = f2)

  f1.close()
  f2.close()


def getParent(parent, n): #Returns the parent of selected node
  p = parent[n]
  if p == n:
    return p
  else:
    return getParent(parent, p)


main()