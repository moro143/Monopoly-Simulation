import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import unittest
from classes import player

class TestPlayer(unittest.TestCase):
    
    def test_init_noinput(self):
        player_puppet = player.Player()
        
        self.assertEqual(player_puppet.name, "Player", msg='No input - name')
        self.assertEqual(player_puppet.money, 0, msg='No input - money')
        self.assertEqual(player_puppet.current_place, 0, msg='No input - current_place')
        self.assertEqual(player_puppet.state, "Active", msg='No input - status')
        self.assertEqual(player_puppet.parent, None, msg='No input - parent')
    
    def test_init_right_input(self):
        player_puppet = player.Player("Puppet", 200)
        
        self.assertEqual(player_puppet.name, "Puppet", msg='Right input - name')
        self.assertEqual(player_puppet.money, 200, msg='Right input - money')
    
    def test_move(self):
        pass
    
    def test_across_active_handler(self):
        pass
    
    def test_all_owned_property(self):
        pass
    
    def test_active_morgaged_property(self):
        pass
    
if __name__=='__main__':
    unittest.main()