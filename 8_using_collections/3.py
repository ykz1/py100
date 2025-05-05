my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
my_tuple = list(my_tuple)
my_tuple.pop()
my_tuple.reverse()
my_tuple.pop()
my_tuple = tuple(my_tuple)
print(my_tuple)

print()

my_tuple = (1, 2, 3, 4, 5)
my_tuple = my_tuple[-2:0:-1]
print(my_tuple)