def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two sorted subarrays into result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Input the array elements
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

# Sort the array using merge sort
sorted_arr = merge_sort(arr)

# Output the sorted array
print("Sorted array:", " ".join(map(str, sorted_arr)))
