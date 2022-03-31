import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import unittest
from classes import game

class TestGame(unittest.TestCase):
    def test_init(self):
        puppet_game = game.Game()
        
        self.assertEqual(puppet_game.tiles, [], msg='Init - tiles')
        self.assertEqual(puppet_game.players, [], msg='Init - players')
        self.assertEqual(puppet_game.across_active, [], msg='Init - across_active')
    
    def test_tiles_import(self):
        puppet_game = game.Game()
        puppet_game.tiles_import()
        
        self.assertEqual(puppet_game.tiles[0].name, 'Go', msg="Tiles import - name tile 0")
        self.assertEqual(puppet_game.tiles[-1].name, 'Boardwalk', msg="Tiles import - name tile -1")
        self.assertEqual(puppet_game.tiles[23].name, 'Indiana Avenue', msg="Tiles import - name tile 23")

    def test_add_player_no_input(self):
        puppet_game = game.Game()
        puppet_game.add_player()
        puppet_game.add_player()
        
        self.assertEqual(puppet_game.players[0].name, "Player", msg='Add player no input - name player 0')
        self.assertEqual(puppet_game.players[1].name, "Player", msg='Add player no input - name player 1')
        self.assertEqual(puppet_game.players[0].money, 0, msg='Add player no input - money player 0')
        self.assertEqual(puppet_game.players[1].money, 0, msg='Add player no input - money player 1')
    
if __name__=='__main__':
    unittest.main()