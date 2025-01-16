# Check if Array is Sorted 
# Problem: Write a function to check if an array is sorted in ascending  order.  
# Testcase 1: 
# Input: [1, 2, 3, 4, 5] 
# Output: true 
# Explanation: 
# The array [1, 2, 3, 4, 5] is sorted in ascending order.

n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)
is_sorted = False
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        is_sorted = True
    else:
        is_sorted = False
        break
print(is_sorted)


