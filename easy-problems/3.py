# Write a program to print factorial of the number.  
# Testcase1 : 3  
# Output : 6  
# Explanation : Factorial of the number 3 is 3*2*1 = 6.  
# Testcase1 : 4  
# Output : 24  
# Explanation : Factorial of the number 4 is 4*3*2*1 = 24.

#Method 1
num=int(input("Enter your number :"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

