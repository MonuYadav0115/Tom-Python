# check number is palindrome or not 

num = int(input("enter here:"))

rev = 0
m = num 

while num > 0:
    r = num % 10
    rev = rev * 10 + r 
    num = num // 10 
if rev == m:
    print("palindrome")
else:
    print("not a palindrome")

