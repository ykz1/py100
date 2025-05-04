def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

print("42, 3.141592, 2 are printed. The first two arguments passed are printed, then the third parameter default value of 2 is printed since no third argument is passed")