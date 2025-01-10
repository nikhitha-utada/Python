# Write a program to print the vowels in the given string in reverse order.  
# Testcase1 : Helloworld  
# Output : ooe  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  reverse order of eoo is ooe.  
# Testcase1 : JackspArrow  
# Output : oAa  
# Explanation : Vowels in the given string JackspArrow are a,A,o . The  reverse order of aAo is oAa.

# method 1:
str = input("Enter the string: ")
check = "aeiouAEIOU"
vow = ""
for i in str:
    if i in check:
        vow+=i
# print(vow[::-1])

# method 2:
for i in reversed(vow):
    print(i,end="")