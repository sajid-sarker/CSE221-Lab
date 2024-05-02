#Task 1_1

inputFile = open('input1.txt', 'r')
outputFile = open('output1_1.txt', 'w')

n , s = map(int, inputFile.readline().split())
arr = [int(i) for i in inputFile.readline().split()]

def comparison(arr, s):

  flag = False
  for i in range(len(arr)-1):

    for j in range(i+1,len(arr)):
      if arr[i] + arr[j] == s:
        outputFile.write(f'{i+1} {j+1}')
        flag = True
        break

    if flag == True: 
      break
  else:
    outputFile.write('IMPOSSIBLE')
  outputFile.close()
comparison(arr, s)