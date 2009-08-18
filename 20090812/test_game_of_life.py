# -*- coding: utf-8 -*-
import unittest
from game_of_life import *


class Test(unittest.TestCase):
    '''
    . = a dead cell
    * = live cell
    '''

    def test_1x1_alive_cell_dies(self):
        input = [['*']]
        
        self.assertEquals([['.']], next_step(input))
    
    def test_2x2_all_alive_cells_stay_alive(self):
        input = [['*', '*'],
                 ['*', '*']]
        
        self.assertEquals(input, next_step(input))
    
    def test_2x2_only_one_dead_revive(self):
        input = [['.', '*'],
                 ['*', '*']]
        all_alive = [['*', '*'],
                     ['*', '*']]
        self.assertEquals(all_alive, next_step(input))
        
    def test_2x2_two_cells_alive_and_two_cells_dead_all_die(self):
        input = [['.', '.'],
                 ['*', '*']]
        all_dead = [['.', '.'],
                    ['.', '.']]
        self.assertEquals(all_dead, next_step(input))
        
    def test_2x2_only_one_dead_revive2(self):
        input = [['*', '.'],
                 ['*', '*']]
        all_alive = [['*', '*'],
                     ['*', '*']]
        self.assertEquals(all_alive, next_step(input))
        
    def test_3x3_only_one_dead_at_the_center(self):
        input = [['*', '*', '*'],
                 ['*', '.', '*'],
                 ['*', '*', '*']]
                
        output = [['*', '*', '*'],
                 ['*', '.', '*'],
                 ['*', '*', '*']]
        self.assertEquals(output, next_step(input))
        
    def test_3x3_only_one_dead_at_the_corner(self):
        input = [['.', '*', '*'],
                 ['*', '*', '*'],
                 ['*', '*', '*']]
                
        output = [['*', '*', '*'],
                 ['*', '*', '*'],
                 ['*', '*', '*']]
        self.assertEquals(output, next_step(input))
        
unittest.main()