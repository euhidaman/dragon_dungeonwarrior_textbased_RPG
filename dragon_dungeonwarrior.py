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
        bookshelf()    #write it later
    elif ((right_roomdir=="right")or(right_roomdir=="Right")):
        print("You exit through the Dungeon.\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(0)
    elif ((right_roomdir=="front")or(right_roomdir=="Front")):
        print("The Fireplace was the entrance to HELL.\n")
        hell()   #write this later
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)

def front():
    print("You have entered the Treasure room.\n")
    print("Infront of you lies an old Golden Box.\n")
    toward_box=input("To go towards the box, Type 'Go front':\n")

    if ((toward_box=="go front")or(toward_box=="Go front")):
        trap()   #write this later
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)


def bookshelf():
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
