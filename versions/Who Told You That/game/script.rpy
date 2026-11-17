# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

##this is where we will be puting all player char

#the player
init python:
 def create_plr(holder):
  backup="logain"
  if not holder:
   return Character(backup,color="7f7f7f")
  else:
   return Character(backup,color="7f7f7f")

label chars:
 
 #therapist interduses DID and stuff
 define tp = None
 $ tp = create_plr("charlot")

 #emmily is a good frind that askes innocent questions but makes the player spriel
 define emily = None
 $ emy = create_plr("emily")
 # The game starts here.

label start:
# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.
 call chars

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
 define p = None
 $ p = create_plr(playerName)
 
 show tp happy
 # intro to the therapist and interduses DID
 tp "ring... ring... ring..."
 tp "You left in a rush yesterday [p] so i just want to go over what we talked about. You have DID. "
 
 #interdusing DID
 show player sad
 menu:
  "what is DID again":
    tp "I already told you what DID is"

  "thank you so much":
   tp "ofcourse, let me know if you have anymore questions."
  #end intro scean
 
 #the plan is for a friend to call her and ask her if she asks a innicont questions on if her alter if violent and send the player into a bad mood and makes her overthink
 scene starting of disinformation
 emy "ring... ring... ring..."
 emy "asks the player a question and sender her spirling"

 label ending:
    "Thanks for playing! Opening the official website now..."
    #$ renpy.run(OpenURL("https://www.youtube.com/watch?v=dPmZqsQNzGA"))
 return
