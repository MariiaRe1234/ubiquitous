
DIGITS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def num_to_num(text):
    hours = 0
    minutes = 0
    seconds = 0
    parts = text.split(':')
    if len(parts) == 1:
        hours = parts[0]
    elif len(parts) == 2:
        hours, minutes = parts
    elif len(parts) == 3:
        hours, minutes, seconds = parts
    return [int(i) for i in (hours, minutes, seconds)]


def num_to_text(number):
    if number < 20:
        return DIGITS[number]
    remaining = number % 10
    integer = number // 10 * 10
    if remaining == 0:
        return DIGITS[integer]
    return f'{DIGITS[integer]}-{DIGITS[remaining]}'


def change_endings(number, unit):
    if number == 1:
        return unit
    if 2 <= number < 20:
        return f'{unit}s'
    if number % 10 == 1:
        return unit
    return f'{unit}s'


print(change_endings(30, 'car'))
