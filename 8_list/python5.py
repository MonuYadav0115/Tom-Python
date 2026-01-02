
# Removing Duplicate list 

l = [1,2,3,3,4,5,6,6,7,7,8,8,9]

res = []

for element in l:
    if element not in res:
        res.append(element)
print(res)


