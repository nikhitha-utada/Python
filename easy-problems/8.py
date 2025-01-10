# Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  
# Testcase1 : Helloworld    eoo "e"
# Output : eo  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  single vowels among them are eo .  

# Testcase1 : Jacksparrow  
# Output : ao  
# Explanation : Vowels in the given string Helloworld are a,a,o . Among  them a is repeated more than once, so consider it for one time , result is  ao.


# method 1:
str = input("enter a string: ")
check = "aeiouAEIOU"
answer = set()
for i in str:
    if i in check:
        answer.add(i)
ans_list = list(answer)
for i in ans_list:
    print(i,end="")


#method 2:
string=input("Enter the string : ")         
check="AEIOUaeiou"
vow=""
for i in string:
    if i in check:
        if i in vow:
            continue
        else:
            vow+=i
print(vow)


