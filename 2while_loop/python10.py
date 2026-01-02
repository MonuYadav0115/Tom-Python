n = int(input("enter here num:"))

i = 0 
max = 0

while i<n:
    i = i + 1
    x = int(input("enter here next num:"))
    if x>max:
        max = x 
print("maximum number:",max)
