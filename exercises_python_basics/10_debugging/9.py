def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

'''
The error occurs when we have a list of numbers all less than 0. Our starting value for max_number is 0 and so our function will always return 0 erroneously for such lists.

To fix, we can simply set max_number's starting value to the first element (or any element) of the numbers list—this is done in line 4.

Alternatively we can set max_number's starting value to the smallest number that Python knows, but that feels like a weird approach.
'''