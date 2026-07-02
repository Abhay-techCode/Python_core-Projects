import random
print("\n................................................................................")
print("|Random Digit Finder|\nrules:\n1.Enter 4 Digit Number\n2.You have only 3 Chances\n")
print("..................................................................................")
def find(num,user):
    if num == user:
        print(f"The Number is Correctly guess i.e {num}.......\n........Well done........")
        i=3
    elif user<num:
        print("Your guess is less than Number............")
    else:
        print("Your guess Is Greater Than number.........")

num=random.randint(1000,9999)
i=0
digit=1
# print(num)  -------for self understanding
while(digit==1):
   if i>2:
       print("\nFailed sorry,\n All 3 Pass are Over Try Next Time............")
       break
   else:
        user=int(input("Guess The Four digit Number : "))
        find(num,user)
        i+=1
    

"""
    IN THE RANDOM DIGIT FINDER GAME--------
        I UNDERSTAND THE FUNCTION USE CASES WHERE THE RANDOM NUMBER GENERATE WITH 
        RANDOM MODULE AND USER GUESS WHERE CONDITIONS OF ELSE-IF ARE APPLIED IN find()
        FUCTION AND 3 PASSES ALLOWED-------
        
"""