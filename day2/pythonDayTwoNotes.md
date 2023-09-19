# Control Flow - 
## Control the flow of your code through conditional statements 
## (including ignoring certain statements depending on the factors)

![Alt text](C:\Users\ChiedozieChukwurah\Downloads\python-flow-control-statements.webp)


#### if ,elif, else and nested if-else

##### if - core statement for handling control flow as it instantiates a condition

```python
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
```

#### In Python there are no switch statements or case statements.

## For and While Loops
#### This is mainly used to go through a collection
#### Python uses 'for' loops only, there are no 'for each' loops

```python
listData = [1, 2, 3, 4, 5]
embeddedLists = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

dictData = {
    1: {"name": "Bronson",
        "money": "£0.05"},
    2: {"name": "Masha",
        "money": "£3.66"},
    3: {"name": "Roscoe",
        "money": "£1.14"},
}

print(dictData)

#for loop format
for num in listData:  
    print(num * 2)

# nested for loops

for data in embeddedLists:
    for num in data:
        print(num)

# looping through dictionaries (nested loops)

for item in dictData.values():
    for embeddedValue in item.values():
        print(embeddedValue)


# get values for individual keys

for items in dictData.values():
    print(items["money"])

# loops and if statements

for num in listData:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("Gone too far")
    else:
        print("Too soon!")
```
## While Loops

#### While loops have a condition and will loop through as long as that condition is the case
```python
x = 0

while x < 10:
     print(f"It's working ---> {x}")
     if x == 4:
         break
     x += 1


# verifying user input

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 119:
        user_prompt = False
    else:
        print("Please provide your answer in digits")


print(f"Your age is {age}"
```
**![Alt text](C:\Users\ChiedozieChukwurah\Downloads\controlFlowDiagram)**

**![Alt text](C:\Users\ChiedozieChukwurah\Pictures\Diagram.png)**
