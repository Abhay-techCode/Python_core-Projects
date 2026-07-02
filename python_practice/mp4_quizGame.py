#This is a Quiz based Game Where Question generated randomly 3 and answers verify 

import random
quiz={"what is ram":"memory",
      "what is i7":"processor",
      "what is python":"language",
      "who is CEO of Google":"sundar pichai",
      "what is vscode":"ide",
      "who is founder of this game":"abhay patil"
      }
pt=0
def check(cor,ans):
    if(cor == ans):
        print("Correct Answer ! ")
        return 1
      
    else:
        print("Incorrect Answer ! ")
        return 0
    

def result(points):
    if points>=2:
        print(f"Score is {points} GOOD SCORE KEEP IT UP!")
    elif points<2 and points>0:
        print(f"Score is {points} NICE NEED TO IMPROVE!")
    else:
        print(f"Score is {points} VERY BAD TRY HARD!")

que=list(quiz.keys())

print("\n........................QUIZ BUSTER ...............................")
print("\nWELCOME,\nTo quiz buster Here 3 Question arise you need to answer it!")
name = input("Enter Your Name : ")

print(f"\nHey , {name}..........play Game")



i=1
while(i<=3):
    random.shuffle(que)
    new=random.choice(que)
    print(f"{i}.{new}")
    ans=input("Enter The Answer : ")
    pt+= check(quiz[new],ans.lower())
    print("\n..........................................................................")
    i+=1

print("\n..............................GAME ENDED..................................")

res=int(input("Enter-\n1.SEE RESULT\n2.EXIT\n"))

if(res==1):
    print("..................................RESULT....................................")
    print(f"NAME :{name}")
    result(pt)
    print("------------------------THANK YOU------------------------")
else:
    print("------------------------THANK YOU------------------------")


    """
    THIS IS A QUIZ GAME WHERE I DECLARED FUNCTIONS FOR 
            -FIRST CHECKING THE RESULT
            -SECOND FOR RESULT CALCULATIONS
    IN THIS DICTIONARY,LIST,IF-ELSE,WHILE LOGICS ETC. USED
    AFTER THAT YOU GET AN RESULT OPTION WHERE FEEDBACK IS 
    GIVEN
    ACCORDING TO THE POINTS GOT SCORED........
    
    
    """
