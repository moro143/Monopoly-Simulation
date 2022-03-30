from classes import tiles, player
from utils import resources_import

class Game:
    def __init__(self):
        self.tiles = []
        self.players = []
        self.across_active = []
        
    def tiles_import(self, filename='resources/board_tiles.csv'):
        tiles_list = resources_import.board_tiles(filename=filename)
        for i in tiles_list:
            if i["Property"]=='Yes':
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
        self.players.append(player.Player(name, base_money, parent=self))
    
    def round(self):
        for player in self.players:
            if player.state == 'Active':
                player.move()
    
    def find_across_active(self):
        for idx, tile in enumerate(self.tiles):
            if tile.across_active:
                self.across_active.append(idx)
            