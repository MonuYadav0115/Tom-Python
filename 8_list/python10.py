
# index and sorting 

# 1 index(elemment,start,end)
# 2 count(element)
# 3 reverse()
# 4 sort(key=none,revers=false)


# 1 index(elemment,start,end)

# l =[10,20,30,40,50,60,70,80,90,10,20,30,40,50]
# l1 = l.index(20)
# print(l1)


# l =[10,20,30,40,50,60,70,80,90,10,20,30,40,50]
# l1 = l.index(20,2)
# print(l1)

# l =[10,20,30,40,50,60,70,80,90,10,20,30,40,50]
# l1 =l.index(20,2,13)
# print(l1)


# count(element)

# l =[10,20,30,40,50,60,70,80,90,10,20,30,40,50]
# l1 = l.count(20)
# print(l1)   # 2 times 


# reverse()

# l =[10,20,30,40,50,60,70,80,90,10,20,30,40,50]
# l.reverse()
# print(l)  # its reverse the list 



# sort(key = None , reverese= false)

# l =[10,20,30,40,50,60,70,80,90,10,20,30,40,50]
# l.sort()
# print(l)  # list is incresing order



# l =[10,20,30,40,50,60,70,80,90,10,20,30,40,50]
# l.sort(reverse=True)
# print(l)             # list is reveres order



# l = ["coat","python","javascript","java","html"]
# l.sort()
# print(l)

# l = ["a","c","e" "ersd","adad","dfs"]
# l.sort()
# print(l)


# l = ["coat","python","javascript","java","html"]
# l.sort(key=len)
# print(l)       # smallest word first


# l = ["Dog","dog","bat","apple","html"]
# l.sort()
# print(l)  # fist word capital Dog becoused ASCII 

l = ["Dog","dog","bat","Apple","html","Peacoke"]
l.sort(key=str.lower)
print(l)

