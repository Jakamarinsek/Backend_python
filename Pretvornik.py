mile = 1.852
print("Hi. I can convert km to miles.")
odgovor = "yes"
while odgovor == "yes":
    number = int(raw_input("Enter km: "))
    km = number / mile
    print km
    odgovor = raw_input("another coversion?: ").lower()
if odgovor == "no":
    print ("bye")