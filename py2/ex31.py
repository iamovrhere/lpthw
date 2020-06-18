prompt = "> "
print "You enter a dark room with two doors. Do you go through door #1 or door #2"

door = raw_input(prompt)

if door == "1":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input(prompt)

    if bear == "1":
        print "You grab it. That takes the cake! Haha, I slay me."
        print "Oh wait, no. That's the bear"
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Weird motivation"
    else:
        print "Well, doing %s is probably better? Bear gets bored and runs off" % bear

elif door == "2":
    print "You stare into the endless abyss, the abyss stares back"
    print "1. Blueberries"
    print "2. Yellow jacket clothespins"
    print "3. Understanding revolvers yelling melodies"

    insanity = raw_input(prompt)

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by the mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of jello. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
