"""
Dots Alignment Algorithm

Author: Derrick Unger
Date: 2/14/20
CSC232 Winter 2020
"""

# Bubble Sorting
arr = nums  # Define your array here
n = len(nums)  # Define length of array here

# Traverse through all array elements
for i in range(len(nums)):

    # Last i elements are already in place
    for j in range(0, n-i-1):

        # Traverse the array from 0 to n-i-1
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
