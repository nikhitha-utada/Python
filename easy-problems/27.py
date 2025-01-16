# Check if String Contains Only Digits 
# Question: Write a function to check if a string contains only numeric 
# digits. 
# Testcase: "12345" 
# Output: true 
# Explanation: The string "12345" consists only of digits, so the result is 
# true.

#method-1:

num  = input("enter the number: ")
is_digit = False
for i in num:
    if i.isdigit():
        is_digit = True
    else:
        is_digit = False
        break
print(is_digit)


