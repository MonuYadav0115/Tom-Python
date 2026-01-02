# Anagram project

s1 = input("enter Phrase1")
s2 = input("enter Phrase2")

s1 = s1.lower()
s2 = s2.lower()

for x in s1:
    if x.isalpha():
        if s1.count(x) != s2.count(x):
            print("Not anagram")
            break
else:
    print("anagram")
    