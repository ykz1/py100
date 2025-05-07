speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)
print(
    '''
    1. braking_force < acceleration returns True
    2. speed > 0 is true and so (...) returns true
    3. both operands left of and right of 'and' are true
    
    True will be printed

    '''
)


is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)
print(
    '''
    1. again, braking_force < acceleration returns True
    2. speed > 0 will be evaluated next to be False
    3. the 'and' operator will return False as a result of ^ speed > 0 returning false
    4. acceleration > 0 will return True
    5. the 'or' operator will return True and assign that to is_moving

    Again, True will be printed but we got there in a different way. The parentheses are indeed needed because—despite the same result—the expression evaluation sequence was different here.

    '''
)