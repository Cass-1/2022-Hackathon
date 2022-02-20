def library(followers):
    print("Your journey to the Hackathon is nearing its end.")
    print("As you turn the corner to the cub, you see something.")
    print("You could have sworn you saw something move in the library.")
    print("You continue your walk to the CUB, but you see it again.")
    print("The hackathon is so close, but you feel something drawing you into the library.")
    print("Would you like to investigate? [y/n]")
    Lchoice1 = input()
    if Lchoice1 == 'y' or Lchoice1 == 'Y':
        print("As you draw closer, you feel a chill run down your spine.")
        print("The wind on your back gives you a push, or maybe something is pulling you in.")
        print("You step inside of the library.")
        print("It's dark inside, with one illuminated room on your right.")
        print("It's the study area.")
        print("As your eyes adjust, you begin to make out the other rooms.")
        print("You see the information desk and the book collection area.")
        print("Where would you like to go?")
        followers = LchoiceTwo(followers)
        
    elif Lchoice1 == 'n' or Lchoice1 == 'N':
        print("Maybe next time.")
        print("A chill runs down your spine, you have upset Andy.")    

    else:
        print("I'll take that as a yes!")
        print("As you draw closer, you feel a chill run down your spine.")
        print("The wind on your back gives you a push, or maybe something is pulling you in.")
        print("You step inside of the library.")
        print("It's dark inside, with one illuminated room on your right.")
        print("It's the study area.")
        print("As your eyes adjust, you begin to make out the other rooms.")
        print("You see the information desk and the book collection area.")
        print("Where would you like to go?")
        followers = LchoiceTwo(followers)
        
    return followers
        
def LchoiceTwo(followers):
    print("1. The information desk.")
    print("2. The book collection area.")
    print("3. The study area.")
    print("Please enter either 1, 2, or 3.")
    
    Lchoice2 = input()
    
    if Lchoice2 == '1':
        print("Ah yes, the information desk!")
        print("Surely someone will know what or who was moving around in here")
        print("If only that someone was here.")
        print("You see a bell and give it a tap, it rings loudly.")
        ring_bell()
        print("You return to the lobby. Where would you like to go from here?")
        LchoiceTwo(followers)
        
    elif Lchoice2 == '2':
        print("It's locked, these things are more expensive than gold.")
        print("You think they would just keep it open?")
        print("You return to the lobby. Where would you like to go from here?")
        LchoiceTwo(followers)
        
    elif Lchoice2 == '3':
        print("As you cautiously take your steps towards the lit room")
        print("You wonder to yourself if this is a good idea.")
        print("Afterall, you are gonna be late to the Hackathon.")
        print("Brushing the thought of responsiblity out of your head, you open the door.")
        print("You see in the dark and mysterious corner noneother than butch.")
        print("As you draw near, you can see he is in desperate need of help.")
        print("Poor butch is trying to solve a coding problem.")
        print("Do you decide to help? [y/n]")
        
        answer = input()
        
        if answer == 'y' or answer == 'Y':
            print("You look down at Butch's laptop and see he is trying his hardest")
            print("to print the words 'Go Cougs!' on his screen.")
            print("without the single quotes around the words.")
            print("You crack your fingers and get ready to code.")
            print("Please write a print statement in python below")
            print("printing the words 'Go Cougs!' without the single quotes")
            coding_problem()
            print("Butch jumps for joy!")
            print("Butch thanks you with all his heart!")
            print("You feel a great sense of accomplishment for having helped a friend in need")
            print("You exit the library and continue on your journey to the CUB.")
            followers += 1
            return followers
        
        elif answer == 'n' or answer == 'N':
            print("Even though it was well within your scope of knowledge")
            print("you decided to leave Butch scratching his head.")
            print("You feel a chill run down your spine. You have upset Andy.")
            print("Cougs do not abandon Cougs that are in need of help.")
            print("You exit the library and continue on your journey to the CUB.")
            return followers
            
        else:
            print("You say something butch doesn't understand")
            print("Confused and ashamed, you exit the library.")
            print("You continue on your journey to the CUB.")
            return followers

    else:
        print("You seem to be too confused to make a decision. You have exited the library.")
        return followers
        
def coding_problem():
    answer = input()
    if answer == 'print("Go Cougs!")' or answer == "print('Go Cougs!')":
        print("The code runs successfully!")
    else:
        print("Please try again!")
        coding_problem()

        
def ring_bell():
    print("Surely someone must have heard you hit the bell.")
    print("ring bell again? [y/n]")
    bell = input()
    if bell == 'y' or bell == 'Y':
        ring_bell()
    elif bell == 'n' or bell == 'N':
        print("After hitting the bell for what seems like an uncomfortable amount of time")
        print("you decide it is time to give up. Afterall, it is around 8am on a Saturday.")
    else:
        print("on second thought, you probably shouldn't.")


