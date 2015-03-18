def jokenpo(play1, play2):
    try:
        rock = [play1, play2].index('rock') + 1
        return 'play' + str(rock)
    except:
        pass


    if play1 == play2:
        return 'draw'
    if play1 == 'lizard':
        return 'play1'
    return 'play2' 