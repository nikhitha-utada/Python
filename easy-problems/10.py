# Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
# Testcase1 : JohnWick  
# Output : jOHNwICK  
# Explanation : All the upper case letters changed to lower case and vise  versa.  
# Testcase1 : Korean  
# Output : kOREAN  
# Explanation : All the upper case letters changed to lower case and vise  versa.

#Method 1:
str = input("enter a string: ")
print(str.swapcase())

#Method 2:
str = input("enter a string: ")
answer = ""
for i in str:
    if i>='A' and i<='Z':
        answer+=i.lower()
    elif i>='a' and i<='z':
        answer+=i.upper()
    else:
        answer = "It contains special characters"
        break
print(answer)

