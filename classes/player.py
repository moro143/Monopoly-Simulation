import utils.utils

class Player:
    def __init__(self, name="Player", money=0):
        self.name = name
        self.money = money
        self.current_place = 0
        self.state = 'Active'
    
    def move(self, parent, max_place=40):
        starting_point = self.current_place
        self.current_place += utils.utils.dice()
        if self.current_place >= max_place:
            self.current_place -= max_place
        ending_point =self.current_place
        
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