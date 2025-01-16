# Find the Largest Element in an Array 
# Problem: Write a function to return the largest number in an array. 
# Testcase 1: 
# Input: [3, 1, 4, 1, 5, 9] 
# Output: 9 
# Explanation: 
# In the array [3, 1, 4, 1, 5, 9], the largest number is 9.

n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    ele = int(input("Enter the element: "))
    arr.append(ele)
largest = arr[0]
for i in arr:
    if i>largest:
        largest = i 
print(largest)

