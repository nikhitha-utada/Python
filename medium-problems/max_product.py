# Find the Maximum Product of Two Elements

# Problem: Write a function to find the maximum product of two elements in an array.
# Testcase 1:
# Input: [3, 5, -2, 8, 11]
# Output: 8 * 11 → 88

def max(arr):
    max=arr[0]
    for i in arr:
        if i>max:
            max=i
    return max

arr=list(map(int,input("Enter the first array elements : ").split()))
max(arr)
max1=max(arr)
arr.remove(max1)
max(arr)
max2=max(arr)
print(max1*max2)