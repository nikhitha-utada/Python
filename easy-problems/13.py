#  Find the Second Largest Element  
# Problem: Write a function to return the second largest number in an array.  
# Testcase 1:  
# Input: [3, 1, 4, 1, 5, 9]  
# Output: 5  
# Explanation:  
# In the array [3, 1, 4, 1, 5, 9], the second largest number after 9 is 5.

# method-1:

arr=[5,3, 1, 4, 1,  9]
arr.sort()
print(arr[-2])


# method-2:
def largest(arr):
    largest = arr[0]
    for i in arr:
        if(i>largest):
            largest=i
    return largest

n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)
# print(largest(arr))
arr.remove(largest(arr))
print(largest(arr))





