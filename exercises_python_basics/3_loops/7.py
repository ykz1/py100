cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for element in cities:
    if element == None:
        continue
    print(len(element))
