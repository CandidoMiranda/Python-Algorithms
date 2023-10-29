def searchMinValue(arr):
    minValue  = arr[0]
    minValueIndex = 0
    for index in range(1, len(arr)):
        if arr[index] < minValue:
            minValue = arr[index]
            minValueIndex = index
    return minValueIndex

def selectionSort(arr):
    newArr = []
    for index in range(len(arr)):
        minValueIndex = searchMinValue(arr)
        newArr.append(arr.pop(minValueIndex))
    return newArr

print(selectionSort([5, 3, 6, 2, 10, 9, 12]))
print(selectionSort([8, 13, 9, 1, 5, 3, 10]))
