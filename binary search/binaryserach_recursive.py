def binary_search(list, item, low, hight):
    if len(list) == 1:
        return guess if item == guess else None
    middle = ((low + hight) // 2)
    guess = list[middle]
    if guess == item:
        return middle
    else:
        return binary_search(list, item, low=low, hight=middle-1) if guess > item else binary_search(list, item, low=middle + 1, hight=hight)

example_list = [1, 3, 4, 5, 7, 9, 10, 11]

print(binary_search(example_list, 7, 0, len(example_list) - 1))
print(binary_search(example_list, 2, 0, len(example_list) - 1))
print(binary_search(example_list ,-2, 0, len(example_list) - 1))
print(binary_search(example_list ,12, 0, len(example_list) - 1))