spodnja = int(raw_input("vnesi spodnjo mejo: "))
zgornja = int(raw_input("vnesi zgornjo mejo: "))
for number in range(spodnja, zgornja+1, 1):
    if number %15 == 0:
        print "FizzBuzz"
    elif number %3 == 0:
        print "Fizz"
    elif number %5 == 0:
        print "Buzz"
    else:
        print number