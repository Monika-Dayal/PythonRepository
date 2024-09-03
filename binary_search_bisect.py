import bisect


def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    if i < len(arr) and arr[i] == x:
        return i
    else:
        return -1


input_array = [2, 4, 6, 9, 10, 13, 33]
search_input = 6
result = binary_search(input_array, search_input)

if result != -1:
    print("Result found at position: ", result)
else:
    print("Input not present in given array.")
