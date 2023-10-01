dict = {'one': 1, 'two': 2, 'three': 33}
print("Original dictionary:", dict)

dict.update({'three': 3, 'four': 4})
print("update():", dict)

del dict['two']
print("del():", dict)

dict.clear()
print("clear():", dict)

dict = {'one': 1, 'two': 2, 'three': 3}
keys = dict.keys()
print("keys():", list(keys))

values = dict.values()
print("values():", list(values))

items = dict.items()
print("items():", list(items))