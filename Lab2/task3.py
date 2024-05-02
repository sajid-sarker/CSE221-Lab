#Task 3

inputFile = open('input3.txt', 'r')
outputFile = open('output3.txt', 'w')

n = int(inputFile.readline()) #n = no. of tasks

#Storing values in an array
arr = []
for i in range(n):
  x, y = map(int, inputFile.readline().split())
  arr.append((x,y))

def mergeSort(arr):
  #Base case
  if len(arr) <= 1:
    return arr

  mid = len(arr)//2
  left = arr[:mid] 
  right = arr[mid:]

  #Recursive call
  left = mergeSort(left)
  right = mergeSort(right)

  #comparison using 2 pointers
  i = j = k = 0
  
  while i < len(left) and j < len(right):
    if left[i][1] <= right[j][1]:   #ordering by end time
      arr[k] = left[i]
      i +=1

    else:
      arr[k] = right[j]
      j +=1
    k +=1

  #Appending the rest of the elements
  while i < len(left):
    arr[k] = left[i]
    i +=1
    k +=1

  while j < len(right):
    arr[k] = right[j]
    j +=1
    k +=1
  
  return arr
  
#Implementation of greedy algorithm
def greedy(arr):
  tasks = []
  currentTime = 0
  for i in range(len(arr)):
    
    if currentTime <= arr[i][0]:
      currentTime = arr[i][1]
      tasks.append(arr[i])

  outputFile.write(f'{len(tasks)}\n')
  for i in tasks: outputFile.write(f'{i[0]} {i[1]}\n')
  outputFile.close()


arr = mergeSort(arr)
greedy(arr)