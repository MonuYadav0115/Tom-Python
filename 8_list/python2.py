
# 2 Writting a data ---- > indexing and slicing 


# rewrite a value in list

# l1 = [1,2,3,4,5,6,8]
# l1[3] = 10  # replace (4 --> 10)
# x1 = l1
# print(x1)


# l1 = [12,13,14,15,16,17,18]
# l1[3] = [11,12]            # output -->[12, 13, 14, [11, 12], 16, 17, 18]
# x1 = l1 
# print(x1)


# Writing in list through the slicing 

# l1 = [11,12,13,14,15,16,17]
# l1[3] = [21,22,23]
# x1 = l1 
# print(x1)   # [11, 12, 13, [21, 22, 23], 15, 16, 17]


# Updating the list throuth the slicing method 

# l1 = [11,12,13,14,15,16,17,18]
# l1[0:0] = [10,21,22]
# x1 = l1 
# print(x1)



#  2 

# l2 = [20,21,22,23,24,25]
# l2[3:3] = [33] 
# x2 = l2 
# print(x2)


#  3 

# l1 = [11,12,13,14,15,16,17]
# l1[2:5] = [10]
# x1 = l1
# print(x1)   # [11, 12, 10, 16, 17] 


# 4  in step method try to check currect value 

# l1 = [1,2,3,4,5]
# l1[::2] = [10,11,12]
# x1 = l1 
# print(x1)


# 5 

l1 = [1,2,3,4,5]
l1[::-1] = [10,11,12,13,14]
x1 = l1
print(x1)
