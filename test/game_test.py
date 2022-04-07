import unittest

from src.classes.game import Game


class TestGame(unittest.TestCase):
    """_summary_

    :param unittest: _description_
    :type unittest: _type_
    """
    @classmethod
    def setUpClass(cls):
        """_summary_
        """
        cls.puppet_game = Game()

    def test_init(self):
        """_summary_
        """
        self.assertEqual(self.puppet_game.tiles, [], msg='Init - tiles')
        self.assertEqual(self.puppet_game.players, [], msg='Init - players')
        self.assertEqual(self.puppet_game.across_active,
                         [], msg='Init - across_active')

    def test_tiles_import(self):
        """_summary_
        """
        self.puppet_game.tiles_import()

        self.assertEqual(
            self.puppet_game.tiles[0].name, 'Go', msg="Tiles import - name tile 0")
        self.assertEqual(
            self.puppet_game.tiles[-1].name, 'Boardwalk', msg="Tiles import - name tile -1")
        self.assertEqual(
            self.puppet_game.tiles[23].name, 'Indiana Avenue', msg="Tiles import - name tile 23")

    def test_add_player_no_input(self):
        """_summary_
        """
        self.puppet_game.add_player()
        self.puppet_game.add_player()

        self.assertEqual(
            self.puppet_game.players[0].name, "Player", msg='Add player no input - name player 0')
        self.assertEqual(
            self.puppet_game.players[1].name, "Player", msg='Add player no input - name player 1')
        self.assertEqual(
            self.puppet_game.players[0].money, 0, msg='Add player no input - money player 0')
        self.assertEqual(
            self.puppet_game.players[1].money, 0, msg='Add player no input - money player 1')


if __name__ == '__main__':
    unittest.main()
