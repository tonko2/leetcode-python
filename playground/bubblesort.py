def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    return arr

my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = bubble_sort(my_list)
print("ソートされたリスト:", sorted_list)