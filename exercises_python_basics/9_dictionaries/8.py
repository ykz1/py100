car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

car2 = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
]

# Alternative below

car3 = []
for (key, value) in car.items():
    car3.append([key, value])

print(car)
print(car2)
print(car3)