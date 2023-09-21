def addition(int1=2, int2=3):
    return int1 + int2


def multiplication(int1=2, int2=3):
    return int1 * int2


def subtraction(int1=2, int2=3):
    return int1 - int2


def division(int1=2, int2=3):
    return int1 / int2


def calculator():
    function = str(input("Which function would you like to do (addition, multiplication, division or subtraction)? "))
    first_number = int(input("What would you like your first number to be? "))
    second_number = int(input("what would you like your second number to be? "))
    if function.lower() == "division":
        return division(first_number, second_number)
    elif function.lower() == "multiplication":
        return multiplication(first_number, second_number)
    elif function.lower() == "addition":
        return addition(first_number, second_number)
    elif function.lower() == "subtraction":
        return subtraction(first_number, second_number)


loop_on = True
while loop_on:
    print(calculator())
    anotherCalculation = str(input("Would you like to do another calculation (y/n)? "))
    if anotherCalculation.lower() != "y":
        loop_on = False
