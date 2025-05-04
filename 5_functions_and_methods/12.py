def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

print("An error is raised because foo is called on line 6 with no arguments passed while the method expects at least one argument")