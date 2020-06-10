# Doesn't work in python3 in theory?
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", 'two', "three", 'four')
print formatter % (True, False, 'True', 'False')
print formatter % (formatter, formatter, formatter, formatter)
# Around this point semantic cessation kicks in.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing right.",
    "So I said goodnight"
)
