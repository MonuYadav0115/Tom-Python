# Data cleaning

scan = input("enter here:")
clean = ""

for x in scan:
    if x.isalpha() or x.isspace():
        clean  = clean + x 
    else:
        clean = clean + " "
print("Clean" , clean)
