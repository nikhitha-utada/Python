# Write a program that takes a string, string should be of even length. Divide the string into two equals parts, check the number of vowels in both the parts of the string. If both parts of string have same number of vowels then return true otherwise return false.

# Testcase1	:  rebels
# Output     	:  true
# Explanation 	:  Given sring rebels divided into two parts, reb and els. In both parts vowels count is same that is 1(e is presented in both the parts) so it returns true.

# Testcase2	:  apples
# Output     	:  true

# Testcase1	:  mars
# Output     	:  false

str = input("enter the string: ")
if len(str)%2==0:
    sub1 = str[0:len(str)//2]
    sub2 = str[len(str)//2:]
    # check = "AEIOUaeiou"
    count1=0
    count2=0
    for i in sub1:
        if i in "aeiouAEIOU":
            count1+=1
    for i in sub2:
        if i in "aeiouAEIOU":
            count2+=1
    if count1==count2:
        print("true")
    else:
        print("false")
else:
    print("the string contains odd number of characters")    

