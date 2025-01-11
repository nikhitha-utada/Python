# Write a program to print the string after removing the duplicate characters  in the string.  
# Testcase1 : madam  
# Output : d  
# Explanation : In the given string madam, the duplicates are m,a. After  removing m’s and a’s from the given string we formed a new string d.  
# Testcase1 : donkey  
# Output : donkey  
# Explanation : In the given string there is no duplicate character.

string=input("Enter a string :")
answer=""
for i in string:
    count = 0
    for j in string:
        if i==j:
            count+=1
    if count==1:
        answer+=i
print(answer)
