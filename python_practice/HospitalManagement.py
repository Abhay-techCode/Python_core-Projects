doc={}  #Doctor Dict initialization

pat ={} #Patient Dict initialization

def registration():
  
    id= int(input("Enter Doctor ID : "))
    doc[id]={
        "name" : input("Enter Doctor Name : "),
        "field":input("Enter Specification : "),
        "mobile": int(input("Enter Mobile Number : "))
    }

    print("\nRecord Inserted Successfully ! ")
    home()

def D_data():
    ids=int(input("Enter Doctor ID : "))
    for id,details in doc.items():
            if ids== id:
                print("\n******************************************************")
                print("Record Founded............")
                print("\n-----------------Doctor Detailes-----------------------")
                print("\nDoctor ID : ",id)
                print("Doctor name : ",details["name"])
                print("Doctor Mobile Number : ",details["mobile"])
                print("Specification : ",details["field"])
                
                print("\n------------------Thanks-----------------------")
                break
            else:
                print("\nSorry ! No Record Found")

    home()

def p_registration():
    
    mobile = int(input("Enter Mobile Number : "))
    pat[mobile]={
        "name": input("Enter Patient Full Name : "),
        "diagnosis":input("Enter Diagnosis : "),
        "doctor": input("Enter Refrence Name : "),
        "Bill" : int(input("Enter Total Bill Amount : "))
    }
    
    print("...........Data Inserted Successfully..............")
    print("\nThank You.....")
    home()

def search():
    mobile = int(input("Enter Patient Mobile Number : "))
    for mob,details in pat.items():
        if mob== mobile:
            print("\n******************************************************")
            print("Record Founded............")
            print("\n------------------Receipt-----------------------")
            print("\nPatient name : ",details["name"])
            print("Patient Mobile Number : ",mobile)
            print("Patient Diagnosis : ",details["diagnosis"])
            print("Refrence Doctor : ",details["doctor"])
            print("Total Pay Amount : ",details["Bill"])
            print("\n------------------Thanks-----------------------")
            break
        else:
            print("\nSorry ! No Record Found")
            

    home()

def doctor():
    c = int(input("Enter:-\n1.Registration\n2.View Data\n"))
    if c == 1:
        registration()
    elif c== 2:
        D_data()
    else:
        print("........No Correct Responce Selected.........")
        home()

def patient():
    c = int(input("Enter:-\n1.Registration\n2.Search\n3.Home\n"))

    if c == 1:
        p_registration()
    elif c==2:
        search()
    else:
        home()

def home():
    print("\nWelcome,\nTo HOSPITALITY SERVICE CORNER")
    print("-------------------------------------------------------")
    choice = int(input("\nSelect:-\n1.Doctor's Section\n2.Patient's Section\n3.Exit\n"))
    print("\n----------------------------------------------------------")
    if choice == 1:
        doctor()
    elif choice == 2:
        patient()
    else:
        print("..............THANK YOU..................")

home()


"""HOSPITAL MANAGEMENT SYSTEM
      THIS SYSTEM BUILDS FOR - RECEPTIONIST WHO ARE RESPONSIBLE FOR ADMINISTRATIVE WORKS
       Here, system consist of Two Module----
            1.Doctors Section
            2.Patient Section
        1.Doctor section
          here Doctor regitration and data insert into dictionary name as doc{}
          doctor records find etc.
        2.Patient section
          here patient registration be done patient search through mobile no as
          a key for pat dict 
        By, This way One of the Most Useful and Real World applicable system builds
        with Python Core logic.
        THANK YOU !
"""