# what is class and object in python --> in python everything is a object if you  
# are create any programm so first prepare the plan like example: building house in page you create plan this plan based you build so many building ---> class in page and object is a what are you building real building 

s1 = "hello"
# s2 = s1.capitalize()       # -------> in object and class to find (.) symble


s1 = "Hello how are you"
x = s1.find("o") 
# print(x)             # -----> 4 index

x1 = s1.rfind("o")
# print(x1)            #------>15 index 

x2 = s1.find("how")
# print(x2)            #-------> 6 index

x3 = s1.find("k")
# print(x3)            # -------> -1 becoused k is not availbe in s1 string 

x4 = s1.find("o",6)
# print(x4)            # means after index 6 o is availbe which index  output-> 7

x5 = s1.find("o",5,6)
# print(x5)            # -1 becoused o is not there between index 5 to 6 

# Same work like 2-rfind and 3-index and 4-rindex 
# rfind word a revers 
# index is work same but little bit different if you search index like not availbe in string so he will give (error)

x6 = s1.count("o") 
# print(x6)            # ------> 3 becoused o is 3 time in string if not found so give 0

# ************************* index *************************

# always remeber in index you give char not a index number what are you find which index you give it

monu = "Monu tom" 
tom = monu.index("u")
print(tom)             # output --->3





