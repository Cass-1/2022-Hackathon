import copy
import random as r
def library(followers):
    print("Your journey to the Hackathon is nearing its end.")
    print("As you turn the corner to the CUB, you see something.")
    print("You could have sworn you saw something move in the library.")
    print("You continue your walk to the CUB, but you see it again.")
    print("The Hackathon is so close, but you feel something drawing you into the library.")
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
        print("Surely someone will know what or who was moving around in here.")
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
        print("As you cautiously take your steps towards the lit room.")
        print("You wonder to yourself if this is a good idea.")
        print("Afterall, you are gonna be late to the Hackathon.")
        print("Brushing the thought of responsiblity out of your head, you open the door.")
        print("You see in the dark and mysterious corner none other than Butch.")
        print("As you draw near, you can see he is in desperate need of help.")
        print("Poor Butch is trying to solve a coding problem.")
        print("Do you decide to help? [y/n]")
        
        answer = input()
        
        if answer == 'y' or answer == 'Y':
            print("You look down at Butch's laptop and see he is trying his hardest.")
            print("He's trying to print the words 'Go Cougs!' on his screen")
            print("without the single quotes around the words.")
            print("You crack your fingers and get ready to code.")
            print("Please write a print statement in python below:")
            print("(print the words 'Go Cougs!' without the single quotes)")
            coding_problem()
            print("Butch jumps for joy!")
            print("Butch thanks you with all his heart!")
            print("You feel a great sense of accomplishment for having helped a friend in need.")
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
            print("You say something Butch doesn't understand.")
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
    print("Ring bell again? [y/n]")
    bell = input()
    if bell == 'y' or bell == 'Y':
        ring_bell()
    elif bell == 'n' or bell == 'N':
        print("After hitting the bell for what seems like an uncomfortable amount of time")
        print("you decide it is time to give up. Afterall, it is around 8am on a Saturday.")
    else:
        print("On second thought, you probably shouldn't.")


def spark_building(followers):
    print('You pass by The Spark and hear a holler coming from inside.')
    print("Help me! Help me!")
    answer = input('Do you investigate? ["Y" or "N"]: ')
    if answer == 'Y' or answer == 'y':
        Room = 0
        while Room != 4:
            print('You enter The Spark lobby but do not know where the scream came from.')
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
                    print('You ask the student if she is okay. She responds, "Yes, thank you!"')
                    print('You look back at the Hash Slinging Slasher only to find the room empty. Was is it all in our heads?')
                    print('Confident that you found the source of the holler, you both leave The Spark unsure of what you just saw.')
                    followers += 1
                    Room = 4
                else:
                    print('Being of the cowardly sort, you leave the room and The Spark building at a brisk pace.')
                    Room = 4
            elif Room == 2:
                print('You go to check out the Starbucks when all of a sudden the lights start flickering.')
                print('You look towards the light switch only to find Nosferatu playing with it.')
                print('You shake your finger at him saying, "Nosferatu!" and he smiles a creepy smile.')
                print('Confident that nothing is happening in the Starbucks, you go back to the lobby.')
            elif Room == 3:
                print('You search the upstairs study area and discover nothing.')
                print("You don't know why, but you were kinda expecting to find something weird.")
                print('You start to go back to the lobby, but before you do you take a quick second to enjoy the view from the third floor.')
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
        print("However, crying isn't gonna get you to the Hackathon on time.")
        morning()

    elif choice == "3":
        print("You are looking your Sunday best.. on a Saturday, that is.")
        print("Are you ready to go?")
        choice = input("y/n\n")
        if choice == "Y" or choice == "y":
            print("Here we go!")
            
        elif choice == "N" or choice == "n":
            print("You realize you have a minute to spare before you need to head out.")
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
                print("Okay then! Here we go!")
               
        else:
            print("I'll take that as a yes.")
          
    else:
        print("Looks like someone doesn't want to follow the rules, I guess we're going pantsless!")



