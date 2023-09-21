# Functions

# DRY - Don't Repeat Yourself

# Allow us to embed/reference code, making it reusable. i.e. return = hold so hold x *x , then you can print the function

# Making a function

def print_something(printString):
    print(printString)


print_something(8)


def greeting(name):
    print(f"Hello, my name is {name}")


greeting("Doz")


# The return statement
def addition(int1=2, int2=3):
    return int1 + int2


print(addition(2, 2))


def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)
    print(type(multiargs))


multi_args(1, 2, 3, 4, 5, 6)


# Type hints - to research

# Functions good practices

# comments on what it does
# clear function and argument names
# keep functions small and compact
# avoid duplication
# correct indentation and formatting/syntax
# organised properly -
# use when needed
# return statement
# consider type hints
