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
        