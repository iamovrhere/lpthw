people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide."

if buses > cars:
    print "Never enough buses"
# Can't do `else if`
# else if buses < cars:
elif buses < cars:
    print "Maybe we could take the buses instead"
else:
    print "Still can't decide!"

if people > buses:
    print "Just take the bus"
else:
    print "Fine. We can stay home"
