#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    
    num_coins = [float('inf')] * (total + 1)
    num_coins[0] = 0

   
    for coin in coins:
        for amount in range(coin, total + 1):
            num_coins[amount] = min(num_coins[amount], 1 + num_coins[amount - coin])

    return num_coins[total] if num_coins[total] != float('inf') else -1