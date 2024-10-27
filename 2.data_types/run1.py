x = 10
y = '10'
z = 10.1
sum1 = x + x
sum2 = y + y
print(sum1, sum2)
print(type(x), type(y), type(z))


student_grades = [19.1, 8.8, 7.5]
mix_list = [9, 'hello', [1, 2, 4.33]]
print(mix_list*2)


smth = range(0,11)
print(type(smth))
list1 = list(range(0,11))
print(type(list1))
print(list1)



# dir(list)
# dir(__buitins__)
#dir(range)
#dir(int)
#dir(str)

#help(len)
#help(str.upper)

mysum = sum(student_grades)
mylen = len(student_grades)
mean = mysum/mylen
print(mean)

#########################################
#Dictionary
student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}
# type(student_grades)
# dir(dict)
# help(dict.values)
mysum = sum(student_grades.values())
mylen = len(student_grades)
mean = mysum/mylen
print(mean)

for key in student_grades.keys():
    print(key)


#########################################
#Typle
monday_temperatures = (1, 4, 5)
print(monday_temperatures)

#########################################



