# Example dict
a_dict = {
    'blue': 'color',
    'apple': 'fruit',
    'dog': 'pet',
}

# Popping an item
print(a_dict.popitem())

# Dictionary no longer has popped item
print(a_dict)

# Popping from empty dict
# Raises KeyError
empty_dict = {}
# empty_dict.popitem()

# In action
a_dict['a'] = 10

print("Popping from dictionary")
while True:
    try:
        item = a_dict.popitem()
        print(item)
        # Do cool stuff with item here
    except KeyError:
        print("The dictionary is empty")
        break



