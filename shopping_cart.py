"""
Create a simple shopping cart system where users can add items, view their cart,
and remove items. The program should maintain a list of items in the cart and
allow users to interact with it through a menu.

Requirements:
The user should be able to add items to the shopping cart.
The user should be able to view all items in the shopping cart.
The user should be able to remove a specific item from the cart by name.
The user should be able to exit the program when done.
Instructions:
Display a menu with the fol  lowing options:

1: Add item
2: View cart
3: Remove item
0: Exit

Hints:
Use a list to store the items in the cart.
Use a while True to keep the program running until the user chooses to exit.
Use conditionals to handle menu selections and input validation for non-existent
   items or options.
"""


print(
    'Welcome to the Shopping Cart System!\n'
    '\n1: Add item'
    '\n2: View cart'
    '\n3: Remove item'
    '\n0: Exit\n')

cart_items = []

while True:
    n = input('Please choose an option: ')
    if n == '1':
        new_item = input("what is your item?")
        cart_items.extend(new_item.split(','))
    elif n == '2':
        print(cart_items)
    # elif n == '3:
    #
    elif n == '0':
        break
    else:
        print('Incorrect option')

# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# class Dog(Animal):
#     type = 'dog'



