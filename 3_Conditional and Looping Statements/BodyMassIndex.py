# Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used
# measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters: BMI= weight(kg)/height2(m2)
w=float(input("Enter your weight(in kg): "))
h=float(input("Enter your height(in m): "))
bmirange=round(w/(h**2),2)
print("Your BMI is",bmirange)
if bmirange<18.5:
    print("Underweight")
elif 18.5<bmirange<24.9:
    print("Normal")
elif 25<bmirange<29.9:
    print("Overweight")
else:
    print("Obese")

