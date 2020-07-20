import sys

print("Welcome, Warrior !!!!\nYou have entered the Dragon's Treasure Dungeon !!!\n")
print("You are in the Main Hall.\n")
print("This place was once the Hall of the Great Heroes.\n")
print("Now all are DEAD !!!!\n")
print("To the left is the Sword room.\n")
print("To the right is the castle reading room, with back entrance.\n")
print("To the front lies the Treasure room.\n")
print("Choose your rooms wisely.\nBecause you can not go back now !!\n")


def mainhall():
    roomdir=input("Enter the way you want to go : Left, Right, or Front:\n")

    if ((roomdir=="left")or(roomdir=="Left")):
        left()
    elif ((roomdir=='right')or(roomdir=="Right")):
        right()
    elif ((roomdir=='front')or(roomdir=="Front")):
        front()
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)


def left():
    print("Sword found in this room.\n")
    swordpick = input(int("Press '0' to pickup Enchanted Sword\n"))

    if (swordpick == 0) :
        print("You are back to main Hall with Enchanted Sword.\n")
        mainhall()
    else:
        print("There was nothing else in the Sword room.\n")
        print("You are back in main Hall.\n")
        mainhall()


def right():
    print("You are in the Reading room.\n")
    print("To your left is the Book shelf.\n")
    print("To your right is the Secret Exit.\n")
    print("To your front lies the Fireplace.\n")
    right_roomdir=input("Enter the way you want to go : Left, Right, or Front:\n")

    if ((right_roomdir=="left")or(right_roomdir=="Left")):
        bookshelf()    #finished
    elif ((right_roomdir=="right")or(right_roomdir=="Right")):
        print("You exit through the Dungeon.\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(0)
    elif ((right_roomdir=="front")or(right_roomdir=="Front")):
        print("The Fireplace was the entrance to HELL.\n")
        hell()   #finished
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)

def front():
    print("You have entered the Treasure room.\n")
    print("Infront of you lies an old Golden Box.\n")
    toward_box=input("To go towards the box, Type 'Go front':\n")

    if ((toward_box=="go front")or(toward_box=="Go front")):
        print("OH No, You stepped on a TRAP, and it transports you somewhere !!!!\n")
        hell()   #finished
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)


def bookshelf():   #make sure to put this at the top
    print("You are at the book shelf.\n")
    print("And, you see some books on the shelf.\n")
    print("There is also a note that says:\n")
    print("** DO NOT READ THESE BOOKS, THESE WILL BE THE DEATH OF YOU **\n")
    read_books=input("To read the books, Type 'Read books'.\nTo go back, Type 'Back off' :\n")

    if ((read_books=="Read books")or(read_books=="read books")):
        print("You were warned !!!!!\n")
        print("You are DEAD\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)
    elif ((read_books=="back off")or(read_books=="Back off")):
        print("You go back to the Entrance of the Reading Room.\n")
        right()
    else:
        print("You Touched something CuRsEd !!!!\n")
        print("You are DEAD\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)


def  hell(): #make sure to put this at the top
    print("You have reached HELL !!!!\n")
    print("Infront of you, stands a DRAGON \n")
    print("KILL HIM, to pass through this hurdle.\n")

    attack=int(input("Enter enough attack power to kill the beast (attack power > 10) :\n"))

    if (attack < 10):
        print("Attack power was TOO LOW....\n")
        print("The DRAGON kills YOU.\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)
    elif(10 <= attack <= 500):
        print("You do your signature MAGMA ICE MAGIC SLASH !!!!\n")
        print("This kills the dragon, and you are awarded the title 'THE DRAGON SLAYER KNIGHT'.\n")
        print("You see Two Portals open....\nThe portals show the destination, you want to go to.\n")
        go_back=input("To go to the Treasure Room, Type 'Treasure room'\nTo go to the Reading Room, Type 'Reading room':\n")
        if ((go_back=="Treasure room")or(go_back=="treasure room")):
            treasure_room()  #write this later
        elif ((go_back=="Reading Room")or(go_back=="reading room")):
            right()
        else:
            print("You got lost in the Portals !!!!\n")
            print("You are DEAD NOW\n")
            print("\t\t\t\t\t***GAME OVER***")
            sys.exit(1)
    else:
        print("WoW, You did your most powerful move 'TIME LIFE BREAKER' !!!!\n")
        print("This kills the DRAGON, but you also lost all your health by using this move....\n")
        print("With your dying breath, you are awarded the title 'DRAGON LIFE DESTROYER' \n")
        print("You are DEAD.\nWell Played.\nTRY AGAIN LATER\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)
