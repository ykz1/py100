def compare_by_length(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    if len1 > len2:
        return 1
    elif len2 > len1:
        return -1
    else:
        return 0


print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0

