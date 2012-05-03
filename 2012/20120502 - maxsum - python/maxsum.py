def maxsum(bets):
    maximum = None
    for i in range(len(bets)):
        for j in range(i, len(bets)):
            maximum = max(maximum, sum(bets[i:j+1]))
    
    return maximum
 
