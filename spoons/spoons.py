import math
import time
import sqlite3

conn = sqlite3.connect('spoonlist.db')
c = conn.cursor()

spoonsprompts = ["How many spoons does that take?"]

class User(object):
    def __init__(self):
        spoonstoday = 0
        medtoday = None
        print "Welcome to Spoons Tracker!"
        print "Have you ever used this tool before?"
        print "Yes or No?"
        newuser = raw_input(">>").upper()
        if newuser == "YES":
            user = raw_input("Enter your username:")
            password = raw_input("Enter your password:")
            t = user
            c.execute('SELECT * FROM UserList WHERE Username=?',(t,))
            checkpword = c.fetchone()
            if checkpword[2] == password:
                self.new_spoons_day()
        else:
            self.user_create()
    def user_create(self):
        c.execute('SELECT * FROM UserList WHERE Usernumber = (SELECT Max(Usernumber) FROM Userlist)')
        checkusernum = c.fetchone()
        usernum = int(checkusernum[0]) + 1
        print "Your user number is:"
        print usernum
        print "Please create a new profile!"
        email = raw_input("Email Address:")
        newusername = raw_input("Username:")
        newpassword = None
        while newpassword == None:
            passwordtest1 = raw_input("Password:")
            passwordtest2 = raw_input("Re-Enter Password:")
            if passwordtest1 == passwordtest2:
                newpassword = passwordtest1
            else:
                print "Passwords must match."
        firstname = raw_input("First Name:")
        lastname = raw_input("Last Name:")
        gender = raw_input("Gender:")
        newuserlist = [usernum, newusername, newpassword, email, firstname, lastname, gender]
        c.execute("INSERT INTO UserList VALUES (?,?,?,?,?,?,?)", (
            newuserlist[0],newuserlist[1],newuserlist[2],
            newuserlist[3],newuserlist[4],newuserlist[5],
            newuserlist[6],
            ))
        conn.commit()

    def user_spoon_set(self,userspoonset):

        c.execute("INSERT INTO SpoonList VALUES ()")

class DailySpoons(User):
    def new_spoons_day(self):
        if spoonstoday == 0:
            print "You need new spoons"
            newspoonday = raw_input("How many spoons do you have today?")
            spoonstoday = newspoonday
            print "You have %s spoons today."
        else:
            pass
    def new_meds_day(self):
        if medtoday == None:
            newmedsday = raw_input("Do you have medications to take today?")
            medstoday = newmedsday
        while medtoday == "YES":
            medspoons = raw_input(spoons_prompts[0])
        else:
            print "I'm glad."

DailySpoons()
conn.close()
print "End"
