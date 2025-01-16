# Write a program that takes array of numbers are input, print the second duplicate number and it’s occurrence.

# Testcase1	:  [ 64, 1, 2, 7, 79, 7, 7, 1, 22]
# Output     	:  Second duplicate number is 7 and it is occurred 3 times
# Explanation	: In the given array [ 64, 1, 2, 7, 79, 7, 7, 1, 22], the second duplicate number is 7 and it is occurred for 3 times.

# Testcase1	:  [ 121, 8, 1, 4, 5, 4, 8, 1 ]
# Output     	:  Second duplicate number is 1 and it is occurred 2 times
# Explanation	: In the given array [ 121, 8, 1, 4, 5, 4, 8, 1 ] the second duplicate number is 1 and it is occurred for 2 times.

#method-1
num=int(input("Enter the number of elements: "))
lst=[]
for i in range(0,num):
    inp=int(input("Enter the numbers : "))
    lst.append(inp)
dup=[]
for i in lst:
    j=i+1
    count=0
    for j in lst:
        if i==j:
            count+=1
    if count>1:
        dup.append(i)
check=0
for i in dup:
    if i==dup[1]:
        check+=1
print(f"Second duplicate number is:{dup[1]} and it is occurred {check} times")