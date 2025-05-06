def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))
print(
    '''
    1. Python reads do_something's definition into memory without invoking the function
    2. my_dict is defined
    3. do_something is called, and my_dict is passed to it as argument dictionary
    4. dictionary's keys are extracted in dictionary view, kind of like a temporary list
    5. the list is sorted ascending
    6. the second element in the list (with index 1) is extracted, this would be the string 'Chris'
    7. upper is called on string 'Chris', resulting in 'CHRIS'
    8. this final string 'CHRIS' is returned by do_something
    9. finally, 'CHRIS' is printed

'''
)
