
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

def enter_Room(room, actions):

    print(room.description)
   
    for string in room.actions:
        print(string)

    #get user input
    while True:
        userInput = input(": ")
        while userInput not in actions:
           print("Not a valid action")
           userInput = input(": ")
        if userInput == "talk":
            print(room.personInRoom.conversation())
        elif userInput == "forward":
            break
        elif userInput == "back":
            break
        elif userInput == "right":
            break
        elif userInput == "left":
            break
        




def main():
    #desk manager
    entranceDescription = "You pass through the large main doors and find yourslef inside of The Spark. You glance around and notice a person sitting at the front desk are greated with a large staircase forward, a cafe to your left, and an exit behind you."
    sparkManagerTopics = ["The weather sure is nice!", "You should stop by and grab some coffee!"]
    
    sparkDeskManager = Person("Mark", "Desk Manager",sparkManagerTopics , False)

    #entrance room
    entrancePeople = {sparkDeskManager}
    actions = ["talk", "forward", "back", "right", "left"]
    entrance = Room("Entrance", entranceDescription, sparkDeskManager, actions)

    currentRoom = entrance

    #entering rooms
    enter_Room(currentRoom, currentRoom.actions)








main()