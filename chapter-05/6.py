#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

fav_lang = {
    "harry" : "hindi",
    "hari" : "telugu",
    "sai" : "english",
    "anil" : "tamil"
}

name  = input("enter the person's name: ")
print(f"{name}'s fav language is {fav_lang[name]}")