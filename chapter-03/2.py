#  Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# '''
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
name = input("Enter the name: ") 
date = input("Enter today's date: ")
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))