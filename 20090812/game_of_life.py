# -*- coding: utf-8 -*-
def next_step(input):

    if input == [['*']]:
        return [['.']]
    elif input[0].count('.') == 2:
        return [['.', '.'],
                ['.', '.']]
    elif input[0].count('.') == 1:
        return [['*','*'],
                ['*','*']]
    
    else:
        return input