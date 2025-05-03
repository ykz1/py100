obj = 42
obj = 'ABcd'        # re-assign
obj.upper()
obj = obj.lower()   # re-assign
print(len(obj))
obj = list(obj)     # re-assign
obj.pop()           # mutate
obj[2] = 'X'        # mutate
obj.sort()          # mutate
set(obj)            
obj = tuple(obj)    # re-assign