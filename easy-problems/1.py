# Write a program to print the sum of the digits in the number.  
# Testcase1 : 101  
# Output : 2  
# Explanation : Sum of the digits in the number 1+0+1 = 2, Answer is 2.  
# Testcase1 : 567  
# Output : 18  
# Explanation : Sum of the digits in the number 5+6+7 = 18, Answer is  18.  

num = int(input("Enter a number: "))
last=0
sum=0
while(num>0):
    last = num%10
    sum+=last
    num = num//10
print(sum)

