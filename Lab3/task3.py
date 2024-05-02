#Task 3
#Conditions: arr[i] > arr[j] ; i < j
#Basically mergesort + one counter

def mergeAndCount(left, right):
    global count
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        result.append(left[i])
        i += 1
      else: 
        result.append(right[j])
        j += 1
        count += len(left) - i
        #If a[i] > a[j], then everything on right side of i(included), is guaranteed to satisfy conditions
        #So we add the len(left) - i to count, then check with values of j
        #Else, i++ and check with the value of j.


    #Appending the rest of the elements
    while i < len(left):
      result.append(left[i])
      i +=1

    while j < len(right):
      result.append(right[j])
      j +=1

    return result

def mergeSort(arr):
    #Base case
    if len(arr) <= 1:
        return arr
    
    #Recursive call
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    mergedArr = mergeAndCount(left, right)

    return mergedArr

def main():
  inputFile = open('input3.txt', 'r')
  outputFile = open('output3.txt', 'w')

  global count
  count = 0

  n = int(inputFile.readline())
  arr = [int(i) for i in inputFile.readline().split()]
  mergeSort(arr)
  outputFile.write(str(count))
  outputFile.close()
main()  