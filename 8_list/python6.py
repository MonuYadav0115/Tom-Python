
# To rotate a list 

l = [1,2,3,4,5,6]

n = int(input("Enter here:"))

rotate = l[n:] + l[:n]

print("Rotated list:", rotate)
