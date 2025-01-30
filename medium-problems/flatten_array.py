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




