import unittest
def Add(string_numbers, delimiter = None):
    result = 0
    if not isinstance(string_numbers,str): raise TypeError("Input must be string")
    if not delimiter: delimiter = ","
    for number in string_numbers.split(delimiter):
        if number != "" and "-" not in number:
            result += int(number)
    return result