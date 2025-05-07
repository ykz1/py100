def extract_region(locale):
    return locale[locale.find('_') + 1 : locale.find('.')]  # does my spacing here correctly follow Python style convention?


print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR