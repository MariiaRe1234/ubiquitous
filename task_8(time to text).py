"""
Convert time into words
====

Given a time in the format of hh:mm:ss (24-hour format), the task is to convert it into words.

Requirements:
  1. Input: A string representing time in the format hh:mm:ss.
  2. Output: A string that converts the time into words.

Examples:
  - 12:00 -> twelve hours
  - 12:13:59 -> twelve hours, thirteen minutes, fifty-nine seconds

Notes:
  - If the given time is `00:00`, the function should return `'midnight'`.
  - If hours, minutes, or seconds are `0`, do not include them in the response.
  - Use singular or plural appropriately:
    - 1 hour, but 5 hours
    - 22 minutes, but 1 minute

Additional notes:
  - use '12:22:33'.split(':') ==> ['12', '22', '33']
  - use ', '.join(['apple', 'orange', 'green']) ==> 'apple, orange, green'

Examples
====
print(convert_time_to_words("12:00:00"))  # Output: "twelve hours"
print(convert_time_to_words("12:13:59"))  # Output: "twelve hours, thirteen minutes, fifty-nine seconds"
print(convert_time_to_words("00:00:00"))  # Output: "midnight"
print(convert_time_to_words("01:00:00"))  # Output: "one hour"
print(convert_time_to_words("00:01:00"))  # Output: "one minute"
print(convert_time_to_words("00:00:01"))  # Output: "one second"
print(convert_time_to_words("01:01:01"))  # Output: "one hour, one minute, one second"

"""


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


# 1. Get values for hours, minutes, seconds
# 2. Convert integer into text. Example int(12) --> twelve
# 3. Use singular or plural

def number_to_text():
    pass

def time_to_str():
    pass

def get_tome_as_numbers():
    pass


def digital_time_to_text(time_str: str) -> str:
    raise ValueError(time_str)


if __name__ == '__main__':
    assert digital_time_to_text('12:00') == 'twelve hours'
    assert digital_time_to_text('01:25:30') == 'one hour, twenty-five minutes, thirty seconds'
    assert digital_time_to_text('12:13:59') == 'twelve hours, thirteen minutes, fifty-nine seconds'
    assert digital_time_to_text('00:00') == 'midnight'
    assert digital_time_to_text('11') == 'eleven hours'