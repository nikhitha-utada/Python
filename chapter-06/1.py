# Write a program to find the greatest of four numbers entered by the user. 

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))
num4 = int(input("Enter the number: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(f"{num1} is greatest!!!")
elif(num2>num3 and num2>num4):
    print(f"{num2} is greatest!!!")
elif(num3>num4):
    print(f"{num3} is greatest!!!")
else:
    print(f"{num4} is greatest!!!")