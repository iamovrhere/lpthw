from sys import exit
# Is this bad programming? Yes.
# Was it mostly entertainment? Also yes.

CMD_HINT = "hint"
CMD_DESCRIBE = "describe"
CMD_ROOM = CMD_DESCRIBE + " room"

def ask_input(room_details):
    """
    Takes in dictionary of details it will read from, if the input matches.
    return input if not in the room_details, empty otherwise.
    """
    prompt = "> "
    next = raw_input(prompt)

    if isinstance(room_details, dict) and next in room_details:
        print room_details[next]
        return ""
    elif CMD_DESCRIBE == next:
        print """
describe - To give an account in words of (someone or something),
including all the relevant characteristics, qualities, or events
"""
        return ""

    return next

def bear_room():
    room_details = {
        CMD_HINT: "Maybe we should leave?",
        CMD_ROOM: """
Why is there a bear in a room?
The bear has a bunch of honey
The pudgy bear is in front another door
How are you going to move the bear?
""",
        CMD_DESCRIBE + " door": "Looks rusted shut. Probably not worth it.",
        CMD_DESCRIBE + " bear": "He just wants to eat honey and your face :)"
    }
    print room_details[CMD_ROOM]
    bear_moved = False

    while True:
        next = ask_input(room_details)

        if next == "take honey":
            you_died("The bear looks at you and then slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through now"
            room_details[CMD_ROOM] = """
The bear has moved from the door, unblocking it.
The door looks rusted shut
"""
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            you_died(
                "You should have quit while you're ahead;" +
                "the bear gets pissed off and bites yer leg off."
            )
        elif next == "open bear":
            print "You attempt to open the bear."
            print "You remember that's not how bears work..."
            print "You step away from the bear"
        elif next == "taunt door":
            print "You yell at the door."
            print "The door stiffens up but does not respond."
        elif next == "open door":
            print "Sure! I'll just go and... AAAAUGH! Forgot about the bear"
        elif next == "open door" and bear_moved:
            print "You attempt to open the door. It doesn't budge"
            print '"This is unbearable!" you exclaim, laughing'
            print "The bear does not appreciate this."
            you_died("Bear knaws at your humerus")
        elif next == "back":
            print "You back away slowly"
            # This will cause a memory leak, since the method calls will stack.
            start()
        elif next != "":
            print "Not sure what you mean by %r. Try something else?" % next

def snake_room(snake_count=1):
    if snake_count > 5:
        you_died("A hoard of %d snakes attack you!" % snake_count)
    elif snake_count < 1:
        # This will cause a memory leak, since the method calls will stack.
        start()

    snakes = 'snakes' if snake_count > 1 else 'snake'

    CMD_SNAKES = CMD_DESCRIBE + " " + snakes
    room_details = {
        CMD_HINT: "Maybe we should leave?",
        CMD_ROOM: """
There's %d %s! Hissing menacingly.
There's a door onward and door back
""" % (snake_count, snakes),
        CMD_SNAKES: "They look mean. Sounds like there's more ahead",
    }
    print room_details[CMD_ROOM]

    print "Do you go onward or back?"

    while True:
        next = ask_input(room_details)
        if "back" in next:
            print "You back away slowly"
            snake_room(snake_count - 1)
        elif "flee" in next:
            print "You run all the way back screaming"
            snake_room(0)
        elif "onward" in next:
            print "Brave or foolish you march on"
            snake_room(snake_count + 1)
        elif "grab snake" in next:
            you_died("Why would you do that?! It bites you.")
        elif next != "":
            print "Maybe not around the snakes..."

def you_died(reason):
    print reason, "\nYou are dead. At least you tried."
    exit(0)

def you_win():
    print """


You're now in an open field
Turns out, all you had to do was say 'please'

Why, yes. That IS lazy story telling.
But I AM writing this to entertain myself, so... You know.
"""

    exit(0)

def start():
    CMD_LIGHT = "turn on a light"
    CMD_SECRET = "please"
    CMD_SIGN = CMD_DESCRIBE + " sign"

    room_details = {
        CMD_HINT: "Maybe we should %s?" % CMD_LIGHT,
        CMD_ROOM: "It's too dark to see. Just doors your right and left",
        CMD_SIGN: "It's dark, are you sure that's not just a wall?"
    }
    print "You are in a dark room"
    print "There is a door to your right and left"
    print "Which do you take"

    while True:
        next = ask_input(room_details)

        if next == CMD_LIGHT:
            print "You turn on the light."
            print "You wince at the brightness. You can see the room clearly..."
            print "Oh! There's a sign on the wall"
            room_details[CMD_ROOM] = \
                "There's door to your right and left, and a sign on the wall"
            room_details[CMD_SIGN] = \
                "It says, \"To exit, say '%s'\"" % CMD_SECRET
        elif next == "left":
            bear_room()
        elif next == "right":
            snake_room()
        elif CMD_SECRET in next:
            print "The world around you shakes"
            print "You hear a deafening rumble"
            print "Your heart begins to pound then...suddenly"
            print "*pop*"
            you_win()
        elif next == "onward":
            print "You walk straight into the wall in front of you."
            print "You see yourself walking straight through the wall in front."
            print "..."
            start()
        elif next != "":
            print "Not sure what to do with '%s'" % next

print "Welcome to Python Trap"
print "(Try describing things or using hints)"
start()
