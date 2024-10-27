#positional args
def add(a, b, c):
    return a + b + c
result = add(b=2, c=3, a=1)
print(result)

#keywork & optional args
def add(a, b, c = 0):
    return a + b + c
print(add(1, 2))
print(add(1, 2, 3))

# * args & **kwargs to add any number of arguments to a function
def add(*args):
    result = 0
    for num in args:
        result += num
    return result
print(add(1,1,1,1,1,1,1))

def add(a, b=0, *args):
    result = a + b
    for num in args:
        result += num
    return result
print(add(10,20,30,40))


#keyword arbitrary arguments or **kwargs

def personal_info(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

personal_info("Sarah", surname="Conor", son="John")
personal_info("Natalie", cats="3", breed="Maine Coon")


def new_func(a, b=0, *args, **kwargs):
	print(f'a = {a}, b = {b}, args = {args}, kwargs = {kwargs}')

new_func(1, 2, 'Love', 'Hope', name='Anna', age=20)