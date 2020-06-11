print "How old are you?",
age = raw_input()

print "How tall are you (inches)?",
height = float(raw_input())

print "How much do you weight (lbs)?",
weight = float(raw_input())

print "Why are you?",
existential = raw_input()

print "So, you're %r old, %r inches tall, and %r lbs heavy." % (
    age, height, weight)
print "Your BMI is %.2f" % ((703.00 * weight) / (height * height))
print "As for why... we'll just keep that between us."
