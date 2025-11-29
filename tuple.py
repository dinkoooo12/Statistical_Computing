# not support add,delete and update
tpl = (1, 2, 3, 4, 5)
2*tpl # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5) replicate rather than modify
 #we can convert to list to modify
lst = list(tpl)
