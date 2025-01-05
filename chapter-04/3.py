# Check that a tuple type cannot be changed in python. 

tuple1 = (1,2,3,"hi")
tuple1[2] = "ksjfks"
# print(tuple1) ---> throws error as tuple cant be changed
