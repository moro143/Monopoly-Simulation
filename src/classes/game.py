from ..utils import resources_import
from . import player, tiles


class Game:
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        self.tiles = []
        self.players = []
        self.across_active = []

    def tiles_import(self, filename='./src/resources/board_tiles.csv'):
        """_summary_

        :param filename: _description_, defaults to './src/resources/board_tiles.csv'
        :type filename: str, optional
        """
        tiles_list = resources_import.board_tiles(filename=filename)
        for i in tiles_list:
            if i["Property"] == 'Yes':
                tile = tiles.ProperyTile(name=i['Name'],
                                         basic_price=i["Base Price"],
                                         property_class=i["Class"],
                                         rent=i['Rent'],
                                         morgage_value=i["Morgage Value"],
                                         upgrade_cost=i['Upgrade Cost'],
                                         across_active=i['Across Active'])
            else:
                tile = tiles.Tile(name=i['Name'],
                                  across_active=i['Across Active'])
            self.tiles.append(tile)

    def add_player(self, base_money=0, name="Player"):
        """_summary_

        :param base_money: _description_, defaults to 0
        :type base_money: int, optional
        :param name: _description_, defaults to "Player"
        :type name: str, optional
        """
        self.players.append(player.Player(name, base_money, parent=self))

    def round(self):
        """_summary_
        """
        for p_l in self.players:
            if p_l.state == 'Active':
                p_l.move()

    def find_across_active(self):
        """_summary_
        """
        for idx, tile in enumerate(self.tiles):
            if tile.across_active:
                self.across_active.append(idx)
