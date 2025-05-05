def all_caps(string):
    return string.upper() if len(string) > 10 else string

print(all_caps('hello world'))
print(all_caps('goodboye'))