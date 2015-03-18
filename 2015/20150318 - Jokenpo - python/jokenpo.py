def jokenpo(play1, play2):
    if play1 == play2:
        return 'draw'
    if play2 == 'rock' :
        return 'play2'
    if play1 == 'lizard':
        return 'play1'
    return 'play2' 