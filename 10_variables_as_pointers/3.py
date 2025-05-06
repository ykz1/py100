dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict3 = dict1

dict1['Monty Python'] = 'Holy Grail'

print(dict1['Monty Python'])    # 'Holy Grail' because we just reassigned this new value 
print(dict2['Monty Python'])    # Remains 'The Life of Brian' because dict() creates a new dict
print(dict3['Monty Python'])    # 'Holy Grail' because dict3 points to the same dict object as dict1
