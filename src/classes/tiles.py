
class Tile:
    def __init__(self, name='Unknown', across_active=None):
        self.name = name
        self.across_active = across_active
        self.type = 'Tile'
        

class ProperyTile(Tile):
    def __init__(self, name='Unknown', 
                 basic_price=0, 
                 property_class='Unknown', 
                 rent='0|0', 
                 morgage_value=0,
                 upgrade_cost='0|0',
                 across_active=None):
        
        super().__init__(name=name, across_active=across_active)
        self.basic_price = basic_price
        self.property_class = property_class
        self.rent_str_list(rent)
        self.morgage_value = morgage_value
        
        if upgrade_cost!='':
            self.upgrade_costs = [int(x) for x in upgrade_cost.split('|')]
        else:
            self.upgrade_costs = []
        
        self.is_morgaged = False
        self.current_upgrade = []
        for _ in self.upgrade_costs:
            self.current_upgrade.append(0)
        self.owner = None
        self.type = 'PropertyTile'
        
    def rent_str_list(self, rent):
        self.rent = []
        if rent!='':
            rent = rent.split('|')
            for i in rent:
                self.rent.append([int(x) for x in (i.split('/'))])
    
    def calculate_current_rent(self):
        for i, e in reversed(list(enumerate(self.current_upgrade))):
            if i==0:
                return self.rent[i][e]
            elif e!=0:
                return self.rent[i][e-1]
