#  Write a program that takes a number as input, print the sum of duplicate
#  numbers in the given number.
#  Testcase1 : 7473183
#  Output
#  : 10
#  Explanation : In the given number 747383, duplicate digits are 7 and 3
#  because they occurred more than once in the number. So the sum of 7 and 3
#  are 10.
#  Testcase1 : 234234
#  Output
#  : 9
#  Explanation : In the given number 234234, duplicate digits are 2, 3 and 4
#  because they occurred more than once in the number. So the sum of 2, 3 and
#  4 are 9.

# Program to calculate the sum of duplicate digits in a given number without a dictionary

# Input: A number from the user
num = input("Enter the number: ")

# Convert the number into a list of its digits
digits = list(map(int, num  ))  # Convert each character to an integer

# List to store digits that have already been processed
seen = []
duplicate_digits = []

# Check for duplicates
for digit in digits:
    if digit in seen and digit not in duplicate_digits:
        duplicate_digits.append(digit)  # Add to duplicate list if not already added
    else:
        seen.append(digit)

# Calculate the sum of duplicate digits
duplicate_sum = sum(duplicate_digits)

# Print the result
print("Sum of duplicate digits:", duplicate_sum)



#method-2
num=input("enter : ")
lst=list(map(int,num))
dup=[]
for i in lst:
    j=i+1
    count=0
    for j in lst:
        if i==j:
            count+=1
    if count>1:
        dup.append(i)
dup=set(dup)
print(sum(dup))

