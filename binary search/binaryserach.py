def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        middle = int((low + hight) / 2)
        guess = list[middle]

        if guess == item:
            return middle
        elif guess > item:
            hight = middle - 1
        else:
            low = middle + 1
    return None

example_list = [1, 3, 4, 5, 7, 9, 10, 11]

print(binary_search(example_list, 7))
print(binary_search(example_list, 2))
print(binary_search(example_list ,-2))
print(binary_search(example_list ,12))