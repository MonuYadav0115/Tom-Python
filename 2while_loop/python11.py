n = int(input("enter here:"))

i = 0 

max = float("-inf")
min = float("inf")

while i < n:
    i = i + 1
    x = int(input("enter here next number:"))
    if x > max:
        max = x 
    if x < min:
        min = x 

print("Number of max and min",max,min )
