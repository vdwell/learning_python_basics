def area(a, b):
    return a * b

print(area(3, 5)) # non keyword arguments

print(area(b=3, a=9)) # keyword arguments = positional args

#####################

def area(a, b=6):  # b is default parameter with value = 6
    return a * b
print(area(5))
print(area(a=5))
print(area(a=4, b=3))
print(area(6, 8))

"""
def area(a=7, b):  # <<<<<<<< not allowed!!! DEFAULT PARAMETER CANNOT BE BEFORE NON-DEFAULT (parameter without a default follows parameter with a default)
    return a * b
print(area(5))
print(area(a=5))
print(area(a=4, b=3))
print(area(6, 8))
"""

#####################
def mean(*args):
    print(type(args))  #### args is a tuple
    return args


print(mean(1, 3, 'a', 4)) # returns tuple


def mean(*args):
    return sum(args) / len(args)
print(mean(1, 3, 4)) # returns tuple

# print(mean(1, 3, 4, x=9)) # no keyword arg is allowed for this function. 'unexpected keyword argument' error

print('#' * 20)
#####################

def new_mean(**kwargs):  #kwargs means keyword args. only keyword (or named) arguments are allowed
    print(type(kwargs)) 
    return kwargs

# print(new_mean(1, 2, 3)) ## error 'takes 0 positional arguments but 3 were given

print(new_mean(a=1, b=2, c=3))

#####################