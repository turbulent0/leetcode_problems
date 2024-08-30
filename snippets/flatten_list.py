# when to use generator
from itertools import chain

list_of_lists = [[1, 2], [2, 3]]
flat_list = [*chain(*list_of_lists)]
flat_list
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# when to use all list
flat_list = [element for sublist in list_of_lists for element in sublist]
flat_list
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# sum if alwals better then reduce + add


# nested lists
def flatten(obj):
    if isinstance(obj, list):
        for item in obj:
            yield from flatten(item)
    else:
        yield obj
