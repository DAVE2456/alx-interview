#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array of size total + 1 to store the minimum number of coins needed to make each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # For each coin, update the corresponding entries in the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
