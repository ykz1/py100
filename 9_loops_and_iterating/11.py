my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index_1 = 0
while index_1 < len(my_list):
    nested_list = my_list[index_1]
    index_2 = 0
    while index_2 < len(nested_list):
        number = nested_list[index_2]
        if number % 2 == 0:
            print(number)
        index_2 += 1
    index_1 += 1