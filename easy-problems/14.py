# Sum of All Elements  
# Problem: Write a function that returns the sum of all elements in an array.  
# Testcase 1:  
# Input: [1, 2, 3, 4]  
# Output: 10 
# Explanation:  
# The sum of the elements 1 + 2 + 3 + 4 = 10.  

# method-1:
n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)
print(sum(arr))

# method-2:
n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)
sum=0
for i in arr:
    sum+=i
print(sum)