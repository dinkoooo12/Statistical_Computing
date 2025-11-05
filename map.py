nums = [1,2,3,4,5]
# map applies the function to each item in the iterable, here iterable is nums
squared = map(lambda x: x**2, nums)  
print(list(squared))  # prints [1, 4, 9, 16, 25]

