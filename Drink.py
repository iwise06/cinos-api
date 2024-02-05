class Drink:
    valid_bases = ['water', 'sbrite', 'pokeacola',
                   'Mr. Salt', 'Hill Fog', 'Leaf Wine']
    valid_flavors = ['lemon', 'cherry',
                     'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self, base, flavors):
        # Check if base is a list and raise an error if it has more than one
        # string
        if isinstance(base, list) and len(base) > 1:
            raise ValueError('Only one base is allowed')

        # Check if the base is an invalid base and raise error if it is
        if base not in self.valid_bases:
            raise ValueError(f'Invalid base: {base}')

        self._validate_flavors(flavors)

        self._base = base
        self._flavors = flavors
        self._cost = 1

    # Function to validate flavors and raise errors if needed
    # Change this and use sets
    def _validate_flavors(self, flavors):
        unique_flavors = []

        for flavor in flavors:
            if flavor not in self.valid_flavors:
                raise ValueError(f'Invalid flavor: {flavor}')
            if flavor in unique_flavors:
                raise ValueError(f'Duplicate flavor: {flavor}')

            unique_flavors.append(flavor)

    def get_flavors(self):
        return self._flavors

    def get_base(self):
        return self._base

    def get_total(self):
        return self._cost

    def get_num_flavors(self):
        return len(self._flavors)

    def set_flavors(self, flavors):
        self._validate_flavors(flavors)
        self._flavors = flavors

    def add_flavor(self, flavor):
        self._validate_flavors([flavor])
        self._flavors.append(flavor)
