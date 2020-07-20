import sys

print("Welcome, Warrior !!!!\nYou have entered the Dragon's Treasure Dungeon !!!\n")
print("You are in the Main Hall.\n")
print("This place was once the Hall of the Great Heroes.\n")
print("Now all are DEAD !!!!\n")
print("To the left is the Sword room.\n")
print("To the right is the castle reading room, with back entrance.\n")
print("To the front lies the Treasure room.\n")
print("Choose your rooms wisely.\n")

def mainhall():
    roomdir=input("Enter the way you want to go : Left, Right, or Front\n")

    if (roomdir=="left")or(roomdir=="Left"):
        left()
    elif (roomdir=='right')or(roomdir=="Right"):
        right()
    elif (roomdir=='front')or(roomdir=="Front"):
        front()
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        sys.exit(1)
