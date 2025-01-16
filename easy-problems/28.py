# Count Occurrences of a Character 
# Question: Write a function that counts the occurrences of a specific 
# character in a string. 
# Testcase: "hello world", "l" 
# Output: 3 
# Explanation: The character 'l' appears 3 times in the string "hello world". 

#method-1:
str = input("enter the string: ")
char = input("enter the character you want to find the occurences for: ")
count = 0
for i in str:
    if i==char:
        count+=1
print(count)