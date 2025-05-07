def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

'''
The problem is that our user's input is stored as a string, and that string is passed to our method. A string multiplication results in a concatenation, which is why we get our user's input repeated 5 times in the final output.

Fixed in line 5 above. There are other places we can conduct this integer conversion, but this is the best place in case we want to use the variable number in other numeric calculations elsewhere.
'''