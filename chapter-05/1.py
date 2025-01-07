#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

my_dict = {"namaste" : "hello",
           "aa jao" : 'cpme here',
            "so jao" : "sleep",
            "ghar" : "home"
        }
word = input("Enter the word you want to search: ")
print(f"The {word} in hindi is {my_dict.get(word)}")