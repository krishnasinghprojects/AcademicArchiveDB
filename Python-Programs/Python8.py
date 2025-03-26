def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input the array elements
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

# Sort the array using selection sort
selection_sort(arr)

# Output the sorted array
print("Sorted array:", " ".join(map(str, arr)))
