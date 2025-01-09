# Write a program to calculate the factorial of a given number using for loop.

num = int(input("enter the number you want to find the factorial for: "))
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"factorial of {num} is {fact}")