def calculator_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi = weight/(height * height)

    print ("BMI =" +str(bmi))

calculator_bmi(weight=57, height=1.73)