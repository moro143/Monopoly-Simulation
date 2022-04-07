
class Tile:
    """_summary_
    """

    def __init__(self, name='Unknown', across_active=None):
        self.name = name
        self.across_active = across_active
        self.type = 'Tile'


class ProperyTile(Tile):
    """_summary_

    :param Tile: _description_
    :type Tile: _type_
    """

    def __init__(self, name='Unknown',
                 basic_price=0,
                 property_class='Unknown',
                 rent='0|0',
                 morgage_value=0,
                 upgrade_cost='0|0',
                 across_active=None):
        """_summary_

        :param name: _description_, defaults to 'Unknown'
        :type name: str, optional
        :param basic_price: _description_, defaults to 0
        :type basic_price: int, optional
        :param property_class: _description_, defaults to 'Unknown'
        :type property_class: str, optional
        :param rent: _description_, defaults to '0|0'
        :type rent: str, optional
        :param morgage_value: _description_, defaults to 0
        :type morgage_value: int, optional
        :param upgrade_cost: _description_, defaults to '0|0'
        :type upgrade_cost: str, optional
        :param across_active: _description_, defaults to None
        :type across_active: _type_, optional
        """

        super().__init__(name=name, across_active=across_active)
        self.basic_price = basic_price
        self.property_class = property_class
        self.rent_str_list(rent)
        self.morgage_value = morgage_value

        if upgrade_cost != '':
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
        """_summary_

        :param rent: _description_
        :type rent: _type_
        """
        self.rent = []
        if rent != '':
            rent = rent.split('|')
            for i in rent:
                self.rent.append([int(x) for x in (i.split('/'))])

    def calculate_current_rent(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        for i, e in reversed(list(enumerate(self.current_upgrade))):
            if i == 0:
                return self.rent[i][e]
            if e != 0:
                return self.rent[i][e-1]
        return -1
