print("Welcome to the game of finding your lost coin.")
print("Your mission is to find the coin.")
direction_1=input("you are in a road with two directions LEFT or RIGHT,"
                  " choose one :)\n").upper()
if direction_1 == "RIGHT":
    print("you fell into a hole and found NOTHING !!!!,game over")
    exit()
elif direction_1 == "LEFT":
    print("you have entered into a shopping mall where you went last time !!!!")

else:
    print("please enter a valid comment :)")
direction_2=input("After you entered the shopping mall,your inner thought strongly"
                  " suggest you to WAIT but its totally up to you to wait or GO,"
                  "choose one :) \n").upper()

if direction_2 == "GO":
    print("you found NOTHING because you did not listen to yourself !!!!!,game over")
    exit()
elif direction_2 == "WAIT":
    print("that is a good choice,now you can continue the game :)")

direction_3 = input("now you see 3 colored DOOR (RED,YELLOW,GREEN)in front of you "
                    "witch one do you choose to go in where"
                    " you might find your coin ???\n").upper()
if direction_3 == "RED":
    print("this door connects directly to a dragon's stomach,"
          "and you also found NOTHING !!!!,Game over")
    exit()
elif direction_3 == "YELLOW":
    print("congrats, you found your COIN !!,you won!!")
elif direction_3 == "GREEN":
    print("you have entered into a room full of snakes, "
          "sorry GREEN snakes because the door is GREEN,"
          " and you found NOTHING,game over")
    exit()


