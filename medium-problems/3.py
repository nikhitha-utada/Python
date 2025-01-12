# Write a program that takes array of numbers as input, among the numbers in array, print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.

# Testcase1	:  [ 7, 4, 7, 23, 10 ]
# Output     	:  4 10
# Explanation : In the given array of number [ 7, 4, 7, 23, 10 ] the numbers 4 and 10 by adding one to these numbers, they formed prime number 5 and 11. So the output is 4 10.

arr = []
n = int(input("enter the number of elements in an array: "))
for i in range(n):
    num = int(input("Enter the element: "))
    arr.append(num)
for num in arr:
    check=num+1
    is_prime = True
    for i in range(2,check):
        if check%i==0:
            is_prime = False
            break
    if is_prime:
        print(num)

