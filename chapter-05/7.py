# If the names of 2 friends are same; what will happen to the program in problem 6?
#answer: it returns the last given value to that key...

fav_lang = {}
name = input("Enter the name : ")
lang = input("enter the language: ")
fav_lang.update({name:lang})
name = input("Enter the name : ")
lang = input("enter the language: ")
fav_lang.update({name:lang})
name = input("Enter the name : ")
lang = input("enter the language: ")
fav_lang.update({name:lang})
name = input("Enter the name : ")
lang = input("enter the language: ")
fav_lang.update({name:lang})
print(fav_lang)