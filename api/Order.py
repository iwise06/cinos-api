"""Order class that contains a list of drinks and food as well as methods related to the order.

This class contains a list of drinks and food as well as methods to get the total cost of the order, get the receipt, 
get the items in the order, get the number of items in the order, add an item to the order, and remove an item from the order.

Typical usage example:
    order = Order([Drink('water', ['lemon', 'cherry'], 'small'), Food('ice cream', ['caramel sauce', 'chocolate sauce']), IceStorm('chocolate', ['dig dogs', 'cherry'])])
"""

from api.Drink import Drink
from api.Food import Food
from api.IceStorm import IceStorm


class Order:
    """Class that contains a list of drinks and food as well as methods related to the order.

    Attributes:
        items: A list of items in the order.
    """

    def __init__(self, items):
        """Initializes the order with a list of items.

        Args:
            items: A list of items in the order.
        """
        self._items = items

    def get_items(self):
        """Returns the list of items in the order."""
        return self._items

    def get_num_items(self):
        """Returns the number of items in the order."""
        return len(self._items)

    def get_total(self):
        """Returns the total cost of the order."""
        total = 0
        for item in self._items:
            total += item.get_total()

        return total

    def add_item(self, item):
        """Adds a item to the order.

        Args:
            item: An item to be added to the order.

        Raises:
            ValueError: If the argument is not a drink or food class.
        """

        # Make sure the argument is a drink or food class
        if not isinstance(item, (Drink, Food, IceStorm)):
            raise ValueError('Only drinks and food can be added to an order')

        self._items.append(item)

    def remove_item(self, index):
        """Removes a item from the order.

        Args:
            index: The index of the item to be removed from the order.

        Raises:
            ValueError: If the index is invalid.
        """
        if index < 0 or index >= len(self._items):
            raise ValueError('Invalid index')

        self._items.pop(index)

    def get_receipt(self):
        """Returns a dictionary containing the receipt for the order."""
        return {
            'item_amount': self.get_num_items(),
            'subtotal': self.get_total(),
            'tax': round(self.get_total() * .0725, 2),
            'total': self.get_total() + round(self.get_total() * .0725, 2),
            'items': [
                {
                    'type': 'drink',
                    'base': item.get_base(),
                    'flavors': item.get_flavors(),
                    'size': item.get_size(),
                    'cost': item.get_total()
                } if isinstance(item, Drink) else
                {
                    'type': 'food',
                    'base': item.get_base(),
                    'toppings': item.get_toppings(),
                    'cost': item.get_total()
                } if isinstance(item, Food) else
                {
                    'type': 'icestorm',
                    'base': item.get_base(),
                    'toppings': item.get_toppings(),
                    'cost': item.get_total()
                } for item in self._items
            ],
        }
