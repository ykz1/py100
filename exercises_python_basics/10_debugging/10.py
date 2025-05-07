def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0``


'''
The issue is that we initialize product with value 0 in line 3. When we multiple additional numbers to product subsequently, the result will always be 0.

To fix this, set product's starting value as 1—done above in line 3.
'''