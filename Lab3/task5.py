#Task 5
#Implement quicksort algorithm using random pivot
import random

def quicksort(arr, start, end):
  #Base case

  #When end == start, there the sub-array has only one elem
  #and the recursion stops so we don't allow that
  #Also it prevents the randomize range from working.
  if end > start: 
    pivotIndex = randomizePivot(arr, start, end)
    quicksort(arr, start, pivotIndex-1)
    quicksort(arr, pivotIndex+1, end)

def randomizePivot(arr, start, end):
  randPivot = random.randrange(start,end)

  #Swaps the start and pivot values.
  #This is done so the random pivot is now at the end and is sorted
  #in a similar way as done normally.
  arr[end], arr[randPivot] = arr[randPivot], arr[end] 

  return partition(arr, start, end)
    

def partition(arr, start, end):  #Returns the index of pivot
  
  pivot = arr[end]  #Choosing the right most elem as pivot

  #Comparison and swapping
  i = start-1

  for j in range(start, end):
    if arr[j] <= pivot:
      i +=1
      arr[i], arr[j] = arr[j], arr[i]

  i+=1
  arr[i], arr[end] = arr[end], arr[i]

  return i #Index of pivot


def main():
  inputFile = open('input5.txt', 'r')
  outputFile = open('output5.txt', 'w')

  n = int(inputFile.readline())
  arr = [int(i) for i in inputFile.readline().split()]

  quicksort(arr, 0, len(arr)-1)

  for i in arr:
    outputFile.write(str(i)+" ")
  outputFile.close()
main()