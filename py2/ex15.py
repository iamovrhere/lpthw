from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename
print txt.read()

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

print "Open the filename again for appending: "
file_again = raw_input("> ")

# Writing will clear file first. Even before you write input.
# Appending won't
txt_again = open(file_again, 'a')

print "Write to file? "
input = raw_input("> ")
txt_again.write(input)
