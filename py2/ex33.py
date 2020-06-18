def number_loop(length):
    #i = 0
    numbers = []

    #while i < 6:
    while len(numbers) < length:
        print "At top i is %d" % len(numbers)
        numbers.append(len(numbers))

        #i += 1
        print "Numbers now: ", numbers
        print "At the bottom is %d" % len(numbers)

    print "The numbers: "

    for num in numbers:
        print num,

number_loop(6)
number_loop(8)
number_loop(2)
