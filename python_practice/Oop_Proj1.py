class Account:
   
    def __init__(self,bal,acc):
        print("Welcome To Bank Online ...")
        self.balance =bal
        self.account =acc
    def debit(self,amt1):
        if amt1 > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -=amt1
            print(f"{amt} debit successfully...")
    def credit(self):
        amt = int(input("Enter Amount : "))
        self.balance += amt
        print(f"Amount Rs.{amt} added in Your Account successfully...")
    def check_bal(self):
        print(f"Your balance is Rs.{self.balance}")

bal = int(input("Enter Your Balance : "))
acc = input("enter Account Number : ")
a1 = Account(bal,acc)
while True:
    i = int(input("debit - 1\nCredit - 2\nBalance - 3"))
    match(i):
        case 1:
            amt = int(input("Enter amount : "))
            a1.debit(amt)
        case 2:
            a1.credit()
        case 3:
            a1.check_bal()
        case _:
            print("invalid selection...")
            break;

            
