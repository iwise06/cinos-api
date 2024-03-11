"""icestorm class that contains the base, toppings, and cost of an icestorm.

This class is used to represent an icestorm in an order. It contains the
base, toppings, and cost of the icestorm. It also contains methods to
manipulate the toppings of the icestorm.

Typical usage example:
    icestorm = IceStorm('chocolate', ['storios', 'pecans'])
"""


class IceStorm:
    """Class that contains the base, toppings, and cost of an icestorm.

    Attributes:
        base: A string representing the icecream flavor of the icestorm.
        toppings: A list of strings representing the toppings of the icestorm.
        cost: A float representing the cost of the icestorm.
    """

    valid_base = ['mint chocolate chip', 'chocolate',
                  'vanilla bean', 'banana', 'butter pecan', 's\' more']
    valid_toppings = ['cherry', 'whipped cream', 'caramel sauce',
                      'chocolate sauce', 'storios', 'dig dogs', 't&t\'s', 'cookie dough', 'pecans']

    def __init__(self, base, toppings):
        """Initializes the icestorm with the base and toppings.

        Args:
            base: A string representing the icecream flavor of the icestorm.
            toppings: A list of strings representing the toppings of the icestorm.
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

    # Need to to implement __eq__ method to compare icestorm since
    # the default __eq__ method compares the memory location of the objects

    def __eq__(self, other):
        if not isinstance(other, IceStorm):
            return False
        return self._base == other._base and self._toppings == other._toppings

    def _validate_toppings(self, toppings):
        """Validates the toppings of the icestorm and raises errors if needed."""
        unique_toppings = []

        for topping in toppings:
            if topping not in self.valid_toppings:
                raise ValueError(f'Invalid topping: {topping}')
            if topping in unique_toppings:
                raise ValueError(f'Duplicate topping: {topping}')

            unique_toppings.append(topping)

    def _calculate_cost(self):
        """Calculates the cost of the icestorm based on the base and the toppings."""
        topping_costs = {'cherry': 0.0, 'whipped cream': 0.0, 'caramel sauce': 0.50, 'chocolate sauce': 0.50,
                         'storios': 1.00, 'dig dogs': 1.00, 't&t\'s': 1.00, 'cookie dough': 1.00, 'pecans': 0.50}

        base_costs = {'mint chocolate chip': 4.00, 'chocolate': 3.00,
                      'vanilla bean': 3.00, 'banana': 3.50, 'butter pecan': 3.50, 's\'more': 4.00}

        return round(base_costs[self._base] + sum([topping_costs[topping] for topping in self._toppings]), 2)

    def get_base(self):
        """Returns the base of the icestorm."""
        return self._base

    def get_total(self):
        """Returns the cost of the icestorm."""
        return self._cost

    def get_num_toppings(self):
        """Returns the number of toppings on the icestorm."""
        return len(self._toppings)

    def get_toppings(self):
        """Returns the list of toppings on the icestorm."""
        return self._toppings

    def set_toppings(self, toppings):
        """Sets the toppings of the icestorm."""
        self._validate_toppings(toppings)
        self._toppings = toppings

        self._calculate_cost()

    def add_topping(self, topping):
        """Adds a topping to the icestorm.

        Args:
            topping: A string representing the topping to be added to the icestorm.
        """
        self._validate_toppings([topping])
        self._toppings.append(topping)

        self._calculate_cost()
