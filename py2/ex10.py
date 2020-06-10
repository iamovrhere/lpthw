import time

tabby_cat = "\tGet it? Because tabs!"
persian_cat = "Split \non a line;\n was this meant to be a pun?"
backslash_cat = "I'm \\ a \\ cat?"

fat_cat = """
I'' do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass?
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        time.sleep(1.0 / 1000.0)
        print("\b\b%s") % i,
