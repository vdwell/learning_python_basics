#########################################
#Dictionary
dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
            'Germany': (357114, 83783942)}
print('1.print dict')
print(dict)
print('#' * 20)


print('2.print particular item')
print(dict['Canada'])
print('#' * 20)



print('3.iterate through dict')
for key in dict:
    print(key)
print('#' * 20)


print('4.iterate through dict')
for key in dict:
    print(key, '->', dict[key])
print('#' * 20)


#Looping Over Dictionary Items: The .items() Method
print('5.iterate through dict')
for item in dict.items():
    print(item)
    print(type(item))
print('#' * 20)


#Looping Over Dictionary Items: The .items() Method
print('6.iterate through dict')
for key, value in dict.items():
    print(key, '->', value)
print('#' * 20)


#Iterating Through Dictionary Keys: The .keys() Method
print('7.iterate through dict')
for key in dict.keys():
    print(key)
print('#' * 20)


#Walking Through Dictionary Values: The .values() Method
print('8.iterate through dict')
for value in dict.values():
    print(value)
print('#' * 20)


# type(student_grades)
# dir(dict)
# help(dict.values)
# mysum = sum(student_grades.values())
# mylen = len(student_grades)
# mean = mysum/mylen
# print(mean)

# for key in student_grades.keys():
#     print(key)


#########################################