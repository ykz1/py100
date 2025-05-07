numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

'''
This is an "off-by-one" error, caused by Python having an index starting at 0 instead of 1. When we generate 5 numbers with range(5), it starts with 0.

Fixed in above. Alternatively we stick to our original range(5) and append(i + 1)
'''