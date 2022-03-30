import classes.game
import argparse


parser = argparse.ArgumentParser(description='Monopoly Simulation.')
parser.add_argument('-r', 
                    action='store_true', 
                    help='Run monopoly simulation')

args = parser.parse_args()

if __name__ == '__main__':
    if args.r:
        game = classes.game.Game()
        game.tiles_import()
        game.add_player(1000, "Player 1")
        game.add_player(1000, "Player 2")
        game.add_player(1000, "Player 3")
        game.add_player(1000, "Player 4")
        game.find_across_active()
        
        while True:
            game.round()
