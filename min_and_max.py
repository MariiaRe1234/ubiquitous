"""
numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
Convert the elements of the list to type int(). Find the minimum and maximum value.

Answer the question:
What type of errors can be expected when converting a value to int()?

"""
# ValueError by converting 'Dog' and TypeError by None

numbers = [1, 2, '0', '300', 'Dog', None, -2.5, True, 0o1256]


def min_max(list_):
    res = []
    for i in list_:
       try:
           res.append(int(i))
       except (ValueError, TypeError):
           pass
    return f"in this list {res} min and max Value are = {min(res)}, {max(res)}"
# a, b = myFunktion 
print(min_max(numbers))





