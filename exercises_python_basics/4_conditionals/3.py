import random
random_number = random.randint(0, 1)

if random_number == 1:
    print('Yes!')
else:
    print('No.')


# One line version below:
print("Yes!") if random_number == 1 else print("No.")

# Alternate one line version:
print("Yes!" if random_number == 1 else "No.")