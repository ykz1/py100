foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

print("'bar' is printed because of variable shadowing: the assignment that happens on line 4 applies to a local variable foo which is specific to set_fool()'s scope, and that foo is different from the outer scope foo printed in line 7")