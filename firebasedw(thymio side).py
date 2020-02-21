from pythymiodw import *
import time
from libdw import pyrebase

projectid = "digital-world-e7b3d"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyDAmRG9cLlW9TDgoZC6z3ANJEqVEsg_lnQ"
email = "67ubersam@gmail.com"
password = "Sutd123456"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}


# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()

robot = ThymioReal()  # create a robot object
from time import sleep
cid_used = []
while True:
    movement_list = db.child("movement_list").get(user['idToken']).each()
    counter = 0

    if movement_list == None:
        sleep(0.5)
        continue
    else:
        for movement in movement_list:
            movement = movement.val()
            if counter == 0:
                cid = movement
                if cid in cid_used:
                    break
                else:
                    counter += 1
            else:
                print("Movement: {}".format(movement))
                if movement == 'forward':
                    robot.wheels(100, 100)
                    robot.sleep(1)
                elif movement == 'left':
                    robot.wheels(-100, 100)
                    robot.sleep(1)
                elif movement == 'right':
                    robot.wheels(100, -100)
                    robot.sleep(1)
                else:
                    robot.wheels(0, 0)
                    break
        cid_used.append(cid)
