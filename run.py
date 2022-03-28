from ctypes import util
import utils.resources_import
import classes.tiles
import classes.game

if __name__ == '__main__':
    game = classes.game.Game()
    game.tiles_import()
    game.add_player(1000, "Player 1")
    game.add_player(1000, "Player 2")
    game.add_player(1000, "Player 3")
    game.add_player(1000, "Player 4")
    game.find_across_active()
    
    
    