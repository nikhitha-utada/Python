# Find Peak Element

# Problem: Write a function to find a peak element in an array. An element is a peak if it is not smaller than its neighbours.
# Testcase 1:
# Input: [1, 3, 20, 4, 1, 0]
# Output: 20

def peak(arr):
    res=[]
    for i in range(0,len(arr)):
        if arr[i]==arr[0]:
            if arr[i]>arr[i+1]:
                res.append(arr[i])
        elif arr[i]==arr[-1]:
            if arr[i]>arr[i-1]:
                 res.append(arr[i])
        else:
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                 res.append(arr[i])
    print(res)

arr=list(map(int,input("Enter the array elements : ").split()))
peak(arr)