#Write a program to find whether a given username contains less than 10 characters or not.

username = input("enter the name: ") 
count = len(username)
if(count<10):
    print(f"{username} contains less than 10 characters...")
else:
    print(f"{username} does not contain less than 10 characters...")