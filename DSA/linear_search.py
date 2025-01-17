# checks the key with each and every element of the array from the beginning till the end..if element is found it return the index of the first occurence of that element or if the element is not found it returns -1
# key --> element to be searched
# linear search is also called as sequential search


#algorithm:

#method-1:
def linear_search(arr,key): 
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i   
    return -1

n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element of the array: "))
    arr.append(element)
key = int(input("Enter the key to be searched: "))  
print(linear_search(arr,key))  

#method-2:
def linear_search(arr,key): 
    for i in arr:
        if i==key:
            return arr.index(i) 
    return -1

n = int(input("enter the number of elements: "))
arr=[]
for i in range(0,n):
    element = int(input("enter the element of the array: "))
    arr.append(element)
key = int(input("Enter the key to be searched: "))  
print(linear_search(arr,key))  

