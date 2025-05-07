
# str.join(iterable) expects one iterable argument
print(' '.join(['hello', 'world']))

# if anything other than 1 iterable argument is given, a TypeError will be raises:
print(' '.join())                       # TypeError: wrong number of arguments
print(' '.join(['hello'], ['world']))   # TypeError: wrong number of arguments
print(' '.join(1234))                   # TypeError: iterable expected