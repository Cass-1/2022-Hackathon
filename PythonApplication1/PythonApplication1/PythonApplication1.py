
#a comment
import random as r

class Room:
    
    def __init__ (self, name, description,peopleInRoom, actions, forward=None, left=None, right=None, back= None):
        self.name = name
        self.forward = forward
        self.left = left
        self.right = right
        self.back = back
        self.description = description #a blurb once u enter the room
        self.peopleInRoom = peopleInRoom #a list of the people in the room
        self.actions = actions # a list of the actions you can take(strings)

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
        convoString = r.randint(0, self.topics.len())
        return convoString

    def __str__(self):
        return self.name

def enter_Room(room):
    print(room.description)
    print(room.actions)



def main():
    print("in main")
    entranceDescription = "You pass through the large main doors and find yourslef inside of The Spark. You glance around and notice a person sitting at the front desk are greated with a large staircase forward, a cafe to your left, and an exit behind you."
    sparkDeskManager = {"Mark", "Desk Manager", {"The weather sure is nice!", "You should stop by and grab some coffee!"}, False}
    entrancePeople = {sparkDeskManager}
    actions = {"talk", "forward", "back", "right", "left"}
    

    entrance = {"Entrance", entranceDescription, entrancePeople, actions}
    currentRoom = entrance

    enter_Room(currentRoom)








main()