"""
Password validation.

Implement function for validating user password. Password *must* match following criteria:
 - should be string
 - length between 8,20
 - must contain at least one capital letter
 - must contain at least one number
 - must contain at least one punctuation symbol
 - whitespace characters are not allowed

Function should return boolean value

Use string.ascii_uppercase
Use string.digits
Use string.punctuation

"""

import string


def validate_password(text):
    """
    :param text: User password
    :type text: str
    :rtype: bool
    """

    if not isinstance(text, str):
        return False
    if len(text) < 8 or len(text) > 20:
        return False
    if not any(i.isupper() for i in text):
        return False
    return True


if __name__ == '__main__':
    print(validate_password('abchldkfkdfF3'))  # not string
