# Reseting password

password1 = input("enter here:")
password2 = input("enter here:")

if password1 == password2:
    print("Password changed")
elif password1.casefold() == password2.casefold():
    print("Please check cases try again")
else:
    print("Password do not match")
    
