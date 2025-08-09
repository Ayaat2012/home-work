class student:
    species = "robot"
    
    def __init__(self, name):
        self.name = name

raven = student("raven")
print("Raven is a {}".format(raven.species))
print("She can do all kinds of works! \nShe can be your personal Artificial Intelligence. If you ask her, she will give you many kinds of information. And she's also able to move around! Isn't that cool?")
