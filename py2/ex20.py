from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

def seek_a_line(seek, f):
    f.seek(seek)
    print seek, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"
print_all(current_file)

print "What if we retry print all?"
# Nothing. read() moves the seek.
print_all(current_file)

print "Now let's rewind?"
rewind(current_file)

print "Let's print three lines"

current_line = 1
print_a_line(current_line, current_file)

# ++ and -- don't exist in python.
# There's a strong preference to using iterators instead.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print "Seek lines from the middle?"
# Seek is character based not line based.
seek_a_line(2, current_file)
seek_a_line(3, current_file)
seek_a_line(1, current_file)
