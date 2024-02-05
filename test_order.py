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
        self.assertEqual(order.get_recepit(), {
                        drink_amount: 2,
                        subtotal: 4.15,
                        tax: round(4.15 * .0725, 2),
                        total: 4.15 + round(4.15 * .0725, 2),
                        drinks: [
                            {
                                drink: Drink('water', ['lemon', 'cherry'], 'small'),
                                cost: Drink('water', ['lemon', 'cherry'], 'small').get_total()
                            }, 
                            {
                                drink: Drink('water', ['lemon', 'cherry'], 'large'),
                                cost: Drink('water', ['lemon', 'cherry'], 'large').get_total()
                            }
                        ],
                    })

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
