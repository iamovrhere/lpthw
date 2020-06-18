from sys import exit

prompt = "> "

def gold_room():
    print "The room is full of gold. How much do you take?"

    next = raw_input(prompt)
    #if "0" in next or "1" in next:
    if next.isdigit():
        how_much = int(next)
    else:
        dead("Man, learn to type numbers.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You poor greedy soul")

def bear_room():
    print "There is a bear here."
    print "Why is there a bear in a room?"
    print "The bear has a bunch of honey"
    print "The pudgy bear is in front another door"
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input(prompt)

        if next == "take honey":
            dead("The bear looks at you and then slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through now"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("You should have quit while you're ahead; the bear gets pissed off and bites yer leg off.")
        elif next == "open bear":
            print "I don't think that's how bears work..."
        elif next == "taunt door":
            print "You yell at the door."
            print "The door stiffens up but does not respond."
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "Not sure what you mean by %r. Try something else?" % next

def chthulu_room():
    print "Here you see the great evil Chut-Cthulu-Cthululul... Angry squid face"
    print "He, it, whatever stares and you and go insane"
    print "Do you flee for your life or eat your head?"

    next = raw_input(prompt)

    if "flee" in next:
        start()
    elif "head" in next:
        dead("How? HOW?!? At least you're not hungry?")
    else:
        chthulu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room"
    print "There is a door to your right and left"
    print "Which do you take"

    next = raw_input(prompt)

    if next == "left":
        bear_room()
    elif next == "right":
        chthulu_room()
    elif next == "forward":
        print "You walk straight into the wall in front of you."
        print "You see yourself walking straight through the wall in front of you."
        print ""
        start()
    else:
        dead("You stumble around in the dark until you starve.")

start()
