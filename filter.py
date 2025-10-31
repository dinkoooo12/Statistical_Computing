nums = [10, 15, 20, 25, 30]
filtered_nums = filter(lambda x: x % 20 == 0, nums)  # filter applies the function to each item in the iterable and returns only those items for which the function returns True
print(list(filtered_nums))  # prints [20]