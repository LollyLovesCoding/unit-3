height = float(input("Your height in m: "))
weight = float(input("Your weight in kg: "))
bmi_category = ""

bmi = round(height / weight / weight, 5)
print(f"The BMI is {bmi}")

if bmi < 15.0:
    bmi_category = "very severely underweight"
elif 15.0 <= bmi <= 16.0:
    bmi_category = "severely underweight"
elif 16.1 <= bmi <= 18.4:
    bmi_category = "underweight"
elif 18.5 <= bmi <= 24.9:
    bmi_category = "normal weight"
elif 25.0 <= bmi <= 29.9:
    bmi_category = "overweight"
elif 30.0 <= bmi <= 34.9:
    bmi_category = "moderately obese"
elif 35.0 <= bmi <= 39.9:
    bmi_category = "severely obese"
elif bmi >= 40:
    bmi_category = 'very severely (or "morbidly") obese'

print(f"BMI Category: {bmi_category}")
