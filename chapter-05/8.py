#If languages of two friends are same; what will happen to the program in problem 6? 
#answer: returns the value without giving any error....

fav_lang = {
    "harry" : "hindi",
    "hari" : "telugu",
    "ravi" : "telugu",
    "anil" : "tamil"
}

name  = input("enter the person's name: ")
print(f"{name}'s fav language is {fav_lang[name]}")