# Prefix and suffix

# Startwith(prefix, start, end)

# 1

s1 = "Hii how are you "
x = s1.startswith("How")
# print(x)                # output --->false

# 2
s2 = "Hello How are you "
x1 = s2.startswith("Hello")
# print(x1)                    # output ----> true


# 3
s3 = "Hello how are you"
x2 = s3.startswith("how",6)
# print(x2)                     #output ---------->true


# Endswith(suffix,start,end)
# 1
s4 = "Hello monu what are you doing"
x3 = s4.endswith("doing")
# print(x3)                         #output ---------->true


# 2 

s5 = "monuy7883@gmail.com"
x4 = s5.endswith("com")
# print(x4)                            #output ---------->true


# removeprefix(prefix)

s6 = "Python is my favorite language"
x5 = s6.removeprefix("Py")
# print(x5)                      #output -->thon is my favorite language


# removesuffix(suffix)

s7 = "Python programming"
x6 = s7.removesuffix("ing")
# print(x6)                    #output---> Python programm


# partition(sep)

s8 = "Python is programming"
x7 = s8.partition("is")
# print(x7)     # output ---> ('Python ', 'is', ' programming')

# rpatition(sep)

s9 = "Python is easy"
x8 = s9.rpartition("s")
# print(x8)        # output ---> ('Python is ea', 's', 'y')
