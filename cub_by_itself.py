def cub(followers):
    '''
    This function has the user complete their journey to the CUB. There is a bonus coug in need of help if the player doesn't find all the 
    cougs in need of help along the way
    '''

    choice = input("\nYou made it to the entrance of the CUB. Do you wish to enter [y/n]? ")
    if choice == 'y':

        print("\nYou enter the CUB. You find yourself in the lobby.\n")

        while True:
            choice = int(input("Choose one:\n\
            1. Go upstairs into the CUB Senior Ballroom.\n\
            2. Go downstairs.\n"))
    #user goes upstairs
            if choice == 1:
                print("You made it to the 2022 Hackathon! Rejoice!\n\
Grab a T-Shirt and look the cougs you helped along the way to form your kickass team.\n\n")


                if followers == 0:
                    print("You didn't help any cougs along the way because you were in a rush, so you have no one on your team.\n\
You struggle to compete by yourself. Thus performing poorly. Your weekend is full of sorrow... :'(\n\n")
                    break

                if followers == 1:
                    print("You helped one coug. You join up to form a team of two members for the Hackathon.\n\
By working together your team does ok during the competition, and is able to submit a suitable program.\n\n")
                    break

                if followers == 2:
                    print("You helped two cougs! You join up to form a team of three members for the Hackathon.\n\
By working together your team does good during the competition, and by having three members the workload is doable.\
Your team has fun together and makes the coding experience better. You turn in a good program.\n\n")
                    break

                if followers == 3:
                    print("You helped three cougs while you were on your way to the Hackathon!! They are gratituous to you and want to join your team.\
You agree to join up to form a team of four members for the Hackathon.\n\
By working together your team does great during the competition.\nIn fact, your team wins the competition because cougs help cougs! :)\n\n")
                    break

                if followers == 4:
                    print("You helped four cougs on your way to the Hackathon!! By showing school spirit you appease the Coding Gods and are blessed with good luck.\
You now have to decide which coug is left to fend for themself and which three you'll work with.\
You join up to form a team of four members for the Hackathon, but saddened in the face of your loss. However, your team overcomes this grief.\n\
By working together your team does great during the competition.\nIn fact, your team wins the competition because cougs help cougs! :)\n\n")
                    break


    #user goes downstairs
            else:
                choice = 0
                while choice != 4:  
                    choice = int(input("When you reach the basement lobby you see there are three rooms. One to your left with the lights off and the door open. \
One is to your right and the light is off and the door closed. Further down the hallway you can see that the light is on in a room.\n\nChoose one:\n\
                    1. Go to the left.\n\
                    2. Go to the right.\n\
                    3. Travel further down the hallway.\n\
                    4. Go back upstairs to be on time to the Hackathon.\n\n"))
    #if user decides to go to the left (lights off and door open)
                    if choice == 1:
                        print("This room is cold and dark. You flip the light switch but the light doesn't turn on. \
You start to get creepy vibes and decide to return to the lobby.\n\n")

    #if user decides to go to the right (lights off and door closed)
                    if choice == 2:
                        print("You try the door handle and find it is locked. A shiver goes down your spine and you return to the lobby.\n\n")

    #if user decides to go down the hallway
                    if choice == 3:
                        print("You notice that a coug is in the room looking lost, so you knock. Being curious you ask what they are doing.\
They respond with that they got lost and were looking for the Hackathon. You tell them that's where you're going \
and you can show them the way. They follow you up.\n\n")
                        followers += 1

                    if choice == 4:
                        print("You go back upstairs.\n\n")
                


#if user chooses not to enter the CUB
    elif choice == 'n':
        print("\nYou do not enter the CUB and since you're late you do not participate in the 2022 Hackathon.\nYou return home sad.\n\n")
#if user inputs incorrect input
    else:
        print("\nInvalid choice. Try again.\n")

    return followers
