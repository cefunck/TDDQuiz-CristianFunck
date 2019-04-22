def Add(string_numbers, delimiter = None):
    result = 0
    if not delimiter: delimiter = ","
    try:
        for number in string_numbers.split(delimiter):
            if number != "" and "-" not in number:
                result += int(number)
    except TypeError:
        print("Input must be a string of numbers delimited by commas.")
    return result