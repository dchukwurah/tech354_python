## Control Flow - Control the flow of your code through conditional statements (including ignoring certain statements
## depending on the factors)

#### if ,elif, else

##### if - core statement for handling control flow as it instantiates a condition

age = 17  # or input age

if age >= 18:  # anything after this is going to happen if this is the case
    print("You are old enough to watch this movie")  # indentation to show action is within the condition

# elif - Uses less processing power as it would only read the first if the first condition is met
elif age < 18:
    print("Sorry, you are not old enough to watch this movie")


film_rating = "U"

if film_rating.lower() == "u":
    print("All age groups can watch this movie")
# elif - Less processing power and runs only if if condition is not met.
elif film_rating.lower() == "pg":
    print("Parental guidance is advised for this movie")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":  # keyword or also used to check for 12 or 12a
    print("People aged 12 or over can watch this movie")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie")
elif film_rating.lower() == "18":
    print("People aged 18 or over can watch this movie")

# else
else:
    print("This is not a valid rating, please use 'u', 'pg','12', '15', '18'")

# In Python there are no switch statements or case statements.

