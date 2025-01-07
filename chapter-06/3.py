#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

#we can use in keyword as well....

sentence = input("Enter the sentence that you want to check for the presence of spam comment: ")
spam = sentence.find("Make a lot of money" or "buy now" or "subscribe this" or "click this") #find() finds for a substring if it is present in the string it returns the index else returns -1.
if(spam == -1):
    print("It doesnot contain spam comment")
else:
    print("It is a spam comment")