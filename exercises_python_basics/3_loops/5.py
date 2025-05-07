lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

# If the provided list is empty, nothing would be printed because len(lst) is 0, and with index at 0 the condition (index < len(lst)) would already be false and the block within while will never be executed.

lst = []
index = 0

while index < len(lst):
    print(lst[index])
    index += 1