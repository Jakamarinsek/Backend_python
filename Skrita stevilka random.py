import random
spodnja = raw_input("spodnja meja ugibanja: ")
zgornja = raw_input("zgornja meja ugibanja: ")

number = random.randint(int(spodnja),int(zgornja))
guess = int(raw_input("Ugani skrito stevilo: "))

while guess != number:
    if guess < number:
        print "Skrito stevilo je visje kot vpisano."
    if guess > number:
        print "Skrito stevilo je nizje kot vpisano."
    guess = int(raw_input("Take another guess: "))
else:
    print "Bravo. Uganili ste."