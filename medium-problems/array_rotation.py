# Rotate an Array

# Problem: Write a function that rotates an array to the right by a given number of steps.
# Testcase 1:
# Input: [1, 2, 3, 4, 5], 2
# Output: [4, 5, 1, 2, 3]

num = int(input("enter the number of elements: "))
lst = []
for i in range(0,num):
    ele = int(input("enter the element: "))
    lst.append(ele)
k = int(input("enter the k value: "))
for i in range(0,k):
    lst.insert(0,lst[-1])    # adding that element at the start of the list and removing the element at the same time
    # del lst[-1]
    lst.pop(-1)
print(lst)

#method-02:
arr=list(map(int,input("Enter the elements : ").split()))
check=int(input("Enter the value:"))
arr1=[]
arr1=arr[(len(arr)-check):] + arr[0:(len(arr)-check)]
print(arr[(len(arr)-check):])
print(arr[0:(len(arr)-check)])
print(arr1)