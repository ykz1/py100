def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)

print(
    '''
    function name = multiply_numbers
    function arguments = 2, 3, 4
    function definition = starts in line 1
    function body = lines 2 and 3
    function parameters = num1, num2, num3
    function invocation = on line 5, to the right of the '=' assignment
    function return value = local variable result with value 24
    all identifiers = multiply_numbers, num1, num2, num3, result, product
    '''
)