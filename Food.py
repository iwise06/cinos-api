class Food:
    valid_base = ['hotdog', 'corndog', 'ice cream',
                  'onion rings', 'french fries', 'tater tots', 'nacho chips']
    valid_toppings = ['cherry', 'whipped cream', 'caramel sauce', 'chocolate sauce',
                      'nacho cheese', 'chili', 'bacon bits', 'ketchup', 'mustard']

    def __init__(self, base, toppings):
        if isinstance(base, list) and len(base) > 1:
            raise ValueError('Only one base is allowed')

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
        unique_toppings = []

        for flavor in toppings:
            if flavor not in self.valid_toppings:
                raise ValueError(f'Invalid flavor: {flavor}')
            if flavor in unique_toppings:
                raise ValueError(f'Duplicate flavor: {flavor}')

            unique_toppings.append(flavor)

    def _calculate_cost(self):
        topping_costs = {'cherry': 0.0, 'whipped cream': 0.0,
                         'caramel sauce': 0.5, 'chocolate sauce': 0.5,
                         'nacho cheese': 0.3, 'chili': 0.6, 'bacon bits': 0.3,
                         'ketchup': 0.0, 'mustard': 0.0}

        base_costs = {'hotdog': 2.30, 'corndog': 2.00, 'ice cream': 3.00,
                      'onion rings': 1.75, 'french fries': 1.50,
                      'tater tots': 1.70, 'nacho chips': 1.90}

        return round(base_costs[self._base] + sum([topping_costs[topping] for topping in self._toppings]), 2)

    def get_base(self):
        return self._base

    def get_total(self):
        return self._cost

    def get_num_toppings(self):
        return len(self._toppings)

    def get_toppings(self):
        return self._toppings

    def set_toppings(self, toppings):
        self._validate_toppings(toppings)
        self._toppings = toppings

        self._calculate_cost()

    def add_topping(self, topping):
        self._validate_toppings([topping])
        self._toppings.append(topping)

        self._calculate_cost()
