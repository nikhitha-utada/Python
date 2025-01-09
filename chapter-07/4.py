# Write a program to find whether a given number is prime or not. 
 
num = int(input('enter the number: '))
isPrime = True
for i in range(2,num):
    if(num%i==0):
        isPrime = False
if(isPrime):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")