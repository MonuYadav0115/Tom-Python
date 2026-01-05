
# list comprehension 

# 1 this is called list comprehension 

l = [x for x in range(1,5)]
print(l)



# 2 squer in list all element 

l2= [x * 2 for x in range(1,6)] 
print(l2)


# 3 


l3 = [x.lower() for x in "PyTHoN"]
print(l3)


# 4 

l4 = [x for x in "12345"]
l5 = [int(x) for x in "12345"]

print(l4)
print(l5)


# 5  

l6 = [x for x in "abc$#@2263kjfje"]
l7 = [x for x in "abc$#@2263kjfje" if x.isalpha()]
print(l6)
print(l7)
