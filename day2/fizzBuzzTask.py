# FizzBuzz - Write
# a
# program
# that
# asks
# for a number from the user.For multiples of 3 print "Fizz" and for multiples of 5 print "Buzz".For multiples of 3 and 5 print "FizzBuzz”.

name = str(input("What is your name? "))
numberChoice = int(input("What number do you want to guess? "))

if numberChoice % 3 == 0 and numberChoice % 5 == 0:
    print("FizzBuzz")
elif numberChoice % 3 == 0:
    print("Fizz")
elif numberChoice % 5 == 0:
    print("Buzz")
else:
    print(f"Hi {name}! You have guessed wrong. Thankyou for playing FizzBuzz.")
