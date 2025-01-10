# A very simple maze game in Python

# Can you find an example of iteration (a loop)?
#
# Can you draw a map of the rooms?
#
# Can you connect room 4 to the system?
# 
# Can you add another room?
#
# To add a room you will need to add a room description in the first sub-process
# You will then need to add a way to get to the room within the if command statements
#
# Can you add something like picking up gold coins to the functionality?
# You would need to create a variable for the purse and add to it when the first sub-process runs.
#

def print_room_description(room):
    if room == 1:
        print("You are in a dark room. There is a door to the north.")
    elif room == 2:
        print("You are in a bright room. There is a door to the south and a door to the east.")
    elif room == 3:
        print("You are in a library. There is a door to the west.")
    elif room == 4:
        print("You are in a treasure room. Congratulations, you found the treasure!")

def main():
    current_room = 1

    while True:
        print_room_description(current_room)
        command = input("Enter a command (north, south, east, west, quit): ").strip().lower()

        if command == "north":
            if current_room == 1:
                current_room = 2
            else:
                print("You can't go that way.")
        elif command == "south":
            if current_room == 2:
                current_room = 1
            else:
                print("You can't go that way.")
        elif command == "east":
            if current_room == 2:
                current_room = 3
            else:
                print("You can't go that way.")
        elif command == "west":
            if current_room == 3:
                current_room = 2
            else:
                print("You can't go that way.")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")

        if current_room == 4:
            print_room_description(current_room)
            break

if __name__ == "__main__":
    main()