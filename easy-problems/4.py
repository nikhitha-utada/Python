# Write a program to print middle character(s) in the given string or 
# number.  
# Testcase1 : Wonder  
# Output : nd  
# Explanation : The middle characters in the given word Wonder is nd.  
# Testcase1 : World  
# Output : r  
# Explanation : The middle character in the given word World is r.  Test Case 1 : 6969  
# Output : 96  
# Explanation : The middle character in the given number 6969 is 96.

# method-1
str=input("Enter your value:")
length=len(str)
if length%2!=0:
    print(str[length//2])
else:
    print(str[(length-1)//2]+str[length//2])

# method-2
str=input("Enter your value:")
length=len(str)
mid=""
if length%2==0:
    mid+=str[(length-1)//2]+str[length//2]
else:
    mid+=str[length//2]
print(mid)

# method-3
str=input("Enter your value:")
length=len(str)
mid=str[0:(length//2)+1]
if length%2!=0:
    print(mid[-1])
else:
    print(mid[-2]+mid[-1])


    
