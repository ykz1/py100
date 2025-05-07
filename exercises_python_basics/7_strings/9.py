def starts_with(string, lookup):
    return string.startswith(lookup)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True