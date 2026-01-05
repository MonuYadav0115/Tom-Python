

# tuple comprehension 


t = (*(x for x in range(1,6) ),)

print(t)

t2 = tuple(x for x in range(1,10))
print(t2)


t3 = tuple(x.lower() for x in "PyTHOn")
print(t3)


t4 = tuple(x for x in "kgdgd$#@%9887JGUU" if x.isalpha())
print(t4)

