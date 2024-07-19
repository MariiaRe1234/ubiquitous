"""
Letters Count
====

Имеется следующий текст:

Python is an interpreted high-level programming language for general-purpose programming.
Created by Guido van Rossum and first released in 1991, Python has a design philosophy
that emphasizes code readability, notably using significant whitespace.
It provides constructs that enable clear programming on both small and large scales.
In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management.
It supports multiple programming paradigms, including object-oriented,
imperative, functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython,
the reference implementation of Python, is open source software and has
a community-based development model, as do nearly all of Python's other implementations.
Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!

Определите какая буква наиболее часто встречается в этом тексте?

Примечания:
 - не учитывайте регистр букв, т.е. 'A' = 'a'
 - не учитывайте знаки препинания и спецсимволы (кавычки, тире)
 - не учитывайте пробелы и переводы строк

Ответьте на следующие вопросы:
 - Сколько раз в этом тексте встречается слово 'Python'?
 - Сколько раз ваша программа перечитывает текст от начала до конца?
 - Будет ли ваше решение работать корректно если в тексте появятся буквы русского алфавита?

Hints:
 - use .lower()
 - use .count()
"""

import string

text_from_wiki = """
Python is an interpreted high-level programming language for general-purpose programming. 
Created by Guido van Rossum and first released in 1991, Python has a design philosophy 
that emphasizes code readability, notably using significant whitespace. 
It provides constructs that enable clear programming on both small and large scales. 
In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management. 
It supports multiple programming paradigms, including object-oriented, imperative, 
functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython, the reference 
implementation of Python, is open source software and has a community-based development model, 
as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation.
Привет из Харькова!
"""

escape_list = string.whitespace + string.punctuation

def count_letters(text):
    text = text.lower()
    res = {}
    for i in text:
        if i in escape_list:
            continue
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return sorted(res.items(), key=lambda pair: pair[1])[-1]


def sssss(text):
    text = text.lower()
    unique_text = set(i for i in text if i not in escape_list)
    l = None
    c = 0
    for i in unique_text:
        value = text.count(i)
        if value >= c:
            l = i
            c = value
    return l, c




print(sssss(text_from_wiki))
