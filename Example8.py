formatter = "%r %r %r %r"
formatter1 = "%s %s %s %s"
formatter2 = "%d %d %d %d"

print formatter % (1, 2, 3, 4)
print formatter1 % (1, 2, 3, 4)
print formatter2 % (1, 2, 3, 4)

print formatter % ("one", "two", "three", "four")
print formatter1 % ("one", "two", "three", "four")

print formatter % (True, False, False, True)
print formatter1 % (True, False, False, True)
print formatter2 % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)
print formatter1 % (formatter, formatter, formatter, formatter)

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print formatter1 % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)