# pattern program in python upper trinagle

# method 1

# for i in range(1,6):
#     for j in range(1,6):
#         if i<=j:
#             print("*",end=" ")
#     print("")


# method 2 

# for i in range(1,6):
#     for j in range(1,6-(i-1)):
#         print("*",end=" ")
#     print("")


# method 3 

for i in range(1,6):
    print("* " * (6-i)) 
