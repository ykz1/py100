grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while len(grocery_list) > 0:
    print(grocery_list[0])
    grocery_list.remove(grocery_list[0])

print(grocery_list)


# Another option below, probably more pythonic 

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while len(grocery_list) > 0:
    print(grocery_list.pop(0))

print(grocery_list)