import unittest
from api.Order import Order
from api.Drink import Drink
from api.Food import Food
from api.IceStorm import IceStorm


class TestOrder(unittest.TestCase):
    def test_get_total(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'large'),
                      Food('ice cream', ['caramel sauce', 'chocolate sauce'])])
        self.assertEqual(order.get_total(), 8.15)

    def test_get_receipt(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'large'),
                      Food('ice cream', ['caramel sauce', 'chocolate sauce']), IceStorm('chocolate', ['dig dogs', 'cherry'])])

        self.assertEqual(order.get_receipt(), {
            'item_amount': 4,
            'subtotal': 12.15,
            'tax': round(12.15 * .0725, 2),
            'total': 12.15 + round(12.15 * .0725, 2),
            'items': [
                {
                    'type': 'drink',
                    'base': Drink('water', ['lemon', 'cherry'], 'small').get_base(),
                    'flavors': Drink('water', ['lemon', 'cherry'], 'small').get_flavors(),
                    'size': Drink('water', ['lemon', 'cherry'], 'small').get_size(),
                    'cost': Drink('water', ['lemon', 'cherry'], 'small').get_total()
                },
                {
                    'type': 'drink',
                    'base': Drink('water', ['lemon', 'cherry'], 'large').get_base(),
                    'flavors': Drink('water', ['lemon', 'cherry'], 'large').get_flavors(),
                    'size': Drink('water', ['lemon', 'cherry'], 'large').get_size(),
                    'cost': Drink('water', ['lemon', 'cherry'], 'large').get_total()
                },
                {
                    'type': 'food',
                    'base': Food('ice cream', ['caramel sauce', 'chocolate sauce']).get_base(),
                    'toppings': Food('ice cream', ['caramel sauce', 'chocolate sauce']).get_toppings(),
                    'cost': Food('ice cream', ['caramel sauce', 'chocolate sauce']).get_total()
                },
                {
                    'type': 'icestorm',
                    'base': IceStorm('chocolate', ['dig dogs', 'cherry']).get_base(),
                    'toppings': IceStorm('chocolate', ['dig dogs', 'cherry']).get_toppings(),
                    'cost': IceStorm('chocolate', ['dig dogs', 'cherry']).get_total()
                }
            ]
        })

    def test_get_items(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'large'),
                      Food('ice cream', ['caramel sauce', 'chocolate sauce'])])
        self.assertEqual(order.get_items(), [
                         Drink('water', ['lemon', 'cherry'], 'small'),
                         Drink('water', ['lemon', 'cherry'], 'large'),
                         Food('ice cream', [
                              'caramel sauce', 'chocolate sauce'])
                         ])

    def test_get_num_items(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'small'),
                      Food('ice cream', ['caramel sauce', 'chocolate sauce'])])
        self.assertEqual(order.get_num_items(), 3)

    def test_add_item(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small')])
        order.add_item(Drink('water', ['lemon', 'cherry'], 'small'))
        order.add_item(Food('ice cream', ['caramel sauce', 'chocolate sauce']))
        self.assertEqual(
            order.get_items(), [
                Drink('water', ['lemon', 'cherry'], 'small'),
                Drink('water', ['lemon', 'cherry'], 'small'),
                Food('ice cream', ['caramel sauce', 'chocolate sauce'])])

    def test_remove_item(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'small'),
                      Food('ice cream', ['caramel sauce', 'chocolate sauce'])])
        order.remove_item(1)
        self.assertEqual(order.get_items(), [
                         Drink('water', ['lemon', 'cherry'], 'small'),
                         Food('ice cream', ['caramel sauce', 'chocolate sauce'])])
