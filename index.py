class Drink:
    valid_bases = ['water', 'sbrite', 'pokeacola',
                   'Mr. Salt', 'Hill Fog', 'Leaf Wine']
    valid_flavors = ['lemon', 'cherry',
                     'strawberry', 'mint', 'blueberry', 'lime']

    # Function to validate flavors and raise errors if needed
    def __validate_flavors(self, flavors):
        unique_flavors = []

        for flavor in flavors:
            if flavor not in self.valid_flavors:
                raise ValueError(f'Invalid flavor: {flavor}')
            if flavor in unique_flavors:
                raise ValueError(f'Duplicate flavor: {flavor}')

            unique_flavors.append(flavor)

    def __init__(self, base, flavors):
        # Check if base is a list and raise an error if it has more than one
        # string
        if isinstance(base, list) and len(base) > 1:
            raise ValueError('Only one base is allowed')

        # Check if the base is an invalid base and raise error if it is
        if base not in self.valid_bases:
            raise ValueError(f'Invalid base: {base}')

        self.__validate_flavors(flavors)

        self.__base = base
        self.__flavors = flavors
        self.__cost = 1

    def get_flavors(self):
        return self.__flavors

    def get_base(self):
        return self.__base

    def get_total(self):
        return self.__cost

    def get_num_flavors(self):
        return len(self.__flavors)

    def set_flavors(self, flavors):
        self.__validate_flavors(flavors)
        self.__flavors = flavors

    def add_flavor(self, flavor):
        self.__validate_flavors([flavor])
        self.__flavors.append(flavor)


drink = Drink('water', ['lemon', 'cherry'])

print(drink.get_flavors())
print(drink.get_base())
print(drink.get_total())


class Order:
    def __init__(self, drinks):
        self.__drinks = drinks

    def get_items(self):
        for drink in self.__drinks:
            print(f'{drink.get_base()} with {drink.get_flavors()}')

    def get_num_items(self):
        return len(self.__drinks)

    def get_total(self):
        total = 0
        for drink in self.__drinks:
            total += drink.get_total()

        return total

    def add_item(self, drink):
        # Make sure the argument is a drink class
        if not isinstance(drink, Drink):
            raise ValueError('Only drinks can be added to an order')

        self.__drinks.append(drink)

    def remove_item(self, index):
        if index < 0 or index >= len(self.__drinks):
            raise ValueError('Invalid index')

        self.__drinks.pop(index)


drink1 = Drink('water', ['lemon', 'cherry'])
drink2 = Drink('sbrite', ['lime'])

order = Order([drink1, drink2])

order.add_item(Drink('pokeacola', ['mint', 'blueberry']))
order.remove_item(1)
order.get_items()
