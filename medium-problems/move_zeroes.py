# Move Zeros to End

# Problem: Write a function that moves all zeros in an array to the end while maintaining the order of other elements.
# Testcase 1:
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# method-1:
arr=list(map(int,input("Enter the first array elements : ").split()))
arr2=[]
for i in arr:
    if i == 0:
        arr2.append(i)
        arr.remove(i)
print(arr)
print(arr2)
print(arr+arr2)
