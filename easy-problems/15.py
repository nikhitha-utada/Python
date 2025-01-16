# Remove Duplicates from an Array  
# Problem: Write a function to remove duplicate values from an array.  
# Testcase 1:  
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]  
# Explanation:  
# The duplicates 2 and 4 are removed from the array, leaving [1, 2, 3,  4, 5]. 


def remove_duplicate(arr):
    unique_elements = []  # To store unique elements
    for i in arr:
        if i not in unique_elements:  # Add the element if it's not already added
            unique_elements.append(i)
    print(unique_elements)

# Input part
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter the element: "))
    arr.append(element)

remove_duplicate(arr)


        

