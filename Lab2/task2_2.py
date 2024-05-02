#Task 2_2
inputFile = open('input2.txt', 'r')
outputFile = open('output2_2.txt', 'w')

sizeN = int(inputFile.readline())
n = [int(i) for i in inputFile.readline().split()]
sizeM = int(inputFile.readline())
m = [int(i) for i in inputFile.readline().split()]

i = j = 0 #i = pointer for N, j = pointer for M

finalArr = []

while i < sizeN and j < sizeM:  #Comparison using 2 pointers
  if n[i] < m[j]:
    finalArr.append(n[i])
    i +=1

  else:
    finalArr.append(m[j])
    j += 1

#Append the remaining elements in the sorted lists into final array
while i < sizeN:
    finalArr.append(n[i])
    i +=1
while j < sizeM:
    finalArr.append(m[j])
    j += 1

for i in finalArr:
  print(i, end =" ")
  outputFile.write(f'{i} ')
outputFile.close()