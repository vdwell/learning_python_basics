def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(type(squared_numbers))
# Convert the map object to a list
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)
