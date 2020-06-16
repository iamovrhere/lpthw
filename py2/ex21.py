def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtract %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiple %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Divide %d / %d" % (a, b)
    return a / b

print "Let's do some math with funcs"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here's not really a puzzle but something to"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "The becomes: ", what, " or something."
