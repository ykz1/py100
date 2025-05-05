def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # This will print 'Product2' because it matches line 5

bar_code_scanner(142)   # This will print 'Product not found!' because integer