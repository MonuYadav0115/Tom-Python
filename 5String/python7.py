# Joining and spliting a string 

# Replace method ------> replace(old,new,count)

s1 = "H-e-l-l-o"
s2 = s1.replace("-",",")
print(s2) # ----->replace (-) to (,) look like H,e,l,l,o

# 2 add count replaced only 3 occurences

s3 = s1.replace("-",',',3)
print(s3) # output like H,e,l,l-o

# if you try replace something not in string so it will give same string example:
# s1.replace("k","m") ---> output same H,e,l,l,o

s4 = "monu@gmail.com"
s5 = s4.replace("gmail","yahoo")
print(s5) # replcae monu@gmail.com to monu@yahho.com if string count less so he will argest like if you replace yahoo to hot then monu@hot.com


