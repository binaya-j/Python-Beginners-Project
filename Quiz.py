print("Welcome to the Quiz :)")
choice=input("Do You Want to Continue : ")
if choice.lower() =="yes":
    print("Lets Start :)")
else:
    quit()

score=0

answer=input("1. What does GPU stands for ? ")
if answer.lower() =="graphics processing unit":
    print("Correct ")
    score+=1
else:
    print("Incorrect")

answer=input("2. When was WW1 started ? ")
if answer.lower() =="1914":
    print("Correct ")
    score+=1
else:
    print("Incorrect")

answer=input("3. Where is Statue of Jesus located ? ")
if answer.lower() =="brazil":
    print("Correct ")
    score+=1
else:
    print("Incorrect")

answer=input("4. Which movie universe has iron man ? ")
if answer.lower() =="marvel":
    print("Correct ")
    score+=1
else:
    print("Incorrect")

print("YOu have completed the quiz. Thankyou.")
print("Your Score is: "+str(score))