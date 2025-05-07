car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

car.pop('mileage', None)    # safe guards against trying to delete a key that doesn't exist
print(car)