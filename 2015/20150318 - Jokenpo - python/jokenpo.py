def jokenpo(play1, play2):
    try:
        rock = [play1, play2].index('rock') + 1
        return 'play' + str(rock)
    except:
        pass

    plays = ['scissor'
            , 'paper'
            , 'rock'
            , 'lizard'
            , 'spock'   ]

    index_1 = plays.index(play1)

    if plays[(index_1 + 1) % 5] == play2:
        return 'play1'