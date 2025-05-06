def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

print(
    '''
    The error occurs in line 6 when Python looks for the variable "counter" in the global scope
    but doesn't find anything because "counter" is not defined in the global scope. We want to
    look in the outer scope within all_actions instead, and so we replace "global" with "nonlocal"
    '''
)