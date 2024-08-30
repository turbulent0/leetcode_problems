# Example dictionary
prices = {
    'apple': .25,
    'orange': .50,
    'kiwi': .75,
}

# Cycling
from itertools import cycle
num_items = 10
for item in cycle(prices.items()):
    if num_items == 0:
        break
    num_items -= 1
    print(item)

# Chains
from itertools import chain
fruits = {'apple': 10, 'banana': 20}
veggies = {'carrot': 5, 'potato': 45}
for item in chain(fruits.items(), veggies.items()):
    print(item)

