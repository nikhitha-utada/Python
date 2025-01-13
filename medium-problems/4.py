# Write a program that takes array of numbers as input and a number as second input. Check the position of the factorial of the second input number in the given array. Print the position of it. If the factorial of given second input number is not presented in the array then print factorial of  the number is not presented.

# Testcase1	:  [ 61, 4, 6, 7, 120 , 10 ]
# Input :  5
# Output     	: 4
# Explanation : In the given array of numbers[ 61, 4, 6, 7, 120 , 10 ], the factorial of second input number 5 is 120, it is presented at 4th position. So output is 5.

# Testcase1	:  [ 61, 4, 6, 7, 120 , 10 ]
# Input 2:  7
# Output     	: Factorial of 7 is not presented.
# Explanation	: Factorial of the second input number 7 is not presented in the given array of numbers.

lst=[]
rang=int(input("Enter the number of elements : "))
for i in range(0,rang):
    num=int(input("Enter the elements  : "))
    lst.append(num)
test=int(input())
fact=1
for i in range(1,test+1):
    fact*=i
for i in lst:
    if i==fact:
        ans=lst.index(fact)
    else:
        ans=(f"factorial of {test} is not presented")
print(ans)