def linear_search(arr, search):
    for index, value in enumerate(arr):
        if value == search:
            return index
    return -1 

# Input the array elements
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
search = int(input("Enter the element to search: "))

# Perform linear search
index = linear_search(arr, search)

# Output the result
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found in the array.")
