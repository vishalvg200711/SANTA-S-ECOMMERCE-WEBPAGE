def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Input list
arr = [10, 20, 30, 40, 50]

# Element to search
key = int(input("Enter the element to search: "))

# Search operation
result = linear_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")