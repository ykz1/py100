numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = [int(number / 2) for number in numbers.values()]

print(half_numbers)