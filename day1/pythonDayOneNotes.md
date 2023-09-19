## What is a variable?

#### It's a way to label data within a program and store it so it can be referenced later.
#### Python is a dynamically typed language - which means it's smart and will dynamically suggest ways to assume the code you write.
```python
a = 1
b = 2
c = 3.5
hi = "Hello World"


#type method

print(type(a))
print(a)
a = 2
print(a)

#user input

name = input("What is your name")
print(name)
```
## What are operators?
#### Symbols that execute a particular mathematical or logical functions

#### Examples
#### Arithmetic Operators:
###### +, -, *, /, %

#### Logical (Comparison) operators:
###### >, <, ==, !=, >=, <=

#### Numeric types
###### int, float, complex

```python
a = 24
b = 16.0
c = 0.333333

print(a+b)
print(a>b)
single_quotes = 'Look! Single quotes'
double_quotes = "Look! Single quotes"
```

#### String slicing
```python
# H E L L O  W O R L D
# 0 1 2 3 4 5 6 7 8 9 10

hw = "hello world"

print(hw[4:])
```
#### String methods
```python
strip_string = "Hi my name is Doz    "
print((strip_string.strip("")))

example_text = "Here's some text there's lots of text"

print(example_text.count("e")) # count sets of characters in string
print(example_text.lower()) # turns characters into lowercase#
print(example_text.replace("text", "replaced text",2))
```

#### Concatenation
```python
a = 1
b = 2.5
c = "3"

print (a + b + int(c))
print (float(c))
```
#### f-strings formatted string , avoid casting
```python
name = "Lassie"
years = 7
height_cm = 60.2
snoop = "Snoopy"
snoop_years = 52

print(f"{name} is {years} years old and {height_cm}cm tall")

print(f"{name.upper()} is {years * 7} years old in dog years!")
```
#### Rounding
```python
pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.6f}") #3.142
```
#### Percentages
```python
score = 49
max_score = 100

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:.2%}")
```

