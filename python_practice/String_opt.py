'''  
str="Abhay"
str1="Patil"
str2=str1+" "+str
print(str2)

name="twinkle"

print(name.capitalize())

print(name.upper())

print(name.lower())

sen="hey varad how are you
i am your friend abhay"
print(sen.title())


name="Abhay Chandrakant Patil"

a=len(name)
print(a)


print(name[::-1])           #printing any strin g in reverse

print(name.endswith("il"))

print(name.startswith("A"))

a=name.count("il")
print(a)

a=name.find("C")
print(a)


na=name.split()
print(na)

str="my name is abhay"

str1=str.replace(" ","--")  #replace operation

print(str1)

print(str.replace(" ",""))


#String is Palindrome or Not

txt=input("ENTER A STRING::")

txt1=txt.lower()

if(txt1==txt1[::-1]):
    print(f"The {txt} is palindrome")
else:
    print("Strings are not plindrome")

'''
"""
#new somethings try and error basis

name="abhay is a good boy"
str=name.split()
print(str)
print(" ".join(reversed(str)))

"""

str="abhay"
str1="Abhay"
a=(str1==str)
print(a)