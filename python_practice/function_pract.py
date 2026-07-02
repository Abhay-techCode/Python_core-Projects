"""
def greet(name="abhay"):
    print("Hey hello ",name)


user = input("Enter Your Name : ")

greet(user)

greet()         #function having default Argument abhay



#Factorial code by Recursion

tot=1
def fact(num):
    if(num==0 or num==1):
        return 1
    else:
        tot=num*fact(num-1)
        return tot
    
num = int(input("Enter a Number : "))


print(f"Tha Factorial of {num} is = {fact(num)}")



def great(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
a=int(input("Enter first Numbers : "))
b=int(input("Enter Second Number : "))

c=int(input("enter Third Number : "))

print(f"The Greatest Number from {a,b,c} is =",great(a,b,c))

"""
total=0

def sum(num):
    if num==1 or num ==0:
        return num
    
    else:
        total=num+sum(num-1)
        return total

num=int(input("Enter a NUMBER : "))

print(f"The sum of First {num} is = {sum(num)}")