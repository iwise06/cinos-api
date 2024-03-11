"""Food class that contains the base, toppings, and cost of a food item.

This class is used to represent a food item in an order. It contains the
base, toppings, and cost of the food. It also contains methods to
manipulate the toppings of the food.

Typical usage example:
    food = Food('hotdog', ['chili', 'nacho cheese'])
"""


class Food:
    """Class that contains the base, toppings, and cost of a food item.

    Attributes:
        base: A string representing the base of the food item.
        toppings: A list of strings representing the toppings of the food.
        cost: A float representing the cost of the food.
    """

    valid_base = ['hotdog', 'corndog', 'ice cream',
                  'onion rings', 'french fries', 'tater tots', 'nacho chips']
    valid_toppings = ['cherry', 'whipped cream', 'caramel sauce', 'chocolate sauce',
                      'nacho cheese', 'chili', 'bacon bits', 'ketchup', 'mustard']

    def __init__(self, base, toppings):
        """Initializes the food with the base and toppings.

        Args:
            base: A string representing the base of the food.
            toppings: A list of strings representing the toppings of the food.
        """
        if isinstance(base, list) and len(base) > 1:
            raise ValueError('Only one base is allowed')

        # Check if the base is an invalid base and raise error if it is

        if base not in self.valid_base:
            raise ValueError(f'Invalid base: {base}')

        self._validate_toppings(toppings)

        self._base = base
        self._toppings = toppings
        self._cost = self._calculate_cost()

    # Need to to implement __eq__ method to compare food since
    # the default __eq__ method compares the memory location of the objects

    def __eq__(self, other):
        if not isinstance(other, Food):
            return False
        return self._base == other._base and self._toppings == other._toppings

    def _validate_toppings(self, toppings):
        """Validates the toppings of the food and raises errors if needed."""
        unique_toppings = []

        for topping in toppings:
            if topping not in self.valid_toppings:
                raise ValueError(f'Invalid topping: {topping}')
            if topping in unique_toppings:
                raise ValueError(f'Duplicate topping: {topping}')

            unique_toppings.append(topping)

    def _calculate_cost(self):
        """Calculates the cost of the food based on the base and the toppings."""
        topping_costs = {'cherry': 0.0, 'whipped cream': 0.0,
                         'caramel sauce': 0.5, 'chocolate sauce': 0.5,
                         'nacho cheese': 0.3, 'chili': 0.6, 'bacon bits': 0.3,
                         'ketchup': 0.0, 'mustard': 0.0}

        base_costs = {'hotdog': 2.30, 'corndog': 2.00, 'ice cream': 3.00,
                      'onion rings': 1.75, 'french fries': 1.50,
                      'tater tots': 1.70, 'nacho chips': 1.90}

        return round(base_costs[self._base] + sum([topping_costs[topping] for topping in self._toppings]), 2)

    def get_base(self):
        """Returns the base of the food."""
        return self._base

    def get_total(self):
        """Returns the cost of the food."""
        return self._cost

    def get_num_toppings(self):
        """Returns the number of toppings on the food."""
        return len(self._toppings)

    def get_toppings(self):
        """Returns the list of toppings on the food."""
        return self._toppings

    def set_toppings(self, toppings):
        """Sets the toppings of the food."""
        self._validate_toppings(toppings)
        self._toppings = toppings

        self._calculate_cost()

    def add_topping(self, topping):
        """Adds a topping to the food.

        Args:
            topping: A string representing the topping to be added to the food.
        """
        self._validate_toppings([topping])
        self._toppings.append(topping)

        self._calculate_cost()
