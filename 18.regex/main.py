import re

'''
re.search method
search for the 1st occurence
returns match object
match.group(1) returns the mtach

re.split method
does splite based on regex pattern
return list


re.findall method
ind all occurrences of a pattern in a string and returns them as a list


re.finditer method
The finditer() function in Python's re module is a powerful tool for finding all non-overlapping occurrences of a specified pattern in a string. 
Unlike findall(), which returns a list of matches, finditer() returns an iterator that yields match objects for each occurrence. 
This allows you to access additional details about each match, such as its position in the string.


'''


with open ('config.txt', 'r') as file:
    content = file.read()
print(type(content))


print('-' * 40)
pattern = r'interfaces ge'
pattern = r'user'
match = re.search(pattern, content)
print(match)
print('-' * 40)

print('-' * 40)
pattern = r'interfaces ge'
matches = re.findall(pattern, content)  
print(matches)
print('-' * 40)



print('-' * 40)
print('-' * 40)
print('-' * 40)




with open ('config.txt', 'r') as file:
    content = file.read().split('\n')
print(type(content))
print(len(content))

#re.search and match.group()
pattern = r'interfaces (ge\S+) '
for i in range(len(content)):
    match = re.search(pattern, content[i])
    print(f'result for line index {i}: {match}')
    if match:
        print(f'result for line index {i}: {match.group(1)}')

print('-' * 40)
print('-' * 40)

#re.split
pattern = r'\s+'
for i in range(len(content)):
    resplitlist = re.split(pattern, content[i])
    print(f'result for line index {i}: {resplitlist}')


print('-' * 40)
print('-' * 40)

#re.findall
#returns a list of all occurrences of "cute" found in the text
pattern = r'0'
for i in range(len(content)):
    match = re.findall(pattern, content[i])
    print(f'result for line index {i}: {len(match)}: {match}')


print('-' * 40)
print('-' * 40)

#re.finditer
#returns a list of all occurrences of "cute" found in the text
pattern = r'et'
for i in range(len(content)):
    re_finditer_iterator = re.finditer(pattern, content[i])
    print(f'result for line index {i}:')
    for item in re_finditer_iterator:
        print (item)
        print (item.group())
      