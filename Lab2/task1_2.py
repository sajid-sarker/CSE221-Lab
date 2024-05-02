#Task 1_2

inputFile = open('input1.txt', 'r')
outputFile = open('output1_2.txt', 'w')

n , s = map(int, inputFile.readline().split())
arr = [int(i) for i in inputFile.readline().split()]


def comparison(arr, i, j):
  while True:
    if i == j:
      return ['Impossible']
    add = arr[i] + arr[j]
    if add > s:
      j -= 1
    elif add < s:
      i +=1
    else:
      return [i+1, j+1]

def main():
  temp = comparison(arr, 0, len(arr)-1)
  for i in temp:
    outputFile.write(f'{i} ')
  outputFile.close()

main()