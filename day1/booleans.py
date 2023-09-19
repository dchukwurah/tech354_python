# What is a Boolean

#Binary option true of false

a = True
b = False

print(a ==b) # False
print(a !=b) # True
print(int (a)) # True

print(True and False) # False as it cant be true and false
print(True or False) # True as it can be true or false

#Boolean methods

hi = "Hello world!"

print(hi.isalpha()) # checks if it has alphabetical characters
print(hi.islower()) # checks lowercase
print(hi.endswith("!")) #True

# Boolean values

x = 0
y = 10

print(bool(x)) # x = 0
print(bool(y)) # x = 10 true because it's not 0

#Value of None (null in other languages)
#use as a placeholder for a value

z = None

print(z is not None)

