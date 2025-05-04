def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

print("Similar to before, this will raise an exception because we try to pass 3 arguments to foo which only has 2 parameters")