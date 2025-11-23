def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

my_list = [2, 3, 4, 10, 40]
target_value = int(input("Enter any element to search from array: "))

result = binary_search(my_list, target_value)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")