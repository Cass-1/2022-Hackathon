#a comment

class Room:
    
    def __init__ (self, name, forward=None, left=None, right=None, back= None, description, peopleInRoom):
        self.name = name
        self.forward = forward
        self.left = left
        self.right = right
        self.back = back
        self.description = description #a blurb once u enter the room
        self.peopleInRoom = peopleInRoom

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
        def __str__(self):
            return self.name


