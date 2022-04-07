from .classes import game


def run():
    """_summary_
    """
    game1 = game.Game()
    game1.tiles_import()
    game1.add_player(1000, "Player 1")
    game1.add_player(1000, "Player 2")
    game1.add_player(1000, "Player 3")
    game1.add_player(1000, "Player 4")
    game1.find_across_active()

    while True:
        game1.round()
        print(game1.players[0].current_place)
