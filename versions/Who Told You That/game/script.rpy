# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

##this is where we will be puting all player char

#the player
default backup="logan"
default playername=""
define p = Character("[playerName]",color="7f7f7f")
#therapist interduses DID and stuff
define therapist = Character("charlet")

#emmily is a good frind that askes innocent questions but makes the player spriel
define emily = Character("Emily")

# The game starts here.

label start:
# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.

 scene images
 screen atmpt():
  add "images.jpeg"
  imagebutton:
   xpos 400
   ypos 400
   idle "images.jpeg"
   action Return()
 call screen atmpt
   

 #getting player input for name
 $ playerName=renpy.input("what would you like to name your charictor", length=32)
 $ playerName=playerName.strip()
 if playerName=="":
  $ playerName=backup
 
 show therapist happy
 # intro to the therapist and interduses DID
 therapist "ring... ring... ring..."
 therapist "You left in a rush yesterday [p] so i just want to go over what we talked about. You have DID. "
 
 #interdusing DID
 show player sad
 menu:
  "what is DID again":
    therapist "I already told you what DID is"

  "thank you so much":
   therapist "ofcourse, let me know if you have anymore questions."
  #end intro scean
 
 #the plan is for a friend to call her and ask her if she asks a innicont questions on if her alter if violent and send the player into a bad mood and makes her overthink
 scene starting of disinformation
 emily "ring... ring... ring..."
 emily "asks the player a question and sender her spirling"

 label ending:
    "Thanks for playing! Opening the official website now..."
    $ renpy.run(OpenURL("https://www.youtube.com/watch?v=dPmZqsQNzGA"))
 return
