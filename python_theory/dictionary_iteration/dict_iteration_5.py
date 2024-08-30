objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']

# "Zipping" values into dictionaries
a_dict = {key: value for key, value in zip(objects, categories)}
print(a_dict)

# Better way of converting keys to values and v.v.
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict)

# Number dictionary
num_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
}

# Filtering a dictionary more readably
filtered_nums = {key: value for key, value in num_dict.items() if value > 2}
print(filtered_nums)

# Incomes dict
incomes = {
    'jeff': 12000,
    'annie': 23000,
    'glen': 50000,
}

# Summing values more readably
print(sum([value for value in incomes.values()]))

# Summing values even more readably
print(sum(incomes.values()))

# Summing values with generators for really large data
# Notice the parentheses instead of brackets
sum((value for value in incomes.values()))

# Sorting by keys
sorted_incomes = {k: incomes[k] for k in sorted(incomes)}
print(sorted_incomes)

# Not the same as sorted(incomes)
print(sorted(incomes))

# Sorting by value
def by_value(item):
    return item[1] # The second item of a tuple

sorted_byv = {}
for k, v in sorted(incomes.items(), key=by_value):
    sorted_byv[k] = v
print(sorted_byv)
