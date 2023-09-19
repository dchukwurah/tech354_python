# While Loops

# While loops have a condition and will loop through as long as that condition is the case

# x = 0
#
# while x < 10:
#     print(f"It's working ---> {x}")
#     if x == 4:
#         break
#     x += 1
#

# verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 119:
        user_prompt = False
    else:
        print("Please provide your answer in digits")


print(f"Your age is {age}")

changeMessage = "I made a change !"
