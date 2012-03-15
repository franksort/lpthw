from sys import exit

def prompt():
    return raw_input("> ")

def gold_room():
    """Places the player in the Gold Room."""
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if next.isdigit():
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        god_room(how_much)
    else:
        dead("You greedy bastard!")

def god_room(gold):
    """Places the player in the God Room"""
    print "You enter an all white room."
    print "A man dressed in a white suit addresses you."
    print "\"I am God.  Would you like to get into heaven?\""

    next = prompt()

    if next.lower() == "yes":
        print "\"Very well.  How much gold will you give me?\""

        good = False 
        while not good:
            amount = prompt()
            if amount.isdigit():
                good = True
            else:
                print "I do not understand.  Enter an amount."

        amount = int(amount)

        if amount == gold:
            print "You win."
            exit(0)
        elif amount < gold:
            dead("Your greed has damned you.")
        else:
            dead("You can't give what you don't have.")
    else:
        print "Very well, visit Cthulhu."
        cthulhu_room()

def bear_room():
    """Places the player in the Bear Room."""
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door.  You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    """Places the player in the Cthulhu Room."""
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    """Ends the game with a reason as to why the player is dead."""
    print why, "Good job!"
    exit(0)

def start():
    """Starts the game.  Places the player in the start room."""
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()


"""


                                
             left -> Bear Room
Dark Room ->
             right -> Cthulhu Room
                            flee, back to Dark Room
                            string with head, dead
                            anything else back to Cthulhu Room
"""
