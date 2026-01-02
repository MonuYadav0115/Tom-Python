# count how many digit all 


n = int(input("enter here:"))

i = 0

while n>0:
    i = i + 1
    n = n // 10
print(i)
