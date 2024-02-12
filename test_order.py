import unittest
from Order import Order
from Drink import Drink


class TestOrder(unittest.TestCase):
    def test_get_total(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'large')])
        self.assertEqual(order.get_total(), 4.15)

    def test_get_receipt(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'large')])
        print(order.get_receipt())

        self.assertEqual(order.get_receipt(), {
            'drink_amount': 2,
            'subtotal': 4.15,
            'tax': round(4.15 * .0725, 2),
            'total': 4.15 + round(4.15 * .0725, 2),
            'drinks': [
                {
                    'base': Drink('water', ['lemon', 'cherry'], 'small').get_base(),
                    'flavors': Drink('water', ['lemon', 'cherry'], 'small').get_flavors(),
                    'size': Drink('water', ['lemon', 'cherry'], 'small').get_size(),
                    'cost': Drink('water', ['lemon', 'cherry'], 'small').get_total()
                },
                {
                    'base': Drink('water', ['lemon', 'cherry'], 'large').get_base(),
                    'flavors': Drink('water', ['lemon', 'cherry'], 'large').get_flavors(),
                    'size': Drink('water', ['lemon', 'cherry'], 'large').get_size(),
                    'cost': Drink('water', ['lemon', 'cherry'], 'large').get_total()
                }
            ],
        })

    def test_get_items(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small')])
        self.assertEqual(order.get_items(), [
                         Drink('water', ['lemon', 'cherry'], 'small')])

    def test_get_num_items(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'small')])
        self.assertEqual(order.get_num_items(), 2)

    def test_add_item(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small')])
        order.add_item(Drink('water', ['lemon', 'cherry'], 'small'))
        self.assertEqual(
            order.get_items(), [
                Drink('water', ['lemon', 'cherry'], 'small'),
                Drink('water', ['lemon', 'cherry'], 'small')])

    def test_remove_item(self):
        order = Order([Drink('water', ['lemon', 'cherry'], 'small'),
                      Drink('water', ['lemon', 'cherry'], 'small')])
        order.remove_item(1)
        self.assertEqual(order.get_items(), [
                         Drink('water', ['lemon', 'cherry'], 'small')])
