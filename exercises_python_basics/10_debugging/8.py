sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"

print(id(matrix[0]))
print(id(matrix[1]))
print(id(matrix[2]))

print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


'''
Originally, in lines 4 and 5 when we generated our starting matrix, we added the object that sub_list points to for all three of our list elements in matrix. Added print statements to show object IDs for matrix's 3 elements in lines 9 to 12 to show this.

What we actually want to do is copy sub_list as 3 new list objects into matrix as elements. Fixed in line 5 above.
'''
