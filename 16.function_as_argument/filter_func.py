#The filter() function is used to create an iterator from elements of an iterable for which a function returns true.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a lambda function to filter out odd numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object to a list
even_numbers_list = list(even_numbers)
print(even_numbers_list)