def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three()

'''

Trick question: we missed the "()" in line 8 when we try to call multiples_of_three, and so nothing will be printed.

Once we add the parentheses to our function call, this will print:
3 / 1 = 3
6 / 2 = 3
9 / 3 = 3
...
30 / 10 = 3
'''