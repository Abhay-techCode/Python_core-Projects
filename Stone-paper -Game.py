import random

user = input("Select Stone paper seasor : ")
user.lower()
li=['stone','paper','seasor']
comp = random.choice(li)

if (user=='stone' and comp=='paper') or (user=='paper' and comp=='seasor') or (user=='seasor' and comp=='stone'):
    print(f"Sorry ! Computer Maharaj [{comp}] Win.....")
elif(user==comp):
    print("Match Tie........")
else:
    print("Congratulations ! You win.....")
