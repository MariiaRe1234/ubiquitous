
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

def take_time_give_text(time):
    hours, minutes, secounds = num_to_num(time)
    res = list()
    if hours == 0 and minutes == 0 and secounds == 0:
        return 'midnight'
    if hours > 0:
        dd = num_to_text(hours)
        uu = change_endings(hours, 'hour')
        res.append(f'{dd} {uu}')
    if minutes > 0:
        dd = num_to_text(minutes)
        uu = change_endings(minutes, 'minute')
        res.append(f'{dd} {uu}')
    if secounds > 0:
        dd = num_to_text(secounds)
        uu = change_endings(secounds, 'second')
        res.append(f'{dd} {uu}')
    return ", ".join(res)



print(take_time_give_text("00:00:01"))
