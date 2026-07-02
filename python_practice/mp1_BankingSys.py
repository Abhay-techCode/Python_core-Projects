#Welcome to banking system - my personalized online banking transaction
import random
#imported random -package for OTP generation

print("WELCOME TO ONLINE PORTAL OF -- PATIL FUNDS")

cus_name=input("Enter Your name [first_name Last_name] :")

cus_pw=input("Enter Your Password:")

print("We are Kindly provide You Otp on Register mobile no please Enter-----\n\n")
i=5
otp=random.randint(1000,9999)
print(otp)
votp=int(input("Enter OTP:"))

print("***************************************************************************************")
if(otp==votp):
    amt=2000
    print("OTP you enterd is Valid \nLogin Successfully\n\n")
    print(f"hello {cus_name} ,")
    print("\n\tSelect The menu:\n\t1.Balance ENQ\n\t2.Deposite\n\t3.Credit\n\t4.Exit")
    print("**************************************************************************")
    i=int(input())
    while(i>0):
       print("\n\tSelect The menu:\n1.Balance ENQ\n2.Deposite\n3.Credit\n4.Exit")
       print("***********************************************************************")
       i=int(input())
    #initially bank balance is fixed i.e rs 2000/-
       if(i==1):
          print('Bank Balance is ::')
          print(f"Bank balance is rupees {amt}")
       elif(i==2):
           val=int(input("Enter a Amount Deposite :- "))
           amt+=val
           print("Amount deposite Successfully")
       elif(i==3):
           val=int(input("Enter amount want to withdraw:-"))
           amt-=val
           print("Amount deducted successfully")
       else:
           print("Thank You ----------------\nyou are Logged out successfully---------")
           i=0

        
else:
    print("Invalid Otp \nLogin Failed")
    print(f"{cus_name} please try again later")



"""THIS BANK SYSTEM IS BASICALLY HAVING OPTION BASED AND DUMMY SYS WHAERE ON IF-ELIF CONDITIONS 
EXECUTED AND ACCORDINGLY PROGRAM IS FLOWED BANK INITIAL ACC BALANCE IS RS 2000 IS FIXED IN THIS
I USED THE PRACTICAL LEARNING IMPLEMENTATION OF =
    DATATYPES
    STRING
    LOOP FOR
    COMPARISION OPRERATORS
    ARITHMETIC OPERATIONS
    RANDOM (OTP GENERATION)---IMPORTING RANDOM PACKAGE

THIS WAY I DEVELOPED AN SYSTEM BASED ON PRIOR KNOWLEDGE OF BANK ONLINE SYSTEM
    """


