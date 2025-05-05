print(1 or 2 and 3)
print(1)
print()


print(0 or 2 and 3)
print(3)
print()

print(1 or 0 and 3)
print(1)
print()

print(1 or 2 and 0)
print(1)
print()

print(0 or 0 and 3)
print(0) # the second one
print()

print(0 or 2 and 0)
print(0) # the third one
print()

print(1 or 0 and 0)
print(1)
print()

print(0 or 0 and 0)
print(0) # the second one
print()

print(1 and 2 or 3)
print(2)
print()

print(0 and 2 or 3) # why does this produce 3? same as below, because "false or true" evaluates to true
print(0)
print()

print(1 and 0 or 3)
print(3)
print()

print(1 and 2 or 0)
print(2)
print()

print(0 and 0 or 3) #why does this produce 3? right because false or true evaluates to true...
print(0) # the first one
print()

print(0 and 2 or 0)
print(0) # the first one
print()

print(1 and 0 or 0)
print(0) # the last one
print()

print(0 and 0 or 0)
print(0) #the first one
print()