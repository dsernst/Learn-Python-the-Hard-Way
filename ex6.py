#define the string, with a decimal int inside of it
x = "There are %d types of people." % 10
#define the string
binary = "binary"
#define the string
do_not = "don't"
#define the string, using the two previous in there.
y = "Those who know %s and those who %s." % (binary, do_not)

#print the first string x
print x
#print the string y
print y

#print a string with the string x inside of it
print "I said: %r." % x
#print a string with the string y inside of it
print "I also said: '%s'." % y

#define the boolean var False
hilarious = False
#define the string, with a format string inside of it, 
#although the var that gets added is left unstated
joke_evaluation = "Isn't that joke so funny?! %r"

#print string joke_evaluation using var hilarious as the format string
print joke_evaluation % hilarious

#define the string
w = "This is the left side of..."
#define the string
e = "a string with a right side."

#print the last two strings, one after another
print w + e