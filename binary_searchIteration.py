def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            high = mid - 1
            #low = mid + 1
        elif arr[mid] > x:
            low = mid + 1
            #high = mid - 1
        else:
            return mid
    return -1


arr = [2, 3, 5, 8, 9, 12]
print (arr[::-1])
x = 5
result = binary_search(arr[::-1], x)
if result != -1:
    print("Result is present at position: ", str(result))
else:
    print("Element is not present in array.")
