name = 'Zed A. Shaw'
age = 35  # not a line
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height,
                                             weight, age + height + weight)

# make inches and pounds transform centimeters and kilograms
weight = 176
height = 70

pound_kg = 0.45
inch_cm = 2.54


print "I'm %d pounds heavy and %d inches tall." % (weight, height)
print "I'm %d kg heavy and %d cm." % (weight * pound_kg, height * inch_cm)
