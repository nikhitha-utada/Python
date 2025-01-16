# Check if a String is a Palindrome 
# Question: Write a function to check if a given string is a palindrome. 
# Testcase: "racecar" 
# Output: true 
# Explanation: A palindrome is a string that reads the same forward and 
# backward. Since "racecar" is the same in both directions, the output is 
# true. 

# method-1:
str=input("enter the string: ")
palindrome = str[::-1]
if(str==palindrome):
    print("its a palindrome")
else:
    print("its not a palindrome")