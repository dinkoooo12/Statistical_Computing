nums = [1,2,3,4,5]
squared = map(lambda x: x**2, nums)  # map applies the function to each item in the iterable, here iterable is nums
print(list(squared))  # prints [1, 4, 9, 16, 25]

#lambda function is an anonymous function defined using the lambda keyword. Equal to def number_square(x): return x**2