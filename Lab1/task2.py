#Task 2

inputFile = open('input2.txt', 'r')
outputFile = open('output2.txt', 'w')

t = inputFile.readline().strip()
t = int(t)

arr = [int(i) for i in inputFile.readline().split()]

def bubbleSort(arr):
  flag = False

  for i in range(len(arr)-1):
    
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flag = True

    if not flag:
      break

bubbleSort(arr)
s = ""
for x in arr: s = s + str(x) + " "

outputFile.write(s)
outputFile.close()


#In the best case scenario, the array is already sorted.
#So we need to only check if the array is sorted.
#By placing a flag in the beginning, we can check if any swaps were made.
#If no swaps were in the first loop, then the array is already sorted ann we can stop the sorting the algorithm.