# Pair Sum

# Problem: Write a function to find all pairs in an array whose sum is equal to a given target.
# Testcase 1:
# Input: [2, 4, 3, 5, 7, 8, 9], 7
# Output: [[4, 3], [2, 5]]

arr=list(map(int,input("Enter the array elements : ").split()))
target=int(input("Enter the target : "))
res=[]
# res1=[]
for i in arr:
    for j in range((arr.index(i))+1,len(arr)):  #accesing the next element
        if i+arr[j]==target:
            res.append([i,arr[j]])
print(res)