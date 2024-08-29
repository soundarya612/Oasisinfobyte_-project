name= input("Enter your name:")
height= float(input("Enter the height in inches:"))
weight= float(input("enter the weight in pounds:"))
BMI= (weight * 703) / (height * height)
print(BMI)

if (BMI>0):
    if (BMI<18.5):
        print(name +",you are underweight")
    elif(BMI<=24.9):
        print(name +",you are in normal weight")
    elif(BMI<=29.9):
        print(name +",you are overweight")
    elif(BMI<=34.9):
        print(name +",you are obese")
    elif(BMI<=39.9):
        print(name +",you are severly obese")
    else:
        print(name +",you are morbidly sever")
else:
    print("Enter valid input")

