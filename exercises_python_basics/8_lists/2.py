def last(list):
    if list:
        return list[-1]
    else:
        return ''

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))