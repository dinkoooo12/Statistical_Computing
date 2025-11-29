# we can do update,delete ,add, extend,append, replace and pop
lst = [1, 2, 3, 4, 5]
lst[0] = 10  # update
del lst[1]   # delete
lst.append(6)  # add
lst.extend([7, 8, 9])  # extend
print(lst)  # Output: [10, 3, 4, 5, 6, 7, 8, 9]