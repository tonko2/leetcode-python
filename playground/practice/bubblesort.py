def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
my_list = [5, 4, 2, 1, 3]
bubble_sort(my_list)
print(my_list)