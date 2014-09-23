name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
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
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)


print "This time I will try a new format character: %r." % name
# prints including the apostrophes used when defined
print "That was using a string."
print ""
print "This time I will try an integer: %r." % weight
print ""
print "What happened?"
print ""
print "What if we use two strings? %r" % (name + teeth)
# print "What if we mix integer and string??  %r" % (weight + eyes)
# the previous line breaks because Python doesn't know 
# how to add an integer and a string

print ""
print ""
# Instructions: Try to write some variables that convert the
# inches and pounds to centimeters and kilos. Do not just type
# in the measurements. Work out the math in Python.
metric_height = height * 2.54
metric_weight = weight * 0.453592
print "To the rest of the world, %s is %2.2f cm tall." % (name, 
	metric_height)
print "And they would say he is %2.4f kg heavy." % metric_weight 