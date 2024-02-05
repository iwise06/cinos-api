import unittest
from Order import Order
from Drink import Drink


class TestOrder(unittest.TestCase):
    def test_get_total(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'large')])
        self.assertEqual(order.get_total(), 4.15)

    def test_get_items(self):
        order = Order([Drink('water', ['lemon', 'cherry'])])
        self.assertEqual(order.get_items(), [
                         Drink('water', ['lemon', 'cherry'])])

    def test_get_num_items(self):
        order = Order([Drink('water', ['lemon', 'cherry']),
                      Drink('water', ['lemon', 'cherry'])])
        self.assertEqual(order.get_num_items(), 2)

    def test_add_item(self):
        order = Order([Drink('water', ['lemon', 'cherry'])])
        order.add_item(Drink('water', ['lemon', 'cherry']))
        self.assertEqual(
            order.get_items(), [
                Drink('water', ['lemon', 'cherry']),
                Drink('water', ['lemon', 'cherry'])])

    def test_remove_item(self):
        order = Order([Drink('water', ['lemon', 'cherry']),
                      Drink('water', ['lemon', 'cherry'])])
        order.remove_item(1)
        self.assertEqual(order.get_items(), [
                         Drink('water', ['lemon', 'cherry'])])
