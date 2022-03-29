import utils.utils

class Player:
    def __init__(self, name="Player", money=0, parent=None):
        self.name = name
        self.money = money
        self.current_place = 0
        self.state = 'Active'
        self.parent = parent
    
    def move(self, max_place=40):
        starting_point = self.current_place
        self.current_place += utils.utils.dice()
        if self.current_place >= max_place:
            self.current_place -= max_place
        ending_point =self.current_place
        
        self.across_active_handler(self.parent, starting_point, ending_point)
        
        possible_moves = {}
        if self.parent.tiles[ending_point].type == "PropertyTile":
            if self.parent.tiles[ending_point].owner == None:
                possible_moves['Buy'] = self.parent.tiles[ending_point].basic_price
            else:
                pass # Take money from player, give it to other player
        else:
            pass
    
    def across_active_handler(self, parent, starting_point, ending_point):    
        # Across actives handler
        for i in parent.across_active:
            if starting_point<ending_point:
                if starting_point < i and i >= ending_point:
                    active = parent.tiles[i].across_active.split('*')
                    if active[0] == 'Give':
                        self.money += int(active[1])
            else:
                if starting_point < i or i <= ending_point:
                    active = parent.tiles[i].across_active.split('*')
                    if active[0] == 'Give':
                        self.money += int(active[1])
        
        