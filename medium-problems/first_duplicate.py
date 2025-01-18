# Find the First Duplicate

# Problem: Write a function to return the first duplicate value in an array.
# Testcase 1:
# Input: [2, 1, 3, 5, 3, 2]
# Output: 3

# arr=list(map(int,input("Enter the array elements : ").split()))
# res=[]
# for i in arr:
#     for j in range(arr.index(i)+1,len(arr)):
#         if i==arr[j]:
#             res.append(i)
#             break
# print(res)

def first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num  # First duplicate found
        seen.add(num)
    return -1  # No duplicates found

# Input from the user
arr = list(map(int, input("Enter the array elements: ").split()))
print(first_duplicate(arr))