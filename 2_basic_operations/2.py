x = 4936

print(f'One place is {x % 10}')
print(f'Tens place is {(x % 100) // 10}')
print(f'Hundreds place is {(x % 1000) // 100}')
print(f'Thousands place is {x // 1000}')

print()

print(f'One place is {str(x)[3]}')
print(f'Tens place is {str(x)[2]}')
print(f'Hundreds place is {str(x)[1]}')
print(f'Thousands place is {str(x)[0]}')