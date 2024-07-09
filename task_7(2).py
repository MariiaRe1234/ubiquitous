"""Home task 2:

List filtering
Given an object of type list():

l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
Implement a function that filters only integer (int) values from this list.
Write several solutions:

using a for loop
using list comprehensions
using filter() + lambda

Example:

def filter_list(l):
    return  # [1, 2, 4, 10, 33]


Check yourself:

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""


l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
res = list()
"""
for i in l:
    if isinstance(i, int):
        res.append(i)
    print(res)


print([i for i in l if isinstance(i, int)])
"""


print(list(filter(lambda i: isinstance(i, int), l)))


