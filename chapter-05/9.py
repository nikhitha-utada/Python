# Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

#answer: we cannot add list inside a set as they are not hashable if we want to achieve this we have to use tuple instead of list. 
# also we cant modify sets...

s = {8, 7, 12, "Harry", [1,2]} 
s.update()