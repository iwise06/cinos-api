from Drink import Drink


class Order:
    def __init__(self, drinks: list[Drink]):
        self._drinks = drinks

    def get_items(self):
        return self._drinks

    def get_num_items(self):
        return len(self._drinks)

    def get_total(self):
        total = 0
        for drink in self._drinks:
            total += drink.get_total()

        return total

    def add_item(self, drink):
        # Make sure the argument is a drink class
        if not isinstance(drink, Drink):
            raise ValueError('Only drinks can be added to an order')

        self._drinks.append(drink)

    def remove_item(self, index):
        if index < 0 or index >= len(self._drinks):
            raise ValueError('Invalid index')

        self._drinks.pop(index)

    def get_receipt(self):
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
