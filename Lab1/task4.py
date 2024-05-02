#Task 4

inputFile = open('input4.txt', 'r')
outputFile = open('output4.txt', 'w')

t = inputFile.readline().strip()
t = int(t)

masterList = []
for i in range(t):
  f  = inputFile.readline().strip().split()
  masterList.append([f[0], f[4], f[6], i]) #name, location, time, serial

def isLatest(t1, t2):  #is train1 later than train 2
  t1 = [int(i) for i in t1.split(':')]
  t2 = [int(i) for i in t2.split(':')]
  if t1[0]> t2[0]:
    return True
  
  elif t1[0] == t2[0]:
    if t1[1] > t2[1]:
      return True
    
  return False

def selectionSort(array, size): 
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i][0] < array[min_idx][0]:
                min_idx = i
            
            elif array[i][0] == array[min_idx][0]:
              if array[i][2] == array[min_idx][2]:
                 if array[i][3] < array[min_idx][3]:
                    min_idx = i
              elif isLatest(array[i][2], array[min_idx][2]):
                min_idx = i
              
        (array[step], array[min_idx]) = (array[min_idx], array[step])


def main(arr):
  selectionSort(masterList, t)
  for i in range(t):
    
    outputFile.write(f"{arr[i][0]} will depart for {arr[i][1]} at {arr[i][2]}\n")
  outputFile.close

main(masterList)