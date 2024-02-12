"""Drink class that contains the base, flavors, size, and cost of a drink.

This class is used to represent a drink in a drink order. It contains the
base, flavors, size, and cost of the drink. It also contains methods to
manipulate the flavors and size of the drink.

Typical usage example:
    drink = Drink('water', ['lemon', 'cherry'], 'small')
"""


class Drink:
    """Class that contains the base, flavors, size, and cost of a drink.

    Attributes:
        base: A string representing the base of the drink.
        flavors: A list of strings representing the flavors of the drink.
        size: A string representing the size of the drink.
        cost: A float representing the cost of the drink.
    """
    valid_bases = ['water', 'sbrite', 'pokeacola',
                   'Mr. Salt', 'Hill Fog', 'Leaf Wine']
    valid_flavors = ['lemon', 'cherry',
                     'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self, base, flavors, size):
        """Initializes the drink with the base, flavors, and size.

        Args:
            base: A string representing the base of the drink.
            flavors: A list of strings representing the flavors of the drink.
            size: A string representing the size of the drink.
        """
        # Check if base is a list and raise an error if it has more than one
        # string
        if isinstance(base, list) and len(base) > 1:
            raise ValueError('Only one base is allowed')

        # Check if the base is an invalid base and raise error if it is
        if base not in self.valid_bases:
            raise ValueError(f'Invalid base: {base}')

        if size.lower() not in ['small', 'medium', 'large', 'mega']:
            raise ValueError(f'Invalid size: {size}')

        self._validate_flavors(flavors)

        self._base = base
        self._flavors = flavors
        self._size = size.lower()
        self._cost = self._calculate_cost()

    # Need to to implement __eq__ method to compare drinks since
    # the default __eq__ method compares the memory location of the objects
    def __eq__(self, other):
        if not isinstance(other, Drink):
            return False
        return self._base == other._base and self._flavors == other._flavors

    def _calculate_cost(self):
        """Calculates the cost of the drink based on the size and number of flavors."""
        size_costs = {'small': 1.5, 'medium': 1.75,
                      'large': 2.05, 'mega': 2.15}

        return round(size_costs[self._size] + 0.15 * len(self._flavors), 2)

    # Function to validate flavors and raise errors if needed
    # Change this and use sets

    def _validate_flavors(self, flavors):
        """Validates the flavors of the drink and raises errors if needed."""
        unique_flavors = []

        for flavor in flavors:
            if flavor not in self.valid_flavors:
                raise ValueError(f'Invalid flavor: {flavor}')
            if flavor in unique_flavors:
                raise ValueError(f'Duplicate flavor: {flavor}')

            unique_flavors.append(flavor)

    def get_flavors(self):
        """Returns the list of flavors of the drink."""
        return self._flavors

    def get_base(self):
        """Returns the base of the drink."""
        return self._base

    def get_total(self):
        """Returns the cost of the drink."""
        return self._cost

    def get_num_flavors(self):
        """Returns the number of flavors of the drink."""
        return len(self._flavors)

    def set_flavors(self, flavors):
        self._validate_flavors(flavors)
        self._flavors = flavors

    def add_flavor(self, flavor):
        """Adds a flavor to the drink.

        Args:
            flavor: A string representing the flavor to be added to the drink.
        """
        self._validate_flavors([flavor])
        self._flavors.append(flavor)

    def get_size(self):
        """Returns the size of the drink."""
        return self._size

    def set_size(self, size):
        """Sets the size of the drink.

        Args:
            size: A string representing the size of the drink.

        Raises:
            ValueError: If the size is invalid.    
        """
        if size not in ['small', 'medium', 'large', 'mega']:
            raise ValueError(f'Invalid size: {size}')
        self._size = size
        self._cost = self._calculate_cost()

    def to_dict(self):
        """Returns a dictionary representation of the drink."""
        return {
            'base': self._base,
            'flavors': self._flavors,
            'size': self._size,
            'cost': self._cost
        }
