def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

'''
Function names      say
Method names        upper, lower
Built-in functions  print, input, max
'''