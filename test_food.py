import unittest
from Food import Food


class TestFood(unittest.TestCase):
    def test_get_name(self):
        food = Food('hotdog', ['mustard'])
        self.assertEqual(food.get_name(), 'hotdog')

    def test_get_total(self):
        food = Food('ice cream', ['caramel sauce', 'chocolate sauce'])
        self.assertEqual(food.get_total(), 4)

    def test_get_num_toppings(self):
        food = Food('ice cream', ['caramel sauce', 'chocolate sauce'])
        self.assertEqual(food.get_num_toppings(), 2)

    def test_get_toppings(self):
        food = Food('ice cream', ['caramel sauce', 'chocolate sauce'])
        self.assertEqual(food.get_toppings(), [
                         'caramel sauce', 'chocolate sauce'])

    def test_set_toppings(self):
        food = Food('ice cream', ['caramel sauce', 'chocolate sauce'])
        food.set_toppings(['whipped cream'])
        self.assertEqual(food.get_toppings(), ['whipped cream'])

    def test_add_topping(self):
        food = Food('ice cream', ['caramel sauce', 'chocolate sauce'])
        food.add_topping('whipped cream')
        self.assertEqual(food.get_toppings(), [
                         'caramel sauce', 'chocolate sauce', 'whipped cream'])
