# If the names of 2 friends are same; what will happen to the program in problem 6?
#answer: it returns the last given value to that key....

fav_lang = {
    "harry" : "hindi",
    "hari" : "telugu",
    "hari" : "english",
    "anil" : "tamil"
}

name  = input("enter the person's name: ")
print(f"{name}'s fav language is {fav_lang[name]}")