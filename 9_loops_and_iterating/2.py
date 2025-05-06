age = int(input('How old are you? '))

print(f'You are {age} years old.')

for duration in range(10, 50, 10):
    print(f'In {duration} years, you will be {age + duration} years old.')