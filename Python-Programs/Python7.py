def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found

# Input the sorted array elements
arr = list(map(int, input("Enter sorted array elements separated by spaces: ").split()))
target = int(input("Enter the element to search: "))

# Perform binary search
index = binary_search(arr, target)

# Output the result
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found in the array.")
