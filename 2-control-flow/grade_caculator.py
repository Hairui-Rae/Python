# Practice 1: grade_caculator

grade = int(input("Please input your grade(0~100):"))

if 100 >= grade >= 90:
    print("Excellent")
elif 89 >= grade >= 80:
    print("Good")
elif 79 >= grade >= 70:
    print("Average")
elif 69 >= grade >= 60:
    print("Pass")
elif 59 >= grade >= 0:
    print("Fail")
else:
    print("Please input the valid grade!")