"""
Problem Statement:
Write a Python function that takes a predefined string and counts the number of
vowels and consonants in the string. It should ignore spaces, punctuation,
and numbers.

Requirements:
Ignore spaces, punctuation, and numbers when counting.
Treat both uppercase and lowercase letters equally (i.e., "A" and "a"
are both vowels).

Hints:
Define a set of vowels and consonants.
Example: vowels = {'a', 'e', 'i', 'o', 'u'}.
Use string methods like .lower() and .isalpha()
"""
import string

text_example = """Write a Python function that takes a predefined string and counts the number of
vowels and consonants in the string. It should ignore spaces, punctuation,
and numbers."""

VOWELS = 'aeoui'
PUNKTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
def vowels(text):
    v = []
    c = []
    for i in text.lower():
        if i in PUNKTUATION or i in string.digits:
            continue
        if i in VOWELS:
            v.append(i)
        else:
            c.append(i)
    return len(v), len(c)

print(vowels("Python! is awesome!"))