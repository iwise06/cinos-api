from Drink import Drink

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
