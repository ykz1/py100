destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, destinations):
    return destinations.count(city) > 0

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False