def cub(followers):
    choice = 0
    #choice = input("You made it to the entrance of the CUB. Do you wish to enter [y/n]? ")
    while not (choice == 'y' or choice =='n'):
        choice = input("You made it to the entrance of the CUB. Do you wish to enter [y/n]? ")
    if choice == 'y':
        print("You enter the CUB. You find yourself in the lobby.")
        while True:
            choice = 0
            #choice = int(input("Choose one:\n\
            #    1. Go upstairs into the CUB Senior Ballroom.\n\
            #    2. Go downstairs.\n"))

            while not (choice == "1"  or choice == "2"):
                choice = input("Choose one:\n\
                1. Go upstairs into the CUB Senior Ballroom.\n\
                2. Go downstairs.\n")
            
            choice = int(choice)

            if choice == 1:
                print("You made it to the 2022 Hackathon! Rejoice!")
                print("Grab a T-Shirt and look for your team.\n")

                if followers == 0:
                    print("You didn't help any Cougs along the way, so you have no one on your team. Fitting for a selfish person.")
                    print("You struggle to compete by yourself. Thus performing poorly. Your weekend is full of sorrow... :'(")
                    break

                elif followers == 1:
                    print("You helped one Coug. You join up to form a team of two members for the Hackathon.")
                    print("By working together your team does ok during the competition, and is able to submit a suitable program.")
                    break

                elif followers == 2:
                    print("You helped two Cougs! You join up to form a team of three members for the Hackathon.")
                    print("By working together your team does good during the competition, and by having three members the workload is doable.")
                    print("Your team has fun together and makes the coding experience better. You turn in a good program.")
                    break

                elif followers == 3:
                    print("You helped three Cougs while you were on your way to the Hackathon!! They are gracious to you and want to join your team.")
                    print("You agree to join up to form a team of four members for the Hackathon.")
                    print("By working together your team does great during the competition.")
                    print("In fact, your team wins the competition because Cougs help Cougs! :)")
                    break

                elif followers == 4:
                    print("You helped four Cougs on your way to the Hackathon!!")
                    print("By showing school spirit you appease the Coding Gods (AKA The All Powerful Andy) and are blessed with good luck.")
                    print("You now have to decide which Coug is left to fend for themself and which three you'll work with.")
                    print("You join up to form a team of four members for the Hackathon, but saddened in the face of your loss.")
                    print("However, your team overcomes this grief.")
                    print("By working together your team does great during the competition.")
                    print("In fact, your team wins the competition because Cougs help Cougs! :)")
                    break

            else:  
                    choice = 0
                    while choice != 4:  
                        print("When you reach the basement lobby you see there are three rooms.")
                        print("One to your left with the lights off and the door open.")
                        print("One is to your right and the light is off and the door closed.")
                        print("Further down the hallway you can see that the light is on in a room.")
                        while not (choice == "1" or choice == "2" or choice == "3" or choice == "4"):
                            choice = input("Choose one:\n\
                            1. Go to the left.\n\
                            2. Go to the right.\n\
                            3. Travel further down the hallway.\n\
                            4. Go back upstairs to be on time to the Hackathon.\n\n")
                        choice = int(choice)
                        #if user decides to go to the left (lights off and door open)
                        if choice == 1:
                            print("This room is cold and dark. You flip the light switch but the light doesn't turn on.")
                            print("You start to get creepy vibes and decide to return to the lobby.\n\n")

                        #if user decides to go to the right (lights off and door closed)
                        if choice == 2:
                            print("You try the door handle and find it is locked. A shiver goes down your spine and you return to the lobby.\n\n")

                        #if user decides to go down the hallway
                        if choice == 3:
                            print("You notice that a Coug is in the room looking lost, so you knock. Being curious you ask what they are doing.")
                            print("They respond with that they got lost and were looking for the Hackathon.")
                            print("You tell them that's where you're going and you can show them the way. They follow you up.\n\n")
                            followers += 1

                        if choice == 4:
                            print("You go back upstairs.\n\n")


    elif choice == 'n':
        print("You do not enter the CUB and since you're late you do not participate in the 2022 Hackathon.\nYou return home sad.")

    else:
        print("You stand there confused")
        print("Unable to listen to the inner monologue of your mind.")
        print("You chose to not make a decision, or have made a wrong one.")
        print("You cry on the ground.")
        print("Game over.")




class Room:
    
    def __init__ (self, name, description, personInRoom = None, actions = None, forward=None, left=None, right=None, back= None):
        self.name = name
        self.forward = forward
        self.left = left
        self.right = right
        self.back = back
        self.description = description #a blurb once u enter the room
        self.personInRoom = personInRoom #a person in the room
        self.actions = copy.deepcopy(actions) # a list of the actions you can take(strings)

        if forward == None:
            self.forward = self
        if left == None:
            self.left = self
        if right == None:
            self.right = self
        if back == None:
            self.back = self

    def go_direction(self, direction):
        direction = direction.lower()
        validDirections = ["forward", "left", "right", "back"]
        if direction in validDirections:
            return getattr(self, direction)
        else:
            return None

    def leave(self):
        if self.name == "Entrance":
            return "Exit"

    def __str__(self):
        return self.name


# A person who has a name, a job and topics they like to talk about. Also whether they are in distress
class Person:

    def __init__ (self, name, job, topics, inDistress = False):
        self.name = name
        self.job = job
        self.topics = topics # an array of strings
        self.inDistress = inDistress

    def conversation(self):
        randInt = r.randint(0, len(self.topics) - 1)
        convoString = self.topics[randInt]
        #print(convoString)
        return convoString

    def __str__(self):
        return self.name


#checks if movement is valid
def check_movement(currentRoom, movement):
    newRoom = currentRoom.go_direction(movement)

    if(newRoom == currentRoom):
        return False, currentRoom
    else:
        return True, newRoom

#what to do when a new room is entered
def enter_room(room, actions):

    print(room.description)
   
    
#Summary: gets and validates an action from the player
#Parameters: the current room and a list of actions to take
#Returns: the action chosen
#Precond: none
#Postcond: the returned userInput will be one of the valid actions
def get_action(room, actions):
    
    #successfulMovement = -1

    for string in room.actions:
        print(string)

    #get user input
    
    userInput = input(": ")

    #validate user input
    while userInput not in actions:
        print("Not a valid action.\n")
        userInput = input(": ")

    return userInput

        
        
#Summary: allows the player to move or talk
#Parameters: the current room and a user input action
#Returns: the new room the player is in, the next step string and if the player has new followers
#Precond: user input has to be in the allowed actions
#Postcond: a newRoom has been returned
def talk_and_move(currentRoom, userInput, newFollowers):

    successfulMovement = False
    #newFollowers = False
    nextStepStr = ""
    
    
        

    #what to do based on input
    if userInput == "talk":
        print(currentRoom.personInRoom.conversation())
        #check if you have helped the people arguing
        if(currentRoom.name == "Front of the Auditorium"):
            newFollowers = True
        nextStepStr = "You have now talked to everyone here.\n"
        return currentRoom, nextStepStr, newFollowers
    elif userInput == "forward":
        successfulMovement, newRoom = check_movement(currentRoom, "forward")
                
    elif userInput == "back":
        successfulMovement, newRoom = check_movement(currentRoom, "back")
            
    elif userInput == "right":
        successfulMovement, newRoom = check_movement(currentRoom, "right")
            
    elif userInput == "left":
        successfulMovement, newRoom = check_movement(currentRoom, "left")
        
    if successfulMovement == True:
        nextStepStr = "Moved rooms.\n"
        return newRoom, nextStepStr, newFollowers
    else:
        nextStepStr = "Rememeber, you're late! Please enter a room you can travel to.\n"
        return currentRoom, nextStepStr, newFollowers


#Summary: The todd hall building
#Parameters: none
#Returns: the number of new followers you have 0 or 1
#Precond: none
#Postcond: none
def toddHall():
    newFollowers = False;
    #People
    #buisnessStudentTopics = ["I have midterms this week! I don't have time to talk!", "I don't have time to hear about your Hackathon! I have exams!"]
    #SparkDeskManager = Person("Mark", "Desk Manager",buisnessStudentTopics , False)

    cafeAttendentTopics = ["Welcome! We have a staffing shortage right now so no coffee is available, sorry.\n", "Hello! Sadly we are not open right now. We're closed for a cleaning.\n"]
    cafeAttendent = Person("Samantha", "Student",cafeAttendentTopics , False)

    angryStudentTopics = ["What the h*** is wrong with you, Gary, we had a deal!\n...\nWhy are you interrupting us?!\n...\n....\nOk fair point, but...\n...\nOk ok fine. I guess you're right. I guess we can reach an agreement.\n\nYou feel good after helping some fellow Cougs resolve their issues!\n"]
    AngryStudent = Person("Robert", "Student",angryStudentTopics , True)

    sleepingStudentTopics = ["Zzzz....\n", "Mghrh....zzzzz..\n"]
    SleepingStudent = Person("Jane", "Student",sleepingStudentTopics , False)

    #sleepingStudentTopics = ["Zzzz....", "Mghrh....zzzzz.."]
    #SleepingStudent = Person("Jane", "Student",sleepingStudentTopics , False)


    #Room Descriptions
    cafeDescription = "You have entered the cafe. There are students milling around; however, none of them seem to be in a talkitive mood. \n\
You notice a cute employee working at the coffee counter who seems friendly.\n The auditorium is ahead of you and the exit to the building is behind you.\n"
    backAuditoriumDescrip = "You have entered the back of the auditorium. \n\
It may be a little old and the lights a little too bright, but at least the chairs are comfy. \n\
You notice a student asleep on one of the chairs. You debate whether to bother them. \n\
Also, you hear some angry shouting coming from the front of the auditorium. \nRemember the coffee shop is behind you and the front of the auditorium is ahead.\n"
    frontAuditoriumDescrip = "You hear two students shouting. They seem to be having a disagreement. \n\
You may want to intervene. It would probably be the right thing to do.\n The back of the audiorium is behind you.\n"

    
    #entrancePeople = {sparkDeskManager}
    actions = ["talk", "forward", "back", "right", "left"]
    
    
    #Room Objects
    #Entrance = Room("Entrance", entranceDescription, SparkDeskManager, actions)
    Cafe = Room("Cafe", cafeDescription, cafeAttendent, actions)
    BackAuditorium = Room("Back of the Auditorium", backAuditoriumDescrip, SleepingStudent,actions)
    FrontAuditorium = Room("Front of the Auditorium", frontAuditoriumDescrip, AngryStudent, actions)
    Exit = Room("Exit", "You are outside of Todd Hall.")

    #Setting Directions
    Cafe.forward = BackAuditorium;
    Cafe.back = Exit;

    BackAuditorium.forward = FrontAuditorium;
    BackAuditorium.back = Cafe;

    FrontAuditorium.back = BackAuditorium

    
    

    CurrentRoom = Cafe

    NewRoom = CurrentRoom

    nextStepStr = ""

    #entering rooms
    enter_room(CurrentRoom, CurrentRoom.actions)

    #talking with people and moving between rooms
    while NewRoom != Exit:
        while NewRoom == CurrentRoom:
            userInput = get_action(CurrentRoom, CurrentRoom.actions)
            NewRoom, nextStepStr, newFollowers = talk_and_move(CurrentRoom, userInput, newFollowers)
            print(nextStepStr)
            
            #check to see if you have helped the arguing people
            if newFollowers:
                BackAuditorium.description = "You have entered the back of the auditorium. \nIt may be a little old and the lights a little too bright, but at least the chairs are comfy. \nYou notice a student asleep on one of the chairs. You debate whether to bother them. \nYou no longer hear the angry shouting.\n"
                FrontAuditorium.description = "You are in the front of the Auditorium and they are no longer arguing. They seem to have resolved their issues.\n Remember the back of the auditorium is behind you.\n"
                AngryStudent.topics = ["Thanks for talking to us! We resloved our differences :)\n"]
        
        
        CurrentRoom = NewRoom
        enter_room(CurrentRoom, CurrentRoom.actions)
        




    if newFollowers:
        return 1
    else:
        return 0


def validate_user_input_for_spark():

    validInput = ['y', 'n']
    userInput = input("As you move on past The Spark, you brave the long walk to the CUB. As you pass by Todd Hall you think you hear angry voices inside. Do you go in? [y/n]\n").lower()

    while not(userInput in validInput):
        userInput = input("As you move on past The Spark, you brave the long walk to the CUB. As you pass by Todd Hall you think you hear angry voices inside. Do you go in? [y/n]\n").lower()

    return userInput




def main():
    #waking up and the first building
    print("It's 8:00am. You have woken up to the sound of your alarm blaring.")
    print("On the morning of the 2022 WSU Hackathon, you, yes you, have overslept.")
    print("The event starts at 8:30 and you need to get moving. What do you do?")
    print("Please enter decision number to continue.")
    morning()
    followers = 0
    followers = spark_building(followers)
    print()

    #user input for spark and the spark building
    userInput = validate_user_input_for_spark();

    if userInput == 'y':
        new = toddHall()
        followers += new
    else:
        print("You decide you don't have time and walk right past Todd Hall and the angry voices. You feel a chill run down your spine.\n")    
    print()

    #the library
    followers = library(followers)
    print()
    #the CUB building
    cub(followers)


#main
main()

