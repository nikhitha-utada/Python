#What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?
#answer : pythons considers 1 and 1.0 as integer itself

s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')
print(len(s)) # 2
print(s) # {20, '20'} 
