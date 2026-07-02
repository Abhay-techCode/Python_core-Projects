import random
import math

def register():
    name = input("Create User ID : ")
    password = input("Genereate One strong PASSWORD : ")
    otp = random.randint(1000,9999)
    print(f"We Send You OTP {otp}")
    votp = int(input("Enter OTP : "))
    #OTP VERIFICATION
    if otp == votp:
        print("REGISTER SUCCESSFULLY !")
        login(name,password)

    else:
        print("OTP MISMATCH\nPLEASE TRY AGAIN........")
        register()


def Data_entry():

    num=int(input("Enter Number of Student : "))
    
    print("....................................................................\n")
    i=0
    
    f = open("record.txt","a")
   
    while i<num:
        name = input("Enter student Name : ")
        age = int(input("Enter Your Age : "))
        mark = int(input("Enter Total Marks : "))
        sec = input("Enter Section Of Student : ")
        per = (mark/600)*100
        

        f.write(f"\nName : {name}\nAge : {str(age)}\nmark : {str(mark)}\nPercentage : {str(per)}\nSection : {sec}")
        f.write("\n--------------------------------------------------------------")

        print("----------------------------------------------------------------")
        i+=1


    f.close()
    

def display():

    f=open("record.txt","r")
    print("....................................................................\n")
    print("...................STUDENT DATA...................")
    data = f.read()
    print(data)
    f.close()
    

def thank():
    print("\n................THANK YOU !.......................................")
    print("For Visiting...............")
    

def login(user_name,password):
    print("\n...................................................................\n")
    print("....................LOGIN REDIRECTED.......................")
    print(f"Hey {user_name}\nYou are Logged Successfully.....")
    
    while True:
        opt = int(input("Select:\n1.Data Entry\n2.Display Data\n3.EXIT"))
        if opt ==1:
            Data_entry()
        elif opt==2:
            display()
        else:
            thank()
            break

    

   
print("...............................................................")
print("Welcome To,\nStudent Management Portal \n")
print("...............................................................")
print("..................REGISTRATION PORTAL..........................")
register() 


"""
    THIS IS A STUDENT RECORD MANAGER WHERE TWO MODULES ARE IMPORTANT -
        1.USER {TEACHER} REGISTRATION AND LOGIN DEMONSTRATION
        2.STUDENT DATA FETCH AND STORE IN FILE AND RETRIEVE AND DISPLAY
        
    BY USING FILE HANDLING JUST READ AND WRITE I APPLY HERE, TO INSERT AND RETRIVE DATA
    APPLY VARIOUS PROGRAMMING LOGIV LIKE WHILE , IF - ELSE FUNCTIONS AND RECURSIVE CALLS
    AND CREATE ONE DUMMY BUT PRACTICAL STUDENT RECORDER.........
    
"""