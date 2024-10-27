# Define a function that takes a function and a value as arguments
def apply_function(func, value):
    return func(value)

# Call the function with a lambda function as the first argument
result = apply_function(lambda x: x * x, 5)

print(result)