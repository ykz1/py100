def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

print("42, 3, 2 are printed because 1 argument is passed to foo so the default values for parameters 2 and 3 are used")