import random

weather = ['sunny', 'cloudy', 'rainy'][random.randint(0, 2)]

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside.")