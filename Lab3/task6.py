#Task 6

def kthSmallest(arr, start, end, k):
  size = end - start + 1
  if k > 0 and k <= size: #Checking if k is within valid range

    #Initial sorting with lower on left and greater on right
    #Now we can discard one side of the array completely.
    pivotIndex = partition(arr, start, end)

    if pivotIndex - start == k-1:   #If pivot index same as k
      return arr[pivotIndex]
    
    #If k lower than pivot then we start working on the left subarray only.
    if pivotIndex - start > k-1:  
      return kthSmallest(arr, start, pivotIndex-1, k)
    
    #If k greater than pivot then we start working on the right subarray only.
    else:
      return kthSmallest(arr, pivotIndex+1, end, k-(pivotIndex-start+1))
    #Here k is adjusted so that we are looking for k relative to the new subarray not the old one.
  
  else: 
    print('This value of k is invalid.')

def partition(arr, start, end): #Same partition func as qsort.
  pivot = arr[end]

  i = start-1
  for j in range(start, end):
    if arr[j] < pivot:
      i+=1
      arr[i], arr[j] = arr[j], arr[i]

  i+=1
  arr[i], arr[end] = arr[end], arr[i]

  return i


def main():
  inputFile = open('input6.txt', 'r')
  outputFile = open('output6.txt', 'w')

  n = int(inputFile.readline())
  arr = [int(i) for i in inputFile.readline().split()]
  q = int(inputFile.readline())
  for i in range(q):
    k = int(inputFile.readline())
    t = kthSmallest(arr, 0, len(arr)-1, k)
    outputFile.write(str(t) + '\n')
  outputFile.close()

main()