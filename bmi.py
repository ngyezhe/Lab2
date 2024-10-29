def calculator_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi = weight/(height * height)

    print ("BMI =" +str(bmi))

    if bmi < 18.5:
        print("Under weight")
        return -1
    elif bmi > 18.5:
        print("Normal weight")
        return 0
    else:
        print("Over weight")
        return 1


calculator_bmi(weight=57, height=1.73)

