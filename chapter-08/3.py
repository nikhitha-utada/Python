# Write a recursive function to calculate the sum of first n natural numbers. 

def sum(num):
   if num==1:           #this base condition is written to stop the function from going into infinite loop.
      return 1
   return sum(num-1)+num        # 1+2+3+4+.....+(n-1)+(n)

num = int(input("enter the number: "))
print(sum(num))
