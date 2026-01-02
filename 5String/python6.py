# Topic is Alingment and Padding 
# left justify ---> s.ljust(wirth , fillchar)


s = "Hello"
x= s.ljust(9,"*") # ----> in string 5 word and 4 added * means toal 9 
print(x)


# Right justify ---> s.rjust(wirth,fillchar)

s = "Hello"
x1= s.rjust(8,"#") # --->Before string added # 3 time becouse string 5 total 8
print(x1)

# center string 
s = "Hello"
x3 = s.center(9,"&") # output &&Hello&& means (&)two add first and two add last 
print(x3)

# Zfill method 

s = "Hello"
x4 = s.zfill(9) # 0 fill first 4 index then hello 
print(x4)


# *****************Strip method********************

# 1 - lstrip 

s = "  Hello"
x5 = s.lstrip() # fist 2 spaces removed 
print(x5)

s = "***Hello"
x6 = s.lstrip("*")   # fisrt *** removed and print Hello 
print(x6)

# 2 - rstrip 
s = "Hello   "
x7 = s.rstrip() # last space removed 
print(x7)

s = "Monu&&&&&"
x8 = s.rstrip("&") # last $ sign removed 
print(x8)


# 3 Strip removed both side whatever extra 

s = "**hello**"
x9 = s.strip("*") # its removed both side extra spaces and whatever you want mention it 
print(x9)


# Special string 

S = "&* Tom @#$!"
x10 = S.strip("!@#$&* ") # its will removed first all side extra char then print Tom
print(x10)
