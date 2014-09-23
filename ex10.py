tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print ""
print "Let's print an ASCII 'bel': \a"

print ""
print "How about a backspace? abc\b"

print ""
print "How about a 'formfeed'? abc\f"

print ""
print "How about a 'vertical tab'? abc\v"

print '''
this is text encapsulated by three single-quotes
maybe it extends to new lines

and empty lines!
!@#$%
'''

single_quotes = " \' \' \' "
double_quotes = " \" \" \" "

print "Prints string single_quotes: %s", single_quotes
print "Prints raw single_quotes: %r", single_quotes
print "Prints string double_quotes: %s", double_quotes
print "Prints raw double_quotes: %r", double_quotes

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,