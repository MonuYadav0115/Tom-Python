# Restaurant Menu - Project 
"""
Example Like this print out

Hot Dog--------$20
Burger---------$20
Pizza----------$20
Donut----------$20

"""
item1 = input("Enter here:")
price1 = "$20"
item2 = input("enter here")
price2 = "$30"
item3 = input("enter here:")
price3 = "$40"
item4 = input("enter here:")
price4 = "$50"
print(item1 + "-" * (30 - len(item1) - len(price1)) + price1)
print(item2 + "-" * (30 - len(item2) - len(price2)) + price1)
print(item3 + "-" * (30 - len(item3) - len(price3)) + price1)
print(item4 + "-" * (30 - len(item4) - len(price4)) + price1)


