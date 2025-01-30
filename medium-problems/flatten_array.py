# Flatten a Nested Array

# Problem: Write a function to flatten a nested array into a single array.
# Testcase 1:Improvements :  Very slow in improving

# Target date for completion : 

# Input: [1, [2, [3, [4]], 5]]
# Output: [1, 2, 3, 4, 5]

str = input("enter the string: ")
res=""
for i in str:
    if i!="[" and i!="]":
        res+=i
print("["+res+"]")


# method - 02:
def flatten_array(arr):
    result = []
    for i in arr:
        if type(i) == list:  # Check if the element is a list
            result.extend(flatten_array(i))  # Recursively flatten the list
        else:
            result.append(i)  # Append non-list elements
    return result

# Taking input from the user
nested_list = eval(input("Enter a nested list: "))  # Example: [1, [2, [3, [4]], 5]]

# Flatten and print the result
print("Flattened list:", flatten_array(nested_list))

