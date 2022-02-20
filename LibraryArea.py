# Bryan Chang
# Hackathon project
# 2/19/22
# spark function

def spark_building(followers, time):
    print('You pass by the spark and hear a holler coming from inside.')
    print("Help me! Help me!")
    answer = input('Do you investigate? ["Y" or "N"]: ')
    if answer == 'Y':
        Room = 0
        while Room != 4:
            print('You enter the spark lobby and do not know where the scream came from.')
            print('You are presented with the following options.')
            print('1. Room G45\n2. Starbucks\n3. Upstairs study area.\n4. Exit')
            Room = int(input('Select room [1,2,3, or 4]: '))
            print(Room)
            if Room == 1:
                print('You enter Room G45 to find a fellow student being chased around by the Hash Slinging Slasher brandishing his spatula.')
                intervention = input('Do you intervene? ["Y" or "N"]: ')
                if intervention == 'Y':
                    print('You walk up to the Hash Slinging Slasher and trip him causing him to face plant on the floor.')
                    print('You ask the student if she is okay. She responds, "Yes, Thank you!"')
                    print('You look back at the Hash Slinging Slasher only to find the room empty. Was is it all in our heads?')
                    print('Confident that you found the source of the holler, you both leave the Spark unsure of what you just saw.')
                    followers += 1
                    time += 10
                    Room = 4
                else:
                    print('Being of the cowardly sort, you leave the room and the Spark building at a brisk pace.')
                    Room = 4
            elif Room == 2:
                print('You go to check out the Starbucks when all of a sudden the lights start flickering.')
                print('You look towards the light switch only to find Nosferatu playing with it.')
                print('You shake your finger at him saying, "Nosferatu!" and he smiles a creepy smile.')
                print('Confident that nothing is happening in the Starbucks, you go back to the lobby.')
            elif Room == 3:
                print('You search the upstairs study area and discover nothing.')
                print("You don't know why, but you were kinda expecting to find something weird.")
                print('You start to back to the lobby, but before you do you take a quick second to enjoy the view from the fourth floor.')
            elif Room == 4:
                print('You decide that you had a enough of this building and leave.')
    return followers, time

def main():
    followers = 1
    time = 0

    followers, time = spark_building(followers, time)
    print(followers, time)

main()
