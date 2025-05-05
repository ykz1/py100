text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

print('Because we are returning the letter f found in two different strings')
print('In line 3 we are looking for f in text[21:35]')
print('In line 4 we are looking for f in the original string, but starting at index 21 and ending at index 24')