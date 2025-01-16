# Sum of Even Numbers  
# Problem: Write a function that returns the sum of all even numbers in an  
# array.  
# Testcase 1:  
# Input: [1, 2, 3, 4, 5]  
# Output: 6  
# Explanation: 
# The even numbers in the array are 2 and 4. Their sum is 2  

def sum_of_even(arr):
    res=[]
    for i in arr:
        if i%2==0:
            res.append(i)
    return sum(res)

n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element: "))
    arr.append(element)
print(sum_of_even(arr))



