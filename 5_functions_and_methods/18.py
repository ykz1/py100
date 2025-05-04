def remainders_3(numbers):
    return [number % 3 for number in numbers]

def not_divisible_by_3(remainders):
    return [remainder != 0 for remainder in remainders]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(not_divisible_by_3(remainders_3(numbers_1))))
print(any(not_divisible_by_3(remainders_3(numbers_2))))
print(any(not_divisible_by_3(remainders_3(numbers_3))))
print(any(not_divisible_by_3(remainders_3(numbers_4))))

'''
I actually didn't need the second function not_divisible_by_3 because the output from remainders_3 would suffice for our purposes since divisble returns 0 which is falsy and not divisble returns 1 or 2 which are both truthy -- matches the output from our second function.

print(remainders_3(numbers_1))
print(remainders_3(numbers_2))
print(remainders_3(numbers_3))
print(remainders_3(numbers_4))

'''