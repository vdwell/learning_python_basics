a, b = 2, 3
a, b = b, a

print(a,b)


my_list = ['Monica', 25, 'Doctor', 'Brazil']
name, age, *_ = my_list
print(name, age)


person_info = {'name': 'John', 'age': 35, 'city': 'New York'}
name, age, city = person_info.values()
print(name, age, city)