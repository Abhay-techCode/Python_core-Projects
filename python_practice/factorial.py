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