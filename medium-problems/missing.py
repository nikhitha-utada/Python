# Find Missing Number

# Problem: Given an array of consecutive numbers with one missing, find the missing number.
# Testcase 1:
# Input: [1, 2, 4, 5]
# Output: [3]

arr1=list(map(int,input("Enter the first array elements : ").split()))
arr2=[]
res=[]
for i in range(arr1[0],arr1[-1]+1):
    arr2.append(i)

for i in arr1:
    for j in arr2:
        if j not in arr1:
            res.append(j)
print(list(set(res)))