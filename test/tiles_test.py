import unittest

from src.classes import tiles


class TestTile(unittest.TestCase):
    """_summary_

    :param unittest: _description_
    :type unittest: _type_
    """

    def test_init_no_input(self):
        """_summary_
        """
        puppet_tile = tiles.Tile()

        self.assertEqual(puppet_tile.name, 'Unknown',
                         msg='Init no input Tile - name')
        self.assertEqual(puppet_tile.type, 'Tile',
                         msg='Init no input Tile - type')
        self.assertEqual(puppet_tile.across_active, None,
                         msg='Init no input Tile - actoss_active')

        puppet_property = tiles.ProperyTile()
        self.assertEqual(puppet_property.name, 'Unknown',
                         msg='Init no input ProperyTile - name')
        self.assertEqual(puppet_property.type, 'PropertyTile',
                         msg='Init no input ProperyTile - type')
        self.assertEqual(puppet_property.across_active, None,
                         msg='Init no input ProperyTile - actoss_active')
        self.assertEqual(puppet_property.basic_price, 0,
                         msg='Init no input ProperyTile - basic_price')
        self.assertEqual(puppet_property.property_class, 'Unknown',
                         msg='Init no input ProperyTile - property_class')
        self.assertEqual(puppet_property.rent, [
                         [0], [0]], msg='Init no input ProperyTile - rent')
        self.assertEqual(puppet_property.morgage_value, 0,
                         msg='Init no input ProperyTile - morgage_value')
        self.assertEqual(puppet_property.current_upgrade, [
                         0, 0], msg='Init no input ProperyTile - current_upgrade')
        self.assertEqual(puppet_property.owner, None,
                         msg='Init no input ProperyTile - owner')
        self.assertEqual(puppet_property.is_morgaged, False,
                         msg='Init no input ProperyTile - is_morgaged')
        self.assertEqual(puppet_property.upgrade_costs, [
                         0, 0], msg='Init no input ProperyTile - upgrade_cost')

    def test_init_input(self):
        """_summary_
        """
        puppet_tile = tiles.Tile(name='Tile name', across_active='Give*300')

        self.assertEqual(puppet_tile.name, 'Tile name',
                         msg='Init input Tile - name')
        self.assertEqual(puppet_tile.type, 'Tile',
                         msg='Init input Tile - type')
        self.assertEqual(puppet_tile.across_active, 'Give*300',
                         msg='Init input Tile - actoss_active')

        puppet_property = tiles.ProperyTile(name='Property name',
                                            basic_price=999,
                                            property_class='blue',
                                            rent='1/2/3/4/5/6|10',
                                            morgage_value=999,
                                            upgrade_cost='40|50',
                                            across_active='Give*400')
        self.assertEqual(puppet_property.name, 'Property name',
                         msg='Init input ProperyTile - name')
        self.assertEqual(puppet_property.type, 'PropertyTile',
                         msg='Init input ProperyTile - type')
        self.assertEqual(puppet_property.across_active, 'Give*400',
                         msg='Init input ProperyTile - actoss_active')
        self.assertEqual(puppet_property.basic_price, 999,
                         msg='Init input ProperyTile - basic_price')
        self.assertEqual(puppet_property.property_class, 'blue',
                         msg='Init input ProperyTile - property_class')
        self.assertEqual(puppet_property.rent, [[1, 2, 3, 4, 5, 6], [
                         10]], msg='Init input ProperyTile - rent')
        self.assertEqual(puppet_property.morgage_value, 999,
                         msg='Init input ProperyTile - morgage_value')
        self.assertEqual(puppet_property.current_upgrade, [
                         0, 0], msg='Init input ProperyTile - current_upgrade')
        self.assertEqual(puppet_property.owner, None,
                         msg='Init input ProperyTile - owner')
        self.assertEqual(puppet_property.is_morgaged, False,
                         msg='Init input ProperyTile - is_morgaged')
        self.assertEqual(puppet_property.upgrade_costs, [
                         40, 50], msg='Init input ProperyTile - upgrade_cost')

    def test_calculate_current_rent(self):
        """_summary_
        """
        puppet_property = tiles.ProperyTile(name='Property name',
                                            basic_price=999,
                                            property_class='blue',
                                            rent='1/2/3/4/5/6|10',
                                            morgage_value=999,
                                            upgrade_cost='40|50',
                                            across_active='Give*400')
        puppet_property.current_upgrade = [6, 1]
        self.assertEqual(puppet_property.calculate_current_rent(),
                         10, msg='Calculate current rent - hotel')

        puppet_property.current_upgrade = [3, 0]
        self.assertEqual(puppet_property.calculate_current_rent(),
                         4, msg='Calculate current rent - motel')

        puppet_property.current_upgrade = [0, 0]
        self.assertEqual(puppet_property.calculate_current_rent(),
                         1, msg='Calculate current rent - motel')


if __name__ == '__main__':
    unittest.main()
