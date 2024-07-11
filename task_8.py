


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


print(num_to_num('12:15'))
