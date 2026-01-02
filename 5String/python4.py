# Card Payment Reciept
# Example XXXX XXXX XXXX 5678


CardNo = input("enter here:")
lastdigit = CardNo[15:]
four = "X" * 4 + " "
dispcardNo = four * 3 + lastdigit
# print(dispcardNo)


# netx method same problem 

cardNumber = input("Enter here:")
ShowcardNumber = cardNumber[15:]
hidingCardnumber = "X" * 4 + " "
DisplaycardNumber = hidingCardnumber * 3 + ShowcardNumber
print(DisplaycardNumber)

