#BMI Calaculator Task

name = input("What is your name? ")
age = input("What is your age? ")
weight = input("What is your weight (kg)? ")
height = input("What is your height (m)? ")
bmi = float(weight) / ((float(height)) * (float(height)))
print(f"Hi {name}, Thankyou for using the BMI Calculator, Your BMI has been calculated as {round(bmi,1)}.")