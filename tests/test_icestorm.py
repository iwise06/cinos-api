import unittest
from api.IceStorm import IceStorm


class TestIceStorm(unittest.TestCase):
    def test_get_base(self):
        icestorm = IceStorm('chocolate', ['dig dogs'])
        self.assertEqual(icestorm.get_base(), 'chocolate')

    def test_get_total(self):
        icestorm = IceStorm('chocolate', ['dig dogs'])
        self.assertEqual(icestorm.get_total(), 4)

    def test_get_num_toppings(self):
        icestorm = IceStorm('chocolate', ['dig dogs', 'cherry'])
        self.assertEqual(icestorm.get_num_toppings(), 2)

    def test_get_toppings(self):
        icestorm = IceStorm('chocolate', ['dig dogs', 'cherry'])
        self.assertEqual(icestorm.get_toppings(), ['dig dogs', 'cherry'])

    def test_set_toppings(self):
        icestorm = IceStorm('chocolate', ['dig dogs', 'cherry'])
        icestorm.set_toppings(['whipped cream'])
        self.assertEqual(icestorm.get_toppings(), ['whipped cream'])

    def test_add_topping(self):
        icestorm = IceStorm('chocolate', ['caramel sauce', 'chocolate sauce'])
        icestorm.add_topping('whipped cream')
        self.assertEqual(icestorm.get_toppings(), [
                         'caramel sauce', 'chocolate sauce', 'whipped cream'])
