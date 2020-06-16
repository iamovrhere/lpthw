people = 20
cats = 30
dogs = 15

if people < cats:
  print "Never too many cats"

if people > cats:
  print "Not enough cats :("

if people < dogs:
  print "The world is drooled on"

if people > dogs:
  print "The world is sorta dry"

dogs += 5

if people >= dogs:
  print "People are greater than or equal to dogs"

if people <= dogs:
  print "People are less than or equal to dogs"

if people == dogs:
  print "Dog Value is People Value"

# I can mix indenting, but it looks (and is) wrong
if people == dogs and people < cats:
    print "Dogs and Cats, living together! Mass hysteria!"
