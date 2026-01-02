# check string is palindrome or not if not to make it palindrome

s1 = input("enter here:")
s2 = s1.replace(" ","")
rev = s2[::-1]
if s2.casefold() == rev.casefold():
    print(s1)
else:
    palindrome = s2.casefold()+ rev.casefold()
    print(palindrome)


