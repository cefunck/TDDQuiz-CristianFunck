def Add(string_numbers):
    result = 0
    try:
        string_numbers.split(",")
    except TypeError:
        print("Input must be a string of numbers delimited by commas.")
    return result