weight=float(input("enter the weight"))
height=float(input("enter the height"))
def analysis(bmi):
    if bmi<=18.5:
        return "underweight"
    elif bmi<=25.0:
        return "normal"
    elif bmi<=30.0:
        return "overweight"
    else:
        return "obese"
bmi=weight/height
print(analysis(bmi))

#Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
