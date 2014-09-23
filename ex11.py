# let's try some math fun:
print "what's the first number you want to add?",
add_a = int(raw_input())

print "and the second number?",
add_b = int(raw_input())

sum_c = add_a + add_b
print "these add up to",sum_c

# following example from official python docs
s = raw_input('--> ')

print s


# what follows was the original exercise
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight
)