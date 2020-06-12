def cheese_and_cracker(cheese_count, boxes_count):
    print "%d cheeses" % cheese_count
    print "%d boxes" % boxes_count
    print "Man that's enough for... something?"
    print "Get a blanket?"

print "We can just give the func some values or vars or inputs etc."
cheese_and_cracker(20, 30)

cheeses = 10
crackers = 50

cheese_and_cracker(cheeses, crackers)

cheese_and_cracker(10+2, 5+5)

cheese_and_cracker(
    int(raw_input("Cheeses? ")),
    int(raw_input("Crackers? "))
)
