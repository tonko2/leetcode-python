def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        pass
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = merge_sort(my_list)
print("ソートされたリスト:", sorted_list)