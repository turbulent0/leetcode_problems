# Example dictionaries
fruits = {'orange': 10, 'apple': 20}
veggies = {'carrot': 5, 'potato': 45}

# ChainMap usage
from collections import ChainMap
chained_map = ChainMap(fruits, veggies)

# Iteration
for key in chained_map:
    print(key, chained_map[key])

# More iteration
for key, value in chained_map.items():
    print(key, "->", value)

# Example about ordering of shared keys
a = {'a': 100}
a2 = {'a', 1}
a_chain = ChainMap(a, a2)
print(a_chain)
print("A value:", a_chain['a'])

