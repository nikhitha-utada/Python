#  Count Vowels in a String 
# Question: Write a function to count the number of vowels in a given 
# string. 
# Testcase: "hello world" 
# Output: 3 
# Explanation: The vowels in "hello world" are 'e', 'o', and 'o'. Thus, the total 
# count of vowels is 3.

#method-1:
str=input("enter the string: ")
check = "aeiouAEIOU"
count=0
for i in str:
    if i in check:
        count+=1
print(count)