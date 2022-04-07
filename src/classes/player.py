from ..utils import utils


class Player:
    """_summary_
    """

    def __init__(self, name="Player", money=0, parent=None):
        """Init player

        :param name: Name of a player, defaults to "Player"
        :type name: str, optional
        :param money: Amount of money, defaults to 0
        :type money: int, optional
        :param parent: Game of player, defaults to None
        :type parent: Game, optional
        """
        self.name = name
        self.money = money
        self.current_place = 0
        self.state = 'Active'
        self.parent = parent

    def move(self, nr_spaces=utils.dice(), max_place=40):
        """Move player on board

        :param nr_spaces: How many spaces does player move, defaults to utils.dice()
        :type nr_spaces: int, optional
        :param max_place: How many tiles does board have, defaults to 40
        :type max_place: int, optional
        """
        starting_point = self.current_place
        self.current_place += nr_spaces
        if self.current_place >= max_place:
            self.current_place -= max_place
        ending_point = self.current_place

        if self.parent is not None:
            self.across_active_handler(
                self.parent, starting_point, ending_point)

            possible_moves = {}
            if self.parent.tiles[ending_point].type == "PropertyTile":
                if self.parent.tiles[ending_point].owner is None:
                    possible_moves['Buy'] = self.parent.tiles[ending_point].basic_price
                else:
                    payment = self.parent.tiles[ending_point].calculate_current_rent(
                    )
                    if payment <= self.money:
                        self.money -= payment
                        self.parent.tiles[ending_point].owner.money += payment
                    else:
                        pass  # function when not enought money
            else:
                pass

    def across_active_handler(self, starting_point, ending_point):
        """Function to handle tiles with actives on crossing them

        :param starting_point: Where player started before moving
        :type starting_point: int
        :param ending_point: Where player ended after moving
        :type ending_point: int
        """
        # Across actives handler
        for i in self.parent.across_active:
            if starting_point < ending_point:
                if starting_point < i and i >= ending_point:
                    active = self.parent.tiles[i].across_active.split('*')
                    if active[0] == 'Give':
                        self.money += int(active[1])
            else:
                if starting_point < i or i <= ending_point:
                    active = self.parent.tiles[i].across_active.split('*')
                    if active[0] == 'Give':
                        self.money += int(active[1])

    def all_owned_property(self):
        """Returns all property owned by player

        :return: List of properties owned by player
        :rtype: list of Tiles
        """
        result = []
        for i in self.parent.tiles:
            if i.type == 'PropertyTile' and i.owner == self:
                result.append(i)
        return result

    def active_morgaged_property(self):
        """Return active morgaged property

        :return: _description_
        :rtype: _type_
        """
        result_active = []
        result_morgaged = []
        all_properties = self.all_active_property()
        for i in all_properties:
            if not i.is_morgaged:
                result_active.append(i)
            else:
                result_morgaged.append(i)
        return result_active, result_morgaged

    def all_active_property(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        active_properties = []
        for tile in self.all_owned_property():
            if not tile.is_morgaged:
                active_properties.append(tile)
        return active_properties
