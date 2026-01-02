# sum of digit all number 

n = 12345
sum = 0 
while n>0:
    r = n % 10
    sum = sum + r
    n = n // 10
# print(sum)

m = int(input("enter here:"))

sum = 0 

while m>0:
    r = m % 10 
    sum = sum + r
    m = m // 10

print("sum of number :",sum)
