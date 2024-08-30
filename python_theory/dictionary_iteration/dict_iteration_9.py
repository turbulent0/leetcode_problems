# Example Dictionaries
fruits = {'apple': .4, 'orange': .35}
veggies = {'carrot': .2, 'onion': .55}

# Dictionary unpacking
print({**fruits, **veggies})

# Iteration
for key, value in {**fruits, **veggies}.items():
    print(key, '->', value)

# Compare the below to ChainMap!
a = {'a': 100}
a2 = {'a': 1}
print("A value:", {**a, **a2}['a'])


