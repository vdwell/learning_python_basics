temps = [221, 234, 340, 230]

result = []
for item in temps:
    new_item = item/10
    result.append(new_item)
print(result)    


new_temps = [temp/10 for temp in temps] # list comprehension
print(new_temps)

######################################################
print('#' * 30)
######################################################


temps = [221, 234, 340, -9999, 230] # We want to ignore -9999 value during further calculations
new_temps = [temp/10 for temp in temps if temp != -9999] # list comprehenstion with if condition
print(new_temps)

######################################################
print('#' * 30)
######################################################

temps = [221, 234, 340, -9999, 230] # We want to ignore -9999 value during further calculations
new_temps = [temp/10 if temp != -9999 else 0 for temp in temps ] # list comprehenstion with if-else condition
#give me temp/10 only if temp is different than -9999
print(new_temps)
