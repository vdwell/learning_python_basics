"""
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
        print(type(value))
        return the_mean
    else:
        the_mean = sum(value) / len(value)
        print(type(value))
        return the_mean

student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}
monday_temperatures = [9.1, 8.8, 7.5]
print(mean(student_grades))
print(mean(monday_temperatures))

#####################


def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
        print(type(value))
        return the_mean
    else:
        the_mean = sum(value) / len(value)
        print(type(value))
        return the_mean

student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}
monday_temperatures = [9.1, 8.8, 7.5]
print(mean(student_grades))
print(mean(monday_temperatures))

##############
print(isinstance(3, int))
##############

"""
x = 3

y = 3
if x > y:
    print('x is greater than y')
elif x == y:
    print('x is equal to y')
else:
    print('x is less than y')
# breakpoint()
x = 5
y = 5

if x > y:
    print('x is greater than y')
elif x == y:
    print('x is equal to y')
else:
    print('x is less than y')