import random

user_wins=0
computer_wins=0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Enter Rock/ Paper/ Scissor or Q to Quit : ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    #rock= 0, paper=1, scissor=2
    computer_pick =options[random_number]
    print("Computer Picked",computer_pick)

    if user_input == computer_pick:
        print("Happened Tie.")
    elif user_input =="rock" and computer_pick =="scissor" or user_input =="paper" and computer_pick =="rock" or user_input =="scissors" and computer_pick =="paper" :
        print("You Win.")
        user_wins+=1
    else:
        print("You Lose.")
        computer_wins+=1

print("Your Win:",user_wins,"times.")
print("You Lose:",computer_wins,"times.")

print("Thanks For Playing.")