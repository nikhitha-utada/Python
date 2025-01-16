#  Reverse an Array  
# Problem: Write a function to reverse the elements in an array.  
# Testcase 1:  
# Input: [1, 2, 3, 4, 5]  
# Output: [5, 4, 3, 2, 1]  


#method-1:
n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)

print(arr[::-1])

#method-2:
n = int(input("enter the number of elements: "))
arr=[]
lst=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)
for i in range(len(arr)-1,-1,-1):
    lst.append(arr[i])
print(lst)