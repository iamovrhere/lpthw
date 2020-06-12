from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit ENTER."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# Happens either way, at least on linux.
# print "Truncating the file. Goodbye!"
# target.truncate()

print "Now I'm going to ask you for 3 lines"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'mma write these to the file..."

target.write(
    line1 + "\n" + line2 + "\n" + line3 + "\n"
)

print "And finally, we close it."
target.close()
