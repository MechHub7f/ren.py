
##this is where we will be puting all player char

#will be using this when making a char
label functions:
 init python:
  def create_plr(holder,color="7f7f7f",backup="unknown"):
   if holder=="":
    return Character(backup,color="#"+color)
   else:
    return Character(holder,color="#"+color)

 return

label chars:
 #this will hold all of the chars
 
 #the player
 call functions
 #getting player input for name
 $ player=renpy.input("what would you like to name your charictor", length=32).strip()
 define p = None
 $ p = create_plr(player)
 
 #therapist interduses DID and stuff
 $ tp = create_plr("charlot")

 #emmily is a good frind that askes innocent questions but makes the player spirel
 $ emy = create_plr("emily")

 return

label phone:
 #this is the beginning of the phone(does not work right now
 #add "images.jpeg"
 #imagebutton:
    #xpos 400
    #ypos 400
    #idle "images.jpeg"
    #action Return()
 return

label phonecall:
 "ring... ring... ring..."
 return

label vars:
 
 return


# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

label start:
 scene images
 call functions
 call chars
 call phone
 call vars
 
 $ notes = ''' 
 TODO:
 make phone work
 add more functions
 the while loop that i made has a error somewhere

 '''

 #update max to amount of chapters 
 $ chap = 1
 $ max = 2
 while chap <= max:
  call expression ("chap_" + str(chap))
  $ chap += 1

label chap_1:
 tp "wow"
 return

label chap_2:

 return
 
 "Thanks for playing! Opening the official website now..."
 #$ renpy.run(OpenURL("https://www.youtube.com/watch?v=dPmZqsQNzGA"))
 return
