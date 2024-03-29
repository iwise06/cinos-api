import unittest
from api.Drink import Drink


class TestDrink(unittest.TestCase):
    def test_get_base(self):
        drink = Drink('water', ['lemon', 'cherry'], 'small')
        self.assertEqual(drink.get_base(), 'water')

    def test_get_total(self):
        drink = Drink('water', ['lemon', 'cherry'], 'large')
        self.assertEqual(drink.get_total(), 2.35)

    def test_get_num_flavors(self):
        drink = Drink('water', ['lemon', 'cherry'], 'small')
        self.assertEqual(drink.get_num_flavors(), 2)

    def test_get_flavors(self):
        drink = Drink('water', ['lemon', 'cherry'], 'small')
        self.assertEqual(drink.get_flavors(), ['lemon', 'cherry'])

    def test_set_flavors(self):
        drink = Drink('water', ['lemon', 'cherry'], 'small')
        drink.set_flavors(['strawberry'])
        self.assertEqual(drink.get_flavors(), ['strawberry'])

    def test_add_flavor(self):
        drink = Drink('water', ['lemon', 'cherry'], 'small')
        drink.add_flavor('strawberry')
        self.assertEqual(drink.get_flavors(), [
                         'lemon', 'cherry', 'strawberry'])

    def test_get_size(self):
        drink = Drink('water', ['lemon', 'cherry'], 'small')
        self.assertEqual(drink.get_size(), 'small')

    def test_set_size(self):
        drink = Drink('water', ['lemon', 'cherry'], 'large')
        drink.set_size('small')
        self.assertEqual(drink.get_size(), 'small')
