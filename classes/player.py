import utils.utils

class Player:
    def __init__(self, name="Player", money=0, parent=None):
        self.name = name
        self.money = money
        self.current_place = 0
        self.state = 'Active'
        self.parent = parent
    
    def move(self, nr_spaces=utils.utils.dice(), max_place=40):
        starting_point = self.current_place
        self.current_place += nr_spaces
        if self.current_place >= max_place:
            self.current_place -= max_place
        ending_point = self.current_place
        
        if self.parent != None:
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
        
    def all_owned_property(self):
        result = []
        for i in self.paretn.tiles:
            if i.type=='PropertyTile' and i.owner==self:
                result.append(i)
        return result
    
    def active_morgaged_property(self):
        result_active = []
        result_morgaged = []
        all_properties = self.all_active_property()
        for i in all_properties:
            if not i.is_morgaged:
                result_active.append(i)
            else:
                result_morgaged.append(i)
        return result_active, result_morgaged