# Waiter Helper Task
restaurantMenu = {
    "Starter": {
        "1": "Soup",
        "2": "Salad",
        "3": "Bruschetta"
    },
    "Main Course": {
        "1": "Steak",
        "2": "Pasta",
        "3": "Fish"
    },
    "Dessert": {
        "1": "Ice Cream",
        "2": "Cake",
        "3": "Fruit Salad"
    },
    "Drink": {
        "1": "Water",
        "2": "Wine",
        "3": "Tea"
    }
}

chosenMeal = {}  # empty dictionary for storing the menu

print("Hello and welcome to our restaurant!")
customerName = str(input("What is your name? "))

for course, courses in restaurantMenu.items():  # printing course options using a loop
    print(f"Here are the options for the {course} course:")
    for courseOption, courseMeal in courses.items():
        print(f"{courseOption}: {courseMeal}"
              f"")

    choice = input(f"Please choose from the {course} options between (1-3) for what you would like: ")  # input on the choice for a particular course

    while choice not in courses:
        print(f"Sorry {customerName}, that is an invalid choice. Please choose between (1-3): ")  # only accepting values between 1-3
        choice = input(f"Please choose a number from the {course} options for what you would like to eat: ")

    chosenMeal[course] = courses[choice]
    for chosenCourse, meal in chosenMeal.items():  # printing the selected meals
        print(f"{chosenCourse}: {meal}")
    print()

print(f"Thanks {customerName}! Your Chosen Meal is: ")  # printing choice at the end
for course, meal in chosenMeal.items():
    print(f"{course}: {meal}")
