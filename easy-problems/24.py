# Remove Vowels from a String 
# Question: Write a function to remove all vowels from a given string. 
# Testcase: "hello world" 
# Output: "hll wrld" 
# Explanation: After removing the vowels 'e', 'o', and 'o' from "hello world", 
# we are left with "hll wrld".

str = input("enter the string: ")
check = "aeiouAEIOU"
lst=list(str)
res=""
for i in lst:
    if i not in check:
        res+=i
print(res)