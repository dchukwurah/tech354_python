# Dictionary

# Uses key/value pairs

# key = the reference to the object

# value = the data storage mechanism you want to use (variable, list, dictionary etc.)

# Making a dictionary

student_1 = {
    "name": "Doz",
    "stream": "DevOps",
    "completed_lessons":4,
    "completed_lessons_names": ["variables", "data_types", "operators"]
}
print(student_1)

#Accessing data using the keys
print(student_1["completed_lessons"])
print(student_1["completed_lessons_names"][0])

#changing a value in a dict

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lessons_names"].remove("data_types")
print(student_1["completed_lessons_names"])

#Getting Keys

# Sets and Frozen sets

car_parts = {"wheels", "doors", "windows", "exhaust"}
print(car_parts)

car_parts.add("steering_wheel")
car_parts.discard("windows")

# Frozen sets - immutable sets

x = frozenset([1, 2, 3, 4, 5])

