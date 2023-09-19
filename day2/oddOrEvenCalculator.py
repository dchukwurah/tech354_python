#OddorEvenCalculator


name = str(input("What is your name? "))
numberChoice = int(input("What number do you want to calculate? "))

if numberChoice % 2 == 0:
    print(f"Hi {name}! Thankyou for using the odd/even Calculator. Your chosen number {numberChoice} is even.")
else:
    print(f"Hi {name}! Thankyou for using the odd/even Calculator. Your chosen number {numberChoice} is odd.")