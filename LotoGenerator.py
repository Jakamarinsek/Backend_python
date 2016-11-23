import random

numdraw = raw_input("How many numbers would you like to draw: ")
seznam = random.sample(xrange(1,39),int(numdraw))
print "Vas izbor za zrebanje lota: ", seznam