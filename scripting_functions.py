#!/bin/python


### FUNCTIONS

def gather_info():
    height = float(raw_input("Whats your height (enter in meters or in inches) "))
    weight = float(raw_input("Whats your weight (enter it in kilograms or in pounds) "))
    unit = raw_input("Are your measurements in Metric or Imperial units ? ").lower().strip()
    return (height, weight, unit)

#adding default value for unit
def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    print("Your BMI is %s" % bmi)

#notice tht for calculate_bmi function below , 
#we can pass keyword args (no need match seq of args in function declaration) or 
#positional args (need to maintain seq mentionined in function declaration) or
#hybrid approach (where you can mention 1st arg as positional and rest dont need to follow order)
while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(weight, unit='imperial', height=height)
        #calculate_bmi(weight=weight, height=height,  unit='imperial')
        break
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
        break
    else:
        print ("Error: Unknow measurement system. Please use Imperial or Metric")