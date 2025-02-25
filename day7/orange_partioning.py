n = int(input().strip())
arr = list(map(int, input().split()))
pivot = arr[-1]
k = 0
for i in range(n - 1):
    if arr[i] <= pivot:
        arr[i], arr[k] = arr[k], arr[i]
        k += 1
arr[k], arr[-1] = arr[-1], arr[k]
print(''.join(str(x) for x in arr))
