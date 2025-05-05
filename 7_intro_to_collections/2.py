stuff = ('hello', 'world', 'bye', 'now')
'''
We cannot change 'bye' to 'goodbye' because tuples are immutable.

We can:
1. Copy stuff into a new tuple with 'bye' changed to 'goodbye'
2. Convert stuff into a list, change the element 'bye', then convert back to a tuple
'''