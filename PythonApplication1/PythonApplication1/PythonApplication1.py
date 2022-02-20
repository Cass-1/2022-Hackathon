
#a comment
import random as r
import copy


class Room:
    
    def __init__ (self, name, description,personInRoom, actions, forward=None, left=None, right=None, back= None):
        self.name = name
        self.forward = forward
        self.left = left
        self.right = right
        self.back = back
        self.description = description #a blurb once u enter the room
        self.personInRoom = personInRoom #a list of the people in the room
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
#Returns: the new room the player is in
#Precond: user input has to be in the allowed actions
#Postcond: a newRoom has been returned
def talk_and_move(currentRoom, userInput):

    successfulMovement = False
    nextStepStr = ""
    
    #what to do based on input
    if userInput == "talk":
        print(currentRoom.personInRoom.conversation())
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
        return newRoom, nextStepStr
    else:
        nextStepStr = "Rememeber, you're late! Please enter a room you can travel too"
        return currentRoom, nextStepStr



def main():
    #People
    sparkManagerTopics = ["The weather sure is nice!", "You should stop by and grab some coffee!"]
    sparkDeskManager = Person("Mark", "Desk Manager",sparkManagerTopics , False)

    studyingStudentTopics = ["I have miderms soon!", "Hush! I'm trying to study"]
    studyingStudent = Person("Samantha", "Student",studyingStudentTopics , False)

    cryingStudentTopics = ["Thanks for talking with me. I've had a very long day", "I really appreciate you talking to me. It's been nice to see a friendly face!"]
    cryingStudent = Person("Robert", "Student",cryingStudentTopics , True)

    sleepingStudentTopics = ["Zzzz....", "Mghrh....zzzzz.."]
    sleepingStudent = Person("Jane", "Student",sleepingStudentTopics , False)


    #Room Descriptions
    entranceDescription = "You pass through the large main doors and find yourslef inside of The Spark. You glance around and notice a person sitting at the front desk are greated with a large staircase forward, a cafe to your left, and an exit behind you."


    #People in each room and room actions
    entrancePeople = {sparkDeskManager}
    actions = ["talk", "forward", "back", "right", "left"]
    
    
    #Room Objects
    entrance = Room("Entrance", entranceDescription, sparkDeskManager, actions)

    #Setting Directions
    
    

    currentRoom = entrance

    newRoom = currentRoom

    nextStepStr = ""

    #entering rooms
    enter_room(currentRoom, currentRoom.actions)

    #talking with people and moving between rooms
    while newRoom == currentRoom:
        userInput = get_action(currentRoom, currentRoom.actions)
        newRoom, nextStepStr = talk_and_move(currentRoom, userInput)
        print(nextStepStr)
        






#Summary: 
#Parameters: 
#Returns: 
#Precond:
#Postcond:

main()