"""
Homework 8
>Problem 1

Author: Derrick Unger
Date: 3/7/20
CSC232 Winter 2020
"""

# Bubble Sorting
arr = [9, 3, 5, 6, 8.8, 5, 100, -5.5, 0, 2020]  # Define your array here
n = len(arr)  # Define length of array here

# Traverse through all array elements
for i in range(len(arr)):

    # Last i elements are already in place
    for j in range(0, n-i-1):

        # Swap if the element found is greater than the next element
        if arr[j] > arr[j+1]:  # Ascending Order
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted Array: ", arr)
