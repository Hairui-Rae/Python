# Practice 2: bmi_calculator

weight = float(input("Please input your weight(kg):"))
height = float(input("Please input your height(m):"))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is:{bmi:.2f}. Body type:Underweight")
elif 18.5 <= bmi <= 24:
    print(f"Your BMI is:{bmi:.2f}. Body type:Normal")
elif 24 <= bmi < 28:
    print(f"Your BMI is:{bmi:.2f}. Body type:Overweight")
else:
    print(f"Your BMI is:{bmi:.2f}. Body type:Obese")
