import random
"""
list=[18,23,"abhay","varad"]

for i in list:
    print(i)

    
"""

#random number genaeration like OTP



otp=random.randint(1000,9999)


print("Welcome sir")
print(f"OTP ---->  {otp}")

i= int(input("Enter Otp did you received::"))
if otp==i :
    print("VALID OTP")
else:
    print("INVALID OTP")



