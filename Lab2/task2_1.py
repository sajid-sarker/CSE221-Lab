#Task 2_1

inputFile = open('input2.txt', 'r')
outputFile = open('output2_1.txt', 'w')

sizeN = int(inputFile.readline())
n = [int(i) for i in inputFile.readline().split()]
sizeM = int(inputFile.readline())
m = [int(i) for i in inputFile.readline().split()]

combined = n + m  #combine the 2 arrays

def mergeSort(arr):
  #Base case
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  right = arr[mid:]
  left = arr[:mid]

#Recursive call
  left = mergeSort(left)
  right = mergeSort(right)
  
  #Comparison using 2 pointers
  i = j = k = 0 #tracking index in left, right, final arrays respectively
  finalArr = []
  while i < len(left) and j < len(right): 
    if left[i] < right[j]:
      finalArr.append(left[i])
      i += 1

    else:
      finalArr.append(right[j])
      j += 1
    k+=1

#Append the remaining elements in the sorted lists into final array
  while i < len(left):
      finalArr.append(left[i])
      i +=1
      k +=1
  while j < len(right):
      finalArr.append(right[j])
      j +=1
      k +=1
  return finalArr

finalArr = mergeSort(combined)
for i in finalArr:
  print(i, end =" ")
  outputFile.write(f'{i} ')
outputFile.close()
