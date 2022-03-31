

import unittest
from src.classes import player

class TestPlayer(unittest.TestCase):
    
    def test_init_noinput(self):
        player_puppet = player.Player()
        
        self.assertEqual(player_puppet.name, "Player", msg='Init no input - name')
        self.assertEqual(player_puppet.money, 0, msg='Init no input - money')
        self.assertEqual(player_puppet.current_place, 0, msg='Init no input - current_place')
        self.assertEqual(player_puppet.state, "Active", msg='Init no input - status')
        self.assertEqual(player_puppet.parent, None, msg='Init no input - parent')
    
    def test_init_right_input(self):
        player_puppet = player.Player("Puppet", 200)
        
        self.assertEqual(player_puppet.name, "Puppet", msg='Init right input - name')
        self.assertEqual(player_puppet.money, 200, msg='Init right input - money')
    
    def test_move_no_parent(self):
        player_puppet = player.Player()
        player_puppet.move(nr_spaces=6, max_place=8)
        
        self.assertEqual(player_puppet.current_place, 6, msg='Move no parent - current_place(normal)')
        player_puppet.move(nr_spaces=6, max_place=8)
        self.assertEqual(player_puppet.current_place, 4, msg='Move no parent - current_place(through start)')
    
    def test_across_active_handler(self):
        pass
    
    def test_all_owned_property(self):
        pass
    
    def test_active_morgaged_property(self):
        pass
    
if __name__=='__main__':
    unittest.main()