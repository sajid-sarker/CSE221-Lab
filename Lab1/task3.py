#Task 3

inputFile = open('input3.txt', 'r')
outputFile = open('output3.txt', 'w')

t = inputFile.readline().strip()
t = int(t)

idNum = [int(i) for i in inputFile.readline().split()]
marks = [int(i) for i in inputFile.readline().split()]
list1 = []    #[(7,40), (4,50)...]

for i in range(t) :   #Conversion to tuple. 
  tup = tuple([idNum[i], marks[i]])
  list1.append(tup)

def selectionSort(array, size): #Selection sorting has min no. of swaps
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i][1] > array[min_idx][1]:
                min_idx = i
            #Checking ID num if marks are equal
            elif array[i][1] == array[min_idx][1] and array[i][0] < array[min_idx][0]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])

def main():
    selectionSort(list1, t)
    for i in range(t):
        outputFile.write(f"ID: {list1[i][0]} Marks: {list1[i][1]}\n")
    outputFile.close()

main()