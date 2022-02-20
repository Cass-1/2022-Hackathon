
#a comment
import random as r
import copy


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
        print("Not a valid action")
        userInput = input(": ")

    return userInput

        
        
#Summary: allows the player to move or talk
#Parameters: the current room and a user input action
#Returns: the new room the player is in, the next step string and if the player has new followers
#Precond: user input has to be in the allowed actions
#Postcond: a newRoom has been returned
def talk_and_move(currentRoom, userInput):

    successfulMovement = False
    newFollowers = False
    nextStepStr = ""
    
    #what to do based on input
    if userInput == "talk":
        print(currentRoom.personInRoom.conversation())
        if(currentRoom.name == "Upstairs Study Lounge"):
            newFollowers = True
        nextStepStr = "You have now talked to everyone here"
    elif userInput == "forward":
        successfulMovement, newRoom = check_movement(currentRoom, "forward")
                
    elif userInput == "back":
        successfulMovement, newRoom = check_movement(currentRoom, "back")
            
    elif userInput == "right":
        successfulMovement, newRoom = check_movement(currentRoom, "right")
            
    elif userInput == "left":
        successfulMovement, newRoom = check_movement(currentRoom, "left")
        
    if successfulMovement == True:
        nextStepStr = "Moved rooms"
        return newRoom, nextStepStr, newFollwers
    else:
        nextStepStr = "Rememeber, you're late! Please enter a room you can travel too"
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

    cafeAttendentTopics = ["Welcome! We have a staffing shortage right now so no coffe is available, sorry.", "Hello! Sadly we are not open right now. We're closed for a cleaning."]
    cafeAttendent = Person("Samantha", "Student",cafeAttendentTopics , False)

    angryStudentTopics = ["What the h*** is wrong with you Gary we had a deal!\n...\nWhy are you inturupting us?!\n...\n....\nOk fair point but...\n...\nOk ok fine. I guess you're right. I guess we can reach an agreement"]
    AngryStudent = Person("Robert", "Student",angryStudentTopics , True)

    sleepingStudentTopics = ["Zzzz....", "Mghrh....zzzzz.."]
    SleepingStudent = Person("Jane", "Student",sleepingStudentTopics , False)

    #sleepingStudentTopics = ["Zzzz....", "Mghrh....zzzzz.."]
    #SleepingStudent = Person("Jane", "Student",sleepingStudentTopics , False)


    #Room Descriptions
    cafeDescription = "You have entered the cafe. There are students milling around however none of them seem in a talkitive mood. \n\
You notice a cute employee working at the coffee counter who seems friendly. The auditorium is ahead of you and the exit to the building is behind you"
    backAuditoriumDescrip = "You have entered the back of the auditorium. \n\
It may be a little old and the lights a little too bright, but at least the chairs are comfy. \n\
You notice a student asleep on one of the chairs. You debate whether to bother them. \n\
Also, you hear some angry showting coming from the front of the auditorium. Remember the coffee shop is behind you and the front of the auditorium is ahead"
    frontAuditoriumDescrip = "You hear two students showting. They seem to be having a disagreement. \n\
You may want to interveen. It would probably be the right thing to do. The back of the audiorium is behind you"

    
    #entrancePeople = {sparkDeskManager}
    actions = ["talk", "forward", "back", "right", "left"]
    
    
    #Room Objects
    #Entrance = Room("Entrance", entranceDescription, SparkDeskManager, actions)
    Cafe = Room("Cafe", cafeDescription, cafeAttendent, actions)
    BackAuditorium = Room("Upstairs Study Lounge", backAuditoriumDescrip, SleepingStudent,actions)
    FrontAuditorium = Room("Downstairs Study Lounge", frontAuditoriumDescrip, AngryStudent, actions)
    Exit = Room("Exit", "The outside of the spark")

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
            NewRoom, nextStepStr = talk_and_move(CurrentRoom, userInput)
            print(nextStepStr)
        
        CurrentRoom = NewRoom
        enter_room(CurrentRoom, CurrentRoom.actions)
        




    if newFollowers:
        return 1
    else:
        return 0



toddHall()