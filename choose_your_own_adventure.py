name = input("Type your Name : ")
print("Welcome",name,"to the Adventure.")

answer=input("You are on a dirt road. It has come to the end. Choose the next move. Left or Right").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk or swim across the river.").lower()
    if answer =="swim":
        print("You have swam across the river and eaten by the aligator.")
    if answer =="walk":
        print("You walked across for miles and ran out of water, and you lose.")
    else:
        print("You walked into the river. You Drown.")


if answer == "right":
    answer = input("You have come to a bridge, you want to cross or back ? ").lower()
    if answer == "cross":
        print("You have crossed the bridge and come to the destination.")
        print("You have Completed. You Won.")
    if answer == "back":
        print("You have walked back to the road.")

else:
    print("Not a option.You have lost.")