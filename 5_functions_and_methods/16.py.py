def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

'''
Question: In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

Answer:
Function names:     multiply (lines 1, 9),
                    get_num (lines 4, 7, 8), 
                    float (line 5), 
                    input (line 5),
                    print (line 10)
Parameters:         left, right (defined on line 1, used as local variable
                    on line 2),
                    prompt (defined on line 4, used as local variable on line 5)

'''