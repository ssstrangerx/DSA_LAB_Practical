def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

my_list = [7,8,9,6,2,1,4,0]
sorted_list = bubble_sort(my_list)
print(sorted_list)

list_b = [9,6,3,25,87,4,10]
sorted_list_b = bubble_sort(list_b)
print(sorted_list_b)
