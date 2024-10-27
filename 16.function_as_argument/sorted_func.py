#The sorted() function returns a new sorted list from the elements of any iterable.
#sorted(iterable, key=key, reverse=reverse)
#iterable is the sequence to sort (list, dict, tuple, etc);
#key is a function to execute to decide the order;
#reverse is a boolean. False is an ascending order, and True is descending. The default is False.


tuples = [(1, 'banana'), (2, 'apple'), (3, 'orange')]

# Using a lambda function to sort by the second element of each tuple
sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)

print(sorted_tuples)