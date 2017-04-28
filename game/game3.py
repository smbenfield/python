from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured, subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self):
        pass
    def play(self):
        pass


class Opening(Scene):
    def enter(self):
        print "You awaken in a field in what looks like the middle of nowhere."
        print "You have a headache and are sort of cold, but overall, you're fine."
        charname = raw_input("What name would you like to be called?")
        print "Okay, not the name I would've chosen, but sure."
        print "You see a path that runs east to west in front of you."
        print "Which way do you go?"
        options = ["EAST","WEST"]
        next_scene = raw_input("East or West?").upper()
        if next_scene in options:
            return next_scene
        else:
            Invalid()
            self.enter()

class Death(Scene):
    quips = [
        "You died. That was uneventful.",
        "You're dead. Go home.",
        "Such a loser."
    ]
    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)
class Invalid(object):
    errors = [
        "That's not valid.",
        "Can you read?",
        "Why would you do this to me?"
    ]
    def __init__(self):
        print Invalid.errors[randint(0,len(self.errors)-1)]


a_game = Opening()
a_game.enter()
#Scenes:
# Opening
#    Name
#  Field
#    East
#      Yard
#        foyer
#          Kitchen
#          Living Room
#          Stairs
#            Parents Room
#            Kids Room
#    West
#      Cave
#      Ghost Cave
#  Survival
#  Death
