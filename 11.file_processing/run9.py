"""

myfile = open('fruits.txt')
print(type(myfile))
print(myfile.read())
print(myfile.read()) # second read does not have effect because of !!! CURSOR CONCEPT !!!

print('#' * 20)
#########################

myfile = open('fruits.txt')
content = myfile.read()
print(type(content))
print(content)
print(content)

print('#' * 20)
#########################

myfile = open('fruits.txt')
content = myfile.read()
print(type(content))
print(content)
print(content)
myfile.close() # <<< close file to release memory
# print(myfile.read()) # error: 'I/O operation on closed file'


print('#' * 20)

"""
#########################  <<<<<<<<<<<< beter way to open file
 # 'with' context manager

with open('fruits.txt') as myfile:
    content = myfile.read()
    #closing file is not needed here! it will be done explicityly
print(content)


print('#' * 20)
#########################
with open('files/fruits2.txt') as myfile: # = with open('files/fruits2.txt', 'r') as myfile:
    content = myfile.read()
print(content)    


print('#' * 20)
#########################

#########################
with open('files/vegetables.txt', 'w') as myfile: #any existing info in the file will be rewrited (overwrited)
    myfile.write('Tomato\nCucumber\nOnion')
    myfile.write('Garlic\n')


print('#' * 20)
#########################


#########################
with open('files/vegetables.txt', 'a') as myfile: #we want to ADD lines to the txt file
    myfile.write('Okra\n')
    # content = myfile.read()  #<< will no work, 'a' is only for writing
# print(content)    


print('#' * 20)
#########################
with open('files/vegetables.txt', 'a+') as myfile: #we want to ADD lines to the txt file
    myfile.write('Carbidge\n')
    content = myfile.read()  #<<<<<<<< empty content because of the !cursor!
print(content)    


print('#' * 20)
#########################
with open('files/vegetables.txt', 'a+') as myfile: #we want to ADD lines to the txt file
    myfile.write('Carbidge\n')
    myfile.seek(0) #<<<<<<<<<< seek() method to move cursor at the beginning
    content = myfile.read()  #<<<<<<<< empty content because of the !cursor!
print(content)    


print('#' * 20)
#########################
