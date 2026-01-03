
# Adding Elements 

# 1 Append(element)
# 2 extend(iterable)
# 3 insert(index,element)
# 4 copy()

# 1 

# l = [ 1,2,3,4,5,6,7]
# l.append(8)
# print(l)


# l = [1,2,3,4]
# l.append(5,6)
# print(l)       # error becoused only one value to append 


# l = []
# l.append(12)
# print(l)


# l = []
# l.append(12)
# l.append("python")
# l.append([1,2])
# l.append(22)
# l.append(33)
# print(l)     # [12, 'python', [1, 2], 22, 33]



# slicing 

# l = [1,2,3,4,5]
# l[5:5] = [6]
# l[len(l):] = [7]
# print(l)


# 2 extend 

# l = [1,2,3,4,5]
# l.extend([6,7,8,9])
# print(l)


# l = [1,2,3]
# l.extend ("python")
# print(l)  # [1, 2, 3, 'p', 'y', 't', 'h', 'o', 'n']


# 3 insert(index , value)

# l = [1,2,3,4,5]
# l.insert(0,50)
# print(l)


# l = [1,2,3,4,5]
# l.insert(70,"python")
# print(l)


# l=[1,2,3,4,5,6]
# l.insert(2,"pyton")
# print(l)


# copy()

# l=[1,2,3,4,5]
# l1=l.copy()
# print(l1)

l1 =[11,12,13,13,14,15,16]
l2 = l1.copy()
print(l2)

