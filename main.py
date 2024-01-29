from Drink import Drink
from Order import Order

# Examples for Drink class
drink = Drink('water', ['lemon', 'cherry'])

print(drink.get_flavors())
print(drink.get_base())
print(drink.get_total())

# Examples for Order class
drink1 = Drink('water', ['lemon', 'cherry'])
drink2 = Drink('sbrite', ['lime'])

order = Order([drink1, drink2])

order.add_item(Drink('pokeacola', ['mint', 'blueberry']))
order.remove_item(1)
order.get_items()
