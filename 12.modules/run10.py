import sys
print(sys.builtin_module_names) #<< list of python built-in modules
print(sys.prefix) # path

import time
print(dir(time))

import os
print(dir(os))

import pandas

"""
while True:
    if os.path.exists('files/vegetables.txt'):
        with open('files/vegetables.txt') as file:
            print(file.read())
            print('#' * 20)
    else:
            print("File does not exist")        
    time.sleep(5)
"""

while True:
    if os.path.exists('files/temps_today.csv'):
        data = pandas.read_csv('files/temps_today.csv')
        print(data.mean())
        print('#' * 20)
    else:
            print("File does not exist")        
    time.sleep(5)

