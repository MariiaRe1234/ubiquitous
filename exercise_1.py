"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that
are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.

Write this in one line of Python.

Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.
"""


a = [1, 0,1, '2', -3, 4.3, 5, 'apple', 21, 34, 'bowl', 89, 49, 63, 37.9, 89.8888, -26]


# def sorting_the_list(x):
#     llist = []
#     for i in x:
#         if isinstance(i, (int, float)) and i <= 5:
#             llist.append(i)
#     return llist
#
# print(sort_the_list(a))

n = int(input("Enter a number: "))
print(list(filter(lambda i: isinstance(i, (int, float)) and i <= n, a)))