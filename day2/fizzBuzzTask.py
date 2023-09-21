# FizzBuzz - Write
# a
# program
# that
# asks
# for a number from the user.For multiples of 3 print "Fizz" and for multiples of 5 print "Buzz".For multiples of 3 and 5 print "FizzBuzz”.
user_prompt = True

while user_prompt:
    name = input("What is your name? ")
    if name.isalpha():
        user_prompt = False
    else:
        print("Please provide your name in alphabetical letters only")

secondUserPrompt = True
numberChoice = 0
while secondUserPrompt:
    numberChoice = input("What number do you want to guess? ")
    if numberChoice.isdigit():
        secondUserPrompt = False
        if int(numberChoice) % 3 == 0 and int(numberChoice) % 5 == 0:
            print("FizzBuzz")
            print(f"Well done {name}! You won Fizzbuzz! Please refer to your trainer for prize money.")
        elif int(numberChoice) % 3 == 0:
            print("Fizz")
        elif int(numberChoice) % 5 == 0:
            print("Buzz")
        else:
            print(f"Hi {name}! You have guessed wrong. Thankyou for playing FizzBuzz.")
    else:
        print("Please provide your answer in digits")
