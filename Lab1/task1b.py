#Task 1b

inputFile = open('input1b.txt', 'r')
outputFile = open('output1b.txt', 'w')

t = inputFile.readline().strip()
t = int(t)

def calc(a):
  n1, n2, sign = int(a[0]), int(a[2]), a[1]

  if sign == '+':
    r = n1 + n2
  elif sign == '-':
    r = n1 - n2
  elif sign == '*':
    r = n1 * n2
  elif sign == '/':
    r = n1 / n2
  return r

for i in range(t):
  line = inputFile.readline().strip().lstrip('calculate ')
  temp = line.split()
  outputFile.write(f"The result of {line} is {calc(temp)}\n")

outputFile.close()