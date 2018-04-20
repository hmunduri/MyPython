#!/bin/python

def gather_info():
    height = float(raw_input("what is your height ? (Inches or meetere) "))
    weight = float(raw_input("what is your weight ? (Pounds or kilograms) "))
    unit = raw_input("Are your measurements in metric or imperial unts ? ").lower().strip()
    return (height,weight,unit)
def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = (weight / (height ** 2 ))
    else:
        bmi = 703 * (weight / (height ** 2))
    print("Your BMI is %s" % bmi)

while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(weight, unit='imperial', height=height)
        break
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
        break
    else: 
       print("Error: Unknow measurement system. Please use imperial or metric.")
