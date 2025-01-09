# #Write a program to print reverse of the given number.  
# # Testcase1 : 721  
# # Output : 127  
# # Explanation : Reverse of the number 721 is 127.  
# # Testcase1 : 765  
# # Output : 567  
# # Explanation : Reverse of the number 765 is 567.

# # Method1:
num = input("Enter a number: ") 
print(num[::-1])

# # Method2:
num = input("Enter a number: ")
rev=""
for i in range(len(num)-1,-1,-1): #we can give -ve values in the range
    rev+=num[i]
print(rev)

#Method3:
num = int(input("Enter a number: "))
rev = 1
while(num>0):
    last = num%10
    rev*=10+last
    num//=10
print(rev)






