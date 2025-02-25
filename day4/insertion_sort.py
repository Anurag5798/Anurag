import sys

def merge_sort(strings):
    if len(strings) <= 1:
        return strings
    mid = len(strings) // 2
    left = merge_sort(strings[:mid])
    right = merge_sort(strings[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

input_list = sys.argv[1:]
print('User given strings are:')
print(input_list)

sorted_list = merge_sort(input_list)
print('Sorted strings are:')
print(sorted_list)
