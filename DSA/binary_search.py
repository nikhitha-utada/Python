#Binary search algorithm divides the array into half and check the one half if the number is greater or less than other half.
#It returns the index of number
#It is Used for SORTED elements only.
#Its is Best for large sized arrays.
#Time complexity:
    # Best case scenario: O(log(1))
    # Average case scenario : O(log(N))
    # Worst case scenario : O(log(N))
#Space-Complexity : O(1)

def binary_search(arr,key):
    low=0
    high=len(arr)-1

    while low<=high:
        mid = (low+high)//2
        if arr[mid]==key:
            return mid
        else:
            if arr[mid]>key:
                high=mid-1
            elif arr[mid]<key:
                low=mid+1
    return mid
  
n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element of the array: "))
    arr.append(element)
key = int(input("Enter the key to be searched: ")) 
arr.sort() 
print(arr)
print(binary_search(arr,key))