def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)  # This line will raise a TypeError because our method accepts 1 argument but 6 were given here.
find_first_nonzero_among(1) # This line will also cause a TypeError because an int is passed to our method as an argument but line 2 expects an iterable instead
