#Task 1

def merge(a, b):
    # write your code here
    # Here a and b are two sorted list
    # merge function will return a sorted list after merging a and b
    i = j = 0
    arr = []
    while i < len(a) and j < len(b):
      if a[i] <= b[j]: 
        arr.append(a[i])
        i +=1

      else:
        arr.append(b[j])
        j +=1

    #Appending the rest of the elements
    while i < len(a):
      arr.append(a[i])
      i +=1

    while j < len(b):
      arr.append(b[j])
      j +=1
    
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  #left
        a2 = mergeSort(arr[mid:])  #right
        return merge(a1, a2)          # complete the merge function above 

def main():
  inputFile = open('input1.txt', 'r')
  outputFile = open('output1.txt', 'w')

  n = int(inputFile.readline())
  arr = [int(i) for i in inputFile.readline().split()]
  sortedArr = mergeSort(arr)
  for i in sortedArr: outputFile.write(str(i) + ' ')

main()