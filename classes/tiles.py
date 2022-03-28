
class Tile:
    def __init__(self, name='Unknown', across_active=None):
        self.name = name
        self.across_active = across_active
        

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
        self.upgrade_costs = upgrade_cost.split('|')
        
        self.is_morgaged = False
        self.current_upgrade = []
        for _ in self.upgrade_costs:
            self.current_upgrade.append(0)
        self.owner = None
    
    def rent_str_list(self, rent):
        self.rent = []
        rent = rent.split('|')
        for i in rent:
            self.rent.append((i.split('/')))
