#remove duplicate add convert to set which like dict does not allow duplicate keys
# Compare this snippet from dict.py:
# #we can do add, delete, update, pop, clear, and modify,case
# set does not have indexing so no update by index
s = {1, 2, 3, 4, 5}
s.add(6)  # add
s.remove(2)  # delete
s.discard(10)  # delete without error if not found
s.update({7, 8, 9})  # extend
print(s)  # Output: {1, 3, 4, 5, 6, 7, 8, 9}