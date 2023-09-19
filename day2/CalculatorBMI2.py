# BMI Calaculator Task

name = str(input("What is your name? "))
age = int(input("What is your age? "))
weight = float(input("What is your weight (kg)? "))
height = float(input("What is your height (m)? "))
bmi = weight / (height ** 2)

if 40 <= bmi <= 50:
    print(f"Hi {name}! Thankyou for using the BMI Calculator. Your BMI has been calculated as {bmi:.2f},"
          f"this is a good index score your age at {age} years old.")
elif bmi > 50:
    print(f"Hi {name}! Thankyou for using the BMI Calculator. Your BMI has been calculated as {bmi:.2f},"
          f"this is an overweight index score your age at {age} years old.")
elif bmi < 40:
    print(f"Hi {name}! Thankyou for using the BMI Calculator. Your BMI has been calculated as {bmi:.2f},"
          f"this is an underweight index score your age at {age} years old.")
