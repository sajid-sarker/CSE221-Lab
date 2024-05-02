#Task 4
#Coin Change problem
#We must find the minimum no. of coins needed to reach target
# dp[i][j] = min(dp[i-1][j], 1 + dp[i][j - coins[i]])

def main():
  f1 = open("input4_2.txt", "r")
  f2 = open("output4_2.txt", "w")

  n, w = map(int, f1.readline().split())  #No. of different coins available, target amount
  
  coins = list(map(int, f1.readline().split()))
  
  result = coinChange(coins, w)
  print(result, file=f2)

  f1.close()
  f2.close()

#1D approach since we don't need backtracking
def coinChange(coins, w):
    dp = [float('inf')] * (w+1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, w+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[w]

main()