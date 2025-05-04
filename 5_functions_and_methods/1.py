def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# This raises an error because the local variable foo is only in-scope within the function set_foo()'s definition, and as a result is not available i.e. is out-of-scope when referenced in line 5