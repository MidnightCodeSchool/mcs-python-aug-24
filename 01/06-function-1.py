"""
BMI Calucaltor
"""

def calc_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


weight = input("Enter your weight (kg): ")
weight = float(weight)

height = input("Enter your height (m): ")
height = float(height)

bmi = calc_bmi(weight, height)
print("Your BMI is:")
print(bmi)
