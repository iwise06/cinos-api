"""Order class that contains a list of drinks and methods related to the order.

This class contains a list of drinks and methods to get the total cost of the order, get the receipt, 
get the items in the order, get the number of items in the order, add an item to the order, and remove an item from the order.

Typical usage example:
    order = Order([Drink('water', ['lemon', 'cherry'], 'small'))
"""

from Drink import Drink


class Order:
    """Class that contains a list of drinks and methods related to the order.

    Attributes:
        drinks: A list of drinks in the order.
    """

    def __init__(self, drinks: list[Drink]):
        """Initializes the order with a list of drinks.

        Args:
            drinks: A list of drinks in the order.
        """
        self._drinks = drinks

    def get_items(self):
        """Returns the list of drinks in the order."""
        return self._drinks

    def get_num_items(self):
        """Returns the number of drinks in the order."""
        return len(self._drinks)

    def get_total(self):
        """Returns the total cost of the order."""
        total = 0
        for drink in self._drinks:
            total += drink.get_total()

        return total

    def add_item(self, drink):
        """Adds a drink to the order.

        Args:
            drink: A drink to be added to the order.

        Raises:
            ValueError: If the argument is not a drink class.
        """
        # Make sure the argument is a drink class
        if not isinstance(drink, Drink):
            raise ValueError('Only drinks can be added to an order')

        self._drinks.append(drink)

    def remove_item(self, index):
        """Removes a drink from the order.

        Args:
            index: The index of the drink to be removed from the order.

        Raises:
            ValueError: If the index is invalid.
        """
        if index < 0 or index >= len(self._drinks):
            raise ValueError('Invalid index')

        self._drinks.pop(index)

    def get_receipt(self):
        """Returns a dictionary containing the receipt for the order."""
        return {
            'drink_amount': self.get_num_items(),
            'subtotal': self.get_total(),
            'tax': round(self.get_total() * .0725, 2),
            'total': self.get_total() + round(self.get_total() * .0725, 2),
            'drinks': [
                {
                    'base': drink.get_base(),
                    'flavors': drink.get_flavors(),
                    'size': drink.get_size(),
                    'cost': drink.get_total()
                } for drink in self._drinks
            ],
        }
