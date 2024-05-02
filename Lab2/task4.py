#Task 4
#Similar to task 3 but with multiple people

inputFile = open('input4.txt', 'r')
outputFile = open('output4.txt', 'w')

n, m = map(int, inputFile.readline().split()) #n = no. of tasks, m = no. of people

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

  #Comparison using 2 pointers
  i = j = k = 0
  
  while i < len(left) and j < len(right):
    if left[i][1] <= right[j][1]:   #ordering by ascending end time
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

sortedArr = mergeSort(arr)

def greedy(arr, m):
  currentTimes = [0]*m
  count = 0
  maxEndTime = 0   #Makes sure each activity is assigned to the person with the earliest available time.
  for start, end in sortedArr:
    
    for i in range(m):
      #Checks if start time is after or equal to max time 
      #And also avoids giving task to person with same ending time. 
      if start >= maxEndTime and currentTimes[i] != maxEndTime:
        continue

      if currentTimes[i] <= start:
        currentTimes[i] = end
        
        if currentTimes[i] > maxEndTime:
          maxEndTime = currentTimes[i]
        
        count +=1
        break
        
  outputFile.write(str(count))
  outputFile.close()


greedy(sortedArr, m)