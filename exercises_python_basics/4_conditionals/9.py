sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

print("$3.99 because line 2 will assign the value 3.99 to admission_price since sale is not not True")