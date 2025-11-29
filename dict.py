#we can do add, delete, update, pop, clear, and modify,case sensitive keys
dct = {'a': 1, 'b': 2, 'c': 3}
dct['a'] = 10  # update
del dct['b']   # delete
dct['d'] = 4   # add
dct.pop('c')   # pop
dct.clear()    # clear
print(dct)  # Output: {}
#we use append to add items to a list but in dict we use assignment
#we can append dict family to others
