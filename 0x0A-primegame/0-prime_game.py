#!/usr/bin/python3


def isWinner(x, nums):
    # initialize counters for Maria and Ben's wins
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # determine if n is even or odd
        if n % 2 == 0:
            # if n is even, Ben will always win
            ben_wins += 1
        else:
            # if n is odd, Maria has the advantage
            # determine which player startsthe game
            if x % 2 == 0:
                # if x is even, Ben starts the game
                ben_wins += 1
            else:
                # if x is odd, Maria starts the game
                maria_wins += 1
    
    # determine the winner of the game
    if maria_wins < ben_wins:
        return "Maria"
    elif ben_wins < maria_wins:
        return "Ben"
    else:
        return None
