#String is Palindrome or Not

txt=input("ENTER A STRING::")

txt1=txt.lower()

if(txt1==txt1[::-1]):
    print(f"The {txt} is palindrome")
else:
    print("Strings are not plindrome")
