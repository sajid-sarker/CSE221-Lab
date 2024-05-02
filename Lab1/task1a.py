#Task 1a

input_file= open('input1a.txt', 'r')      #Any open file must be closed explicitly at the end
output_file = open('output1a.txt', 'w')

#read = reads the whole thing as one string
#readable = T or F whether we can read the file
#readline = reads each line one by one; iterable.

t = input_file.readline().strip()
t = int(t)


def evenOdd(n):
  if n%2 == 0:
    res = 'Even'
  else: res = 'Odd'
  return res

for i in range(t):
  text = input_file.readline()
  n = int(text.strip())
  output_file.write(f"{n} is an {evenOdd(n)} number.\n")


output_file.flush()   #Forces the file from RAM to ROM
output_file.close()