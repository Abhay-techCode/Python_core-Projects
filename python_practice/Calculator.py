#calculator program Where we take input as a 2num and display result

#in python indentation plays an crucial role 

a=int(input("Enter a First Number:"))
b=int(input("Enter a Second Number:"))

print("Select Operation:-\n1.addition\n2.Substraction\n3.Multiplication\n4.Division")
user_resp=int(input())
if(user_resp==1):
    print(f"The Addition of Two Num={a+b}")
elif(user_resp==2):
    print(f"The Substration of Two Num={a-b}")
elif(user_resp==3):
    print(f"The Multiplication of Two Num={a*b}")
elif(user_resp==4):
    print(f"The Division of Two Num={a/b}")
else:
    print("wrong Option selection *******")





