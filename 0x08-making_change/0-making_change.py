#!/usr/bin/python3
"""2D matrix"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    current_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total-current_total)//coin
        current_total += r*coin
        coin_used += r
        if current_total == total:
            return coin_used
    return -1
