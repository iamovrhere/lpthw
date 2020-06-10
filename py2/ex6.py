x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "Additionally, I said: '%s'." % y

hilarious = True # False
joke_evaluation = "Isn't this joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left of..."
e = "string with a right side."

print w + e
