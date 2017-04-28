import math
import time

spoonstoday = 0
medtoday = None

spoons_prompts = ["How many spoons does that take?"]

class Spoons(object):
    def newspoons(self):
        if spoonstoday == 0:
            newspoonday = raw_input("How many spoons do you have today?")
            spoonstoday = newspoonday
            print "You have %s spoons today."

class DailySpoons(Spoons):
    def __init__(self):
        while medtoday == None:
            newmedsday = raw_input("Do you have medications to take today?")
            medstoday = newmedsday
        if medtoday == "YES":
            medspoons = raw_input(spoons_prompts[0])
        else:
            pass

DailySpoons.newspoons
