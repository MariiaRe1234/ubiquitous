import task_7


def test_greeting_c_style():
    result = task_7.greeting_c_style('James', 14)
    assert result == 'Hello, my name is James. I am 14 years old!'


def test_greeting_with_format():
    result = task_7.greeting_with_format('Anna', 31)
    assert result == 'Hello, my name is Anna. I am 31 years old!'


def test_false_greeting_with_format():
    result = task_7.greeting_with_format('31', 'Anna')
    assert result != 'Hello, my name is Anna. I am 31 years old!'


def test_greeting_fstring():
    result = task_7.greeting_fstring('Kolin', 20)
    assert result == "Hello, my name is Kolin. I am 20 years old! Today is monday"
