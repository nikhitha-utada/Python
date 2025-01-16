# Find Unique Elements  
# Problem: Write a function to find the unique elements in an array  
# (elements that appear only once).  
# Testcase 1:  
# Input: [1, 2, 2, 3, 4, 4, 5]  
# Output: [1, 3, 5]  
# Explanation:  
# The unique elements that appear only once in the array are 1, 3, and 5.

def unique(arr):
    unique_arr = []
    for i in arr:
        # count=0
        for j in arr[arr.index(i)+1:]:
            if i==j:
                arr.remove(i)
                arr.remove(j)
    return arr

n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)
print(unique(arr))


    