# Write a program to check whether the sum of digits in the number except  
# first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal  
# Testcase1 : 75547  
# Output : equal  
# Explanation : In the given number 7557, first digit and last digit sum  that is sum(7,7)=14 is equal to sum of remaining numbers that is  sum(5,5,4) = 14. So both sums are equal.  
# Testcase1 : 765  
# Output : not equal  
# Explanation : Sum(7,5)=12 and Sum(6)=6, both sums are not equal. 


num=int(input("Enter a number :"))
temp2=num
temp1=num
last=temp1%10
count=0
while temp1>0:
    temp1//=10
    count+=1
first=temp2//10**(count-1)
fila=first+last
sum=0
while temp2>0:
    sum+=temp2%10
    temp2=temp2//10
remain=sum-fila
if fila!=remain:
    print("not equal")
else:
    print("equal")


