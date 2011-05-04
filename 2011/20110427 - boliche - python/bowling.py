def has_spare(game):
    return sum(game[0]) == 10 or sum(game[1]) == 10

def find_spare(game):
    if sum(game[0]) == 10:
        return 0
    if sum(game[1]) == 10:
        return 1
    
def has_strike(game):
    return game[0] == (10,)
        
def find_strike(game):
    if game[0] == (10,):
        return 0


def bowling(game):
    score = sum(map(sum, game))
        
    if has_strike(game):
        score += sum(game[find_strike(game)+1] + game[find_strike(game)+2])
        
    elif has_spare(game):
        score += sum(game[find_spare(game)+1])

    return score