def spark_building(followers):
    print('You pass by the spark and hear a holler coming from inside.')
    print("Help me! Help me!")
    answer = input('Do you investigate? ["Y" or "N"]: ')
    if answer == 'Y' or answer == 'y':
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
                print()
                if intervention == 'Y' or intervention == 'y':
                    print('You walk up to the Hash Slinging Slasher and trip him causing him to face plant on the floor.')
                    print('You ask the student if she is okay. She responds, "Yes, Thank you!"')
                    print('You look back at the Hash Slinging Slasher only to find the room empty. Was is it all in our heads?')
                    print('Confident that you found the source of the holler, you both leave the Spark unsure of what you just saw.')
                    followers += 1
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
    elif answer == 'N' or answer == 'n':
        print('You choose to ignore the idea of responsiblity.')
    else:
        print('Unable to make a valid choice, you continue with your journey.')
    return followers


def morning():
    print("1. Snooze")
    print("2. Cry")
    print("3. Don clothes")
    print("Enter 1, 2, or 3")
    choice = input()
    if choice == "1":
        print("You were a lot more tired than you initally thought.")
        print("It is now 1:00pm and you have missed the registration window.")
        print("Congrats. Game over.")

    elif choice == "2":
        print("It was quick and felt kinda good to let it out.")
        print("However, crying isn't gonna get you to the hackathon on time.")
        morning()

    elif choice == "3":
        print("You are looking your Sunday best.. on a Saturday, that is.")
        print("Are you ready to go?")
        choice = input("y/n\n")
        if choice == "Y" or choice == "y":
            print("Here we go!")
            
        elif choice == "N" or choice == "n":
            print("You realize you have a minute to spare before you need to head out")
            print("However, your time is rather limited.")
            print("What will you do with your precious spare minute?")
            print("1. Equip smile.")
            print("2. Look in the mirror and give yourself the finger guns.")
            print("3. Pray to the Altar of Andy.")
            print("Enter option number below.")
            choice = input(">>> ")
            
            if choice == "1":
                print("Lookin good! You are ready to conquer the day!")
                print("Time to go!")
                            
            elif choice == "2":
                print("A classy move. You feel like you could conquer the world!")
                print("Time to go!")  
                             
            elif choice == "3":
                print("You feel a strange power wash over you.")
                print("It's time to rock and roll!")
                
            else:
                print("okay then! Here we go!")
               
        else:
            print("I'll take that as a yes.")
          
    else:
        print("Looks like someone doesn't want to follow the rules, I guess we're going pantsless!")



def cub(followers):
    choice = input("You made it to the entrance of the CUB. Do you wish to enter [y/n]? ")
    if choice == 'y':
        print("You enter the CUB. You find yourself in the lobby.")
        choice = int(input("Choose one:\n\
            1. Go upstairs into the CUB Senior Ballroom.\n\
            2. Go downstairs.\n"))

        if choice == 1:
            print("You made it to the 2022 Hackathon! Rejoice!")
            print("Grab a T-Shirt and look for your team.\n")

            if followers == 0:
                print("You didn't help any cougs along the way, so you have no one on your team.")
                print("You struggle to compete by yourself. Thus performing poorly. Your weekend is full of sorrow... :'(")
            elif followers ==1:
                print("You helped one coug. You join up to form a team of two members for the Hackathon.")
                print("By working together your team does ok during the competition.")
            elif followers == 2:
                print("You helped two cougs! You join up to form a team of three members for the Hackathon.")
                print("By working together your team does good during the competition.")
            elif followers == 3:
                print("You helped three cougs!! You join up to form a team of four members for the Hackathon.")
                print("By working together your team does great during the competition.\nIn fact, your team wins the competition because cougs help cougs! :)")

        else:  
            print("Wrong choice...\n\nYou don't make it to the Hackathon in time and cursed to wander the labrinth of the underbelly of the CUB.\
                You don't earn extra credit and forced to live with your mistakes.\n\nAndy is saddened.")


    elif choice == 'n':
        print("You do not enter the CUB and since you're late you do not participate in the 2022 Hackathon.\nYou return home sad.")

    else:
        print("You stand there confused")
        print("Unable to listen to the inner monologue of your mind.")
        print("You chose to not make a decision, or have made a wrong one.")
        print("You cry on the ground.")
        print("Game over.")

        

def main():
    morning()
    followers = 0
    followers = spark_building(followers)
    print()
    followers = library(followers)
    print()
    cub(followers)
main()
