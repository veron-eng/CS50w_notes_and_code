class Point():
    #constructor, called everytime you try and make an object
    # self,  -> references the object we are creating and changes when your making different objects
    def __init__(self, x, y):
        # storing properties inside the object
        self.x = x
        self.y = y
    

p = Point(2,8)

print(p.x)
print(p.y)
