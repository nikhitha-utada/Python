# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 

def pattern(n):
   if n==0:         #step-3: as soon as the n becomes 0 then it stops the function there itself
      return 
   print("* "*n)    # step-1: for n times n stars will be printed
   pattern(n-1)     # step-2: then it calls the same function recursively until the n becomes 0

n = int(input("enter the number: "))
pattern(n)