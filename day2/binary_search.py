def binary_search(array, search_element):
    high = len(array) - 1 
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == search_element:
            return mid
        elif search_element < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [2, 4, 6, 8, 10, 12, 14]
result = binary_search(arr, 8)
print("Index of 8 is", result)
