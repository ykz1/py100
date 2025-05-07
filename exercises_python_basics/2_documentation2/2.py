iceCreamDensity=10                  
while iceCreamDensity>0 :
    print('Drip...')
    iceCreamDensity-=1

print('The ice cream melted.')

'''
1. Using camelCase for a variable name; should use snake_case
2. Whitespaces—missing in lines 1, 3, and 5; and there is an extraneous one on line 3

Refactored below
'''

print()

ice_cream_density = 10                  

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')
