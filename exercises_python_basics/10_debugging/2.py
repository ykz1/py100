import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()


'''
The error is in line 4, where we were originally sampling from two string elements, which both will evaluate as True on line 6 because non-empty strings are truthy in Python.

Fixed in above.
'''
