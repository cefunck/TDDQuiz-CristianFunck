def Add(string_numbers):
    result = 0
    try:
        for number in string_numbers.split(","):
            result += int(number)
    except TypeError:
        print("Input must be a string of numbers delimited by commas.")
    return result