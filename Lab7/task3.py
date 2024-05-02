#Task 3
#Fibonacci  

def main():
    f1 = open("input3_3.txt", "r")
    f2 = open("output3_3.txt", "w")

    n = int(f1.read())
    
    #Compared to normal fibonacci sequence, the pattern is shifted by 1.
    #E.g: 5th stair = fib 6
    #Thus, nth stair = fib(n+1)

    memo = [None] * (n+2) #So we need to take size (n+1) +1 = n+2

    ans = fib(n+1, memo)
    print(ans, file=f2)

    f1.close()
    f2.close()

def fib(n, memo):
    if memo[n]:
      return memo[n]
    if n == 0 or n == 1:
      return n
    else:
      result = fib(n-1, memo) + fib(n-2, memo)
      memo[n] = result
      return result

main()