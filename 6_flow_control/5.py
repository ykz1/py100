def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

print('Empty will be printed because [] will be passed as an argument to our method, and the empty list will evaluate as falsy which takes us to the else in our if statement.')