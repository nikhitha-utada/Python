# Write a python function to print multiplication table of a given number. 

def mul(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n = int(input("enter the number: "))
mul(n)