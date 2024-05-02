#Task 2

def maxDC(arr):
  #Base case
  if len(arr) <= 1:
    return arr[0]   #return value 
  
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]

  #Recursive call for division
  left = maxDC(left)
  right = maxDC(right)

  #Comparison
  maxVal = -1
  
  if left <= right: 
    maxVal = right
    
  else:
    maxVal = left
  
  return maxVal


def main():
  inputFile = open('input2.txt', 'r')
  outputFile = open('output2.txt', 'w')

  n = int(inputFile.readline())
  arr = [int(i) for i in inputFile.readline().split()]

  val = maxDC(arr)
  outputFile.write(str(val))
  outputFile.close()


main()