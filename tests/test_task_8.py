import task_8


# def num_to_num(text):
#     hours = 0
#     minutes = 0
#     seconds = 0
#     parts = text.split(':')
#     if len(parts) == 1:
#         hours = parts[0]
#     elif len(parts) == 2:
#         hours, minutes = parts
#     elif len(parts) == 3:
#         hours, minutes, seconds = parts
#     return [int(i) for i in (hours, minutes, seconds)]

def test_num_to_num():
    result = task_8.num_to_num('2:15:00')
    assert result == '2, 15, 0'

# def num_to_text(number):
#     if number < 20:
#         return DIGITS[number]
#     remaining = number % 10
#     integer = number // 10 * 10
#     if remaining == 0:
#         return DIGITS[integer]
#     return f'{DIGITS[integer]}-{DIGITS[remaining]}'

def test_num_to_text():
    result = task_8.num_to_text('2:15:00')
    assert result == '2, 15, 0'