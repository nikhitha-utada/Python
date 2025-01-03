#Check the type of variable assigned using input () function
a = input("Enter the variable: ")
var_type = type(a)
print(var_type)

'''Use comparison operator to find out whether a given variable a is greater than
b or not. Take a = 34 and b = 80'''
a = 34
b = 80
print(a>b)


#Write a python program to find an average of two numbers entered by the user.
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
avg = (num1+num2)/2
print("Average of",num1,"and" ,num2 ,"is",avg)


#Write a python program to calculate the square of a number entered by the user.
num = int(input("Enter the number: "))
square = num*num
print("Square of",num,"is",square)