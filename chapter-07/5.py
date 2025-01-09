# Write a program to find the sum of first n natural numbers using while loop.

num  = int(input("enter the number: "))
sum=0
for i in range(1,num+1):
    sum+=i
print(f"sum of {num} natural numbers is {sum}")