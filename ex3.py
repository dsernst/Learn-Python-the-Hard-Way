# prints the string
print "I will now count my chickens:"

# prints string, then divides 30 by 6 then adds to 25
print "Hens", 25 + 30 / 6
# prints string, then multiplies 25 by 3, which is 75, 
# then takes the remainder of 75 divided by 4, which is 3
# which is subtracted from 100, resulting in 97
print "Roosters", 100 - 25 * 3 % 4

# prints string
print "Now I will count the eggs:"

# finds remainder of 4 % 2, which is 0
# divides 1 by 4,
# what happens to the remainder? we are working in integers, right?
# let's assume it treats .25 as 0
# then adds all these numbers:
# 3 + 2 + 1 - 5 + 0 - 0 + 6
# which is 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1.00 / 4.00 + 6

# prints string
print "Is it true that 3 + 2 < 5 - 7?"

# evaluates (3 + 2) < (5 - 7)
# which is 5 < -2, which is False
print 3 + 2 < 5 - 7

# prints string, then adds 3 and 2
print "What is 3 + 2?", 3 + 2
# prints string, then subtracts 7 from 5
print "What is 5 - 7?", 5 - 7

# prints string
print "Oh, that's why it's False."

# prints string
print "How about some more."

# prints string, then evaluates 5 > -2
print "Is it greater?", 5 > -2
# prints string, then evaluates 5 >= -2 
print "Is it greater or equal?", 5 >= -2
# prints string, then evaluates 5 <= -2 
print "Is it less or equal?", 5 <= -2