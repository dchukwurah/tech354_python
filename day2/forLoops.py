# For and While Loops
# used to go through a collection
# Python uses 'for' loops only, there are no 'for each' loops

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

