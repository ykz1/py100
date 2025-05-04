def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

print("An error will be raised because parameters follwoing a paremeter with a default must also have defaults")

