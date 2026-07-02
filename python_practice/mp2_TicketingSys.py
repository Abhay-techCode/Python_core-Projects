#this is Online Ticketing syatem
import random
print("\nWelcome To, MSRTC online booking Center\n")
print("*"*100)
id=input("\nEnter Your Authorized ID:")
otp=random.randint(1000,9999)

print(otp)
print("\nEnter OTP :")
votp=int(input())

list={1:'jalgaon to Shegaon',2:'jalgaon to Nandura',3:'jalgaon to Akola',4:'jalgaon to Yavatmal'}

if(id=='abhay2005' and votp==otp ):
    print("*****************************************************************************")
    print(f"Welcome user {id}")
    print("******************************************************************************\n")
    fares={1:91,2:51,3:111,4:356}
    i=1
    while(i<4):
        print("\tPlease Select Menu:\n\t1.Jalgaon (ja)---->shegaon\n\t2.jalgaon (ja)---->Nandura\n\t3.jalgaon (ja)---->Akola\n\t4.jalgaon (ja)---->Yavatmal")
        choice=int(input())
        cus_name=input("Enter Customer Name:")
        gender=input("Enter Gender:")
        age=int(input("Enter Your Age :"))
        if(age<18):
            amt=fares.get(choice)/2
            print("\n************************Your Ticket************************")
            print(f"Customer name={cus_name}\nCustomer Age={age}\nCustomer Gender={gender}\nTravel route: {list.get(choice)}\nTotal fare={amt}rs")
            print("----------------------------------Thank You---------------------------------------------")
            i=int(input("Enter\n3.New Ticket\n4.Exit"))
        else:
            amt=fares.get(choice)
            print("\n************************Your Ticket************************")
            print(f"Customer name={cus_name}\nCustomer Age={age}\nCustomer Gender={gender}\nTravel route: {list.get(choice)}\nTotal fare={amt}rs")
            print("----------------------------------Thank You---------------------------------------------")
            i=int(input("Enter\n3.New Ticket\n4.Exit"))
else:
    print("Invalid Credit please Try again Later..............................")

print("Thanks for visiting................................................")



"""IN THIS BUS FARE TICKETING SYSTEM ITS A HARD CODED UID AND AFTER SUCCESSFUL LOGIN 
A MENU BAR GET OPEN HERE I USED A DICTIONERY ------>2 FOR THE STORE F MULTI VALUES DATA
AND AFTER SUCCESSFULLY TICKET GENERATION TICKET RECEIPT GOT GENERATED.............
        TOPIC COVERED---->
        1.DATATYPES
        2.dICTIONARY
        3.iF-ELSE
        4.WHILE LOOP
        5.RANDOM USE CASE FOR OTP VALIDATIONS
        """