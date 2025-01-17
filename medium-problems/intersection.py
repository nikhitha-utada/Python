# Intersection of Two Arrays
#  Problem: Write a function that returns the common elements
#  between twoarrays.
#  Testcase 1:
#  Input: [1, 2, 3], [2, 3, 4]
#  Output: [2, 3]

arr1=list(map(int,input("Enter the first array elements : ").split()))
arr2=list(map(int,input("Enter the second array elements : ").split()))
res=[]
for i in arr1:
    for j in arr2:
        if i==j and i not in res:
            res.append(i)
print(res)