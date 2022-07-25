def unitmenu():
    print("Welcome to Unit Solver")
    print("1. Multiples Of SI units")
    print("2. Length")
    print("3. Area")
    print("4. Temperature")
    print("5. Kinematic Viscocity")
    print("6. Dynamic Viscocity")
    print("7. Volumetric Gas Flow")
    print("8. Torque")
    print("9. Mass Flow")
    print("10. Density")
    print("11. Mass")
    print("12. Speed")
    print("13. Volume")
    print("14. Exit")
    index = input("Index:")
    if index == "1":
        print("Check the file named multiconv.txt")
        unitmenu()
    elif index == "2":
        length()
    elif index == "3":
        area()
    elif index == "4":
        temperature()
    elif index == "5":
        kinematicviscosity()
    elif index == "6":
        dynamicviscosity()
    elif index == "7":
        volumetricgasflow()
    elif index == "8":
        torque()
    elif index == "9":
        massflow()
    elif index == "10":
        density()
    elif index == "11":
        mass()
    elif index == "12":
        speed()
    elif index == "13":
        volume()
    else:
        exit()
def length():
    print("Which unit do you have:")
    print("1. Millimeters\n"
          "2. Centimeters\n"
          "3. Meters\n"
          "4. Kilometers\n"
          "5. Inches\n"
          "6. Feet\n"
          "7. Yards\n"
          "8. Miles\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        unit1 = 1
        unit2 = 0.1
        unit3 = 0.01
        unit4 = 0.000001
        unit5 = 0.03937
        unit6 = 0.003281
        unit7 = 0.001094
        unit8 = 6.21e-07
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("Press Enter To Continue")
        length()
    elif index == "2":
        unit1 = 10
        unit2 = 0.01
        unit3 = 1
        unit4 = 0.00001
        unit5 = 0.393701
        unit6 = 0.032808
        unit7 = 0.010936
        unit8 = 0.000006
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("Press Enter To Continue")
        length()
    elif index == "3":
        unit1 = 1000
        unit2 = 100
        unit3 = 1
        unit4 = 0.001
        unit5 = 39.37008
        unit6 = 3.28084
        unit7 = 1.093613
        unit8 = 0.000621
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("Press Enter To Continue")
        length()
    elif index == "4":
        unit1 = 1000000
        unit2 = 100000
        unit3 = 1000
        unit4 = 1
        unit5 = 39370.08
        unit6 = 3280.84
        unit7 = 1093.613
        unit8 = 0.621371
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("Press Enter To Continue")
        length()
    elif index == "5":
        unit1 = 25.4
        unit2 = 2.54
        unit3 = 0.0254
        unit4 = 0.000025
        unit5 = 1
        unit6 = 0.083333
        unit7 = 0.027778
        unit8 = 0.000016
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("Press Enter To Continue")
        length()
    elif index == "6":
        unit1 = 304.8
        unit2 = 30.48
        unit3 = 0.3048
        unit4 = 0.000305
        unit5 = 12
        unit6 = 1
        unit7 = 0.333333
        unit8 = 0.000189
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("Press Enter To Continue")
        length()
    elif index == "7":
        unit1 = 914.4
        unit2 = 91.44
        unit3 = 0.9144
        unit4 = 0.000914
        unit5 = 36
        unit6 = 3
        unit7 = 1
        unit8 = 0.000568
        print("in MM is:" + str(value * unit1))
        print("in CM is:" + str(value * unit2))
        print("in M is:" + str(value * unit3))
        print("in KM is:" + str(value * unit4))
        print("in INCH is:" + str(value * unit5))
        print("in FEET is:" + str(value * unit6))
        print("in YARD is:" + str(value * unit7))
        print("in MILE is:" + str(value * unit8))
        input("Press Enter To Continue")
        length()
    elif index == "8":
        unit1 = 1609344
        unit2 = 160934.4
        unit3 = 1609.344
        unit4 = 1.609344
        unit5 = 63360
        unit6 = 5280
        unit7 = 1760
        unit8 = 1
        print("in MM is:"+str(value * unit1))
        print("in CM is:"+str(value * unit2))
        print("in M is:"+str(value * unit3))
        print("in KM is:"+str(value * unit4))
        print("in INCH is:"+str(value * unit5))
        print("in FEET is:"+str(value * unit6))
        print("in YARD is:"+str(value * unit7))
        print("in MILE is:"+str(value * unit8))
        input("Press Enter To Continue")
        length()
    else:
        length()
def area():
    print("Which unit do you have:")
    print("1. Millimeter square\n"
          "2. Centimeter square\n"
          "3. Meter square\n"
          "4. Inches square\n"
          "5. Feet square\n"
          "6. Yards square\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        unit1 = 1
        unit2 = 0.01
        unit3 = 0.000001
        unit4 = 0.00155
        unit5 = 0.000011
        unit6 = 0.000001
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))

    elif index == "2":
        unit1 = 100
        unit2 = 1
        unit3 = 0.0001
        unit4 = 0.155
        unit5 = 0.001076
        unit6 = 0.00012
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        area()

    elif index == "3":
        unit1 = 1000000
        unit2 = 10000
        unit3 = 1
        unit4 = 1550.003
        unit5 = 10.76391
        unit6 = 1.19599
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        area()

    elif index == "4":
        unit1 = 645.16
        unit2 = 6.4516
        unit3 = 0.000645
        unit4 = 1
        unit5 = 0.006944
        unit6 = 0.000772
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        area()

    elif index == "5":
        unit1 = 92903
        unit2 = 929.0304
        unit3 = 0.092903
        unit4 = 144
        unit5 = 1
        unit6 = 0.111111
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        area()

    elif index == "6":
        unit1 = 836127
        unit2 = 8361.274
        unit3 = 0.836127
        unit4 = 1296
        unit5 = 9
        unit6 = 1
        print("in MM^2 is:" + str(value * unit1))
        print("in CM^2 is:" + str(value * unit2))
        print("in M^2 is:" + str(value * unit3))
        print("in INCH^2 is:" + str(value * unit4))
        print("in FEET^2 is:" + str(value * unit5))
        print("in YARD^2 is:" + str(value * unit6))
        area()
    else:
        area()
def temperature():
    print("Choose the unit given")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Celsius is:" + str(value))
        print("In Fahrenheit is:" + str((value * 9/5) + 32))
        print("In Kelvin is:" + str(value + 273.15))
        temperature()
    elif index == "2":
        print("In Celsius is:" + str((value-32)*(5/9)))
        print("In Fahrenheit is:" + str(value))
        print("In Kelvin is:" + str((value + 459.67)/1.8))
        temperature()
    elif index == "3":
        print("In Celsius is:" + str(value - 273.15))
        print("In Fahrenheit is:" + str((1.8 * value) - 459.67))
        print("In Kelvin is:" + str(value))
        temperature()
    else:
        temperature()
def kinematicviscosity():
    print("Choose the unit given")
    print("1. Centistroke")
    print("2. Stroke")
    print("3. Foot square / second")
    print("4. Metre square / second")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Centistroke is:" + str(value))
        print("In Stroke is:" + str(value * 0.01))
        print("In Foot Square / sec is:" + str(value * 0.00001))
        print("In Metre square / sec is:" + str(value * 0.000001))
        kinematicviscosity()
    elif index == "2":
        print("In Centistroke is:" + str(value * 100))
        print("In Stroke is:" + str(value))
        print("In Foot Square / sec is:" + str(value * 0.001076))
        print("In Metre square / sec is:" + str(value * 0.0001))
        kinematicviscosity()
    elif index == "3":
        print("In Centistroke is:" + str(value * 92903))
        print("In Stroke is:" + str(value * 929.03))
        print("In Foot Square / sec is:" + str(value))
        print("In Metre square / sec is:" + str(value * 0.092903))
        kinematicviscosity()
    elif index == "4":
        print("In Centistroke is:" + str(value * 1000000))
        print("In Stroke is:" + str(value * 10000))
        print("In Foot Square / sec is:" + str(value * 10.76392))
        print("In Metre square / sec is:" + str(value))
        kinematicviscosity()
    else:
        kinematicviscosity()
def dynamicviscosity():
    print("Choose the unit given")
    print("1. Centipoise")
    print("2. Poise")
    print("3. Pound square/ sec")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Centipoise is:" + str(value))
        print("In Poise is:" + str(value * 0.01))
        print("In Pound square/ sec is:" + str(value * 0.000672))
        dynamicviscosity()
    elif index == "2":
        print("In Centipoise is:" + str(value * 100))
        print("In Poise is:" + str(value))
        print("In Pound square/ sec is:" + str(value * 0.067197))
        dynamicviscosity()
    elif index == "3":
        print("In Centipoise is:" + str(value * 1488.16))
        print("In Poise is:" + str(value * 14.8816))
        print("In Pound square/ sec is:" + str(value))
        dynamicviscosity()
    else:
        dynamicviscosity()
def volumetricgasflow():
    print("Choose the unit given")
    print("1. Normal metre cube/hour")
    print("2. Standard cubic feet/hour")
    print("3. Standard cubic feet/minute")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Normal metre cube/hour is:" + str(value))
        print("In Standard cubic feet/hour is:" + str(value * 35.31073))
        print("In Standard cubic feet/minute is:" + str(value * 0.588582))
        dynamicviscosity()
    elif index == "2":
        print("In Normal metre cube/hour is:" + str(value * 0.02832))
        print("In Standard cubic feet/hour is:" + str(value))
        print("In Standard cubic feet/minute is:" + str(value * 0.016669))
        dynamicviscosity()
    elif index == "3":
        print("In Normal metre cube/hour is:" + str(value * 1.699))
        print("In Standard cubic feet/hour is:" + str(value * 59.99294))
        print("In Standard cubic feet/minute is:" + str(value))
        dynamicviscosity()
    else:
        dynamicviscosity()
def torque():
    print("Choose the unit given")
    print("1. Newton metre")
    print("2. Kilogram force metre")
    print("3. Foot pound")
    print("4. Inch pound")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Newton metre is:" + str(value))
        print("In Kilogram force metre is:" + str(value * 0.101972))
        print("In Foot pound is:" + str(value * 0.737561))
        print("In Inch pound is:" + str(value * 8.850732))
        torque()
    elif index == "2":
        print("In Newton metre is:" + str(value * 9.80665))
        print("In Kilogram force metre is:" + str(value))
        print("In Foot pound is:" + str(value * 7.233003))
        print("In Inch pound is:" + str(value * 86.79603))
        torque()
    elif index == "3":
        print("In Newton metre is:" + str(value * 1.35582))
        print("In Kilogram force metre is:" + str(value * 0.138255))
        print("In Foot pound is:" + str(value))
        print("In Inch pound is:" + str(value * 12))
        torque()
    elif index == "4":
        print("In Newton metre is:" + str(value * 0.112985))
        print("In Kilogram force metre is:" + str(value * 0.011521))
        print("In Foot pound is:" + str(value * 0.083333))
        print("In Inch pound is:" + str(value))
        torque()
    else:
        torque()
def massflow():
    print("Choose the unit given")
    print("1. Kilogram/hour")
    print("2. Pound/hour")
    print("3. Kilogram/second ")
    print("4. Ton/hour")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Kilogram/hour is:" + str(value))
        print("In Pound/hour is:" + str(value * 2.204586))
        print("In Kilogram/second  is:" + str(value * 0.000278))
        print("In Ton/hour is:" + str(value * 0.001))
        massflow()
    elif index == "2":
        print("In Kilogram/hour is:" + str(value * 0.4536))
        print("In Pound/hour is:" + str(value))
        print("In Kilogram/second  is:" + str(value * 0.000126))
        print("In Ton/hour is:" + str(value * 0.000454))
        massflow()
    elif index == "3":
        print("In Kilogram/hour is:" + str(value * 3600))
        print("In Pound/hour is:" + str(value * 7936.508))
        print("In Kilogram/second  is:" + str(value))
        print("In Ton/hour is:" + str(value * 3.6))
        massflow()
    elif index == "4":
        print("In Kilogram/hour is:" + str(value * 1000))
        print("In Pound/hour is:" + str(value * 2204.586))
        print("In Kilogram/second  is:" + str(value * 0.277778))
        print("In Ton/hour is:" + str(value))
        massflow()

    else:
        massflow()
def density():
    print("Choose the unit given")
    print("1. Gram/millilitre")
    print("2. Kilogram/metre cube")
    print("3. Pound/foot cube ")
    print("4. Pound/inch cube")
    index = input("Unit given:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("In Gram/millilitre is:" + str(value))
        print("In Kilogram/metre cube is:" + str(value * 1000))
        print("In Pound/foot cube  is:" + str(value * 62.42197))
        print("In Pound/inch cube is:" + str(value * 0.036127))
        massflow()
    elif index == "2":
        print("In Gram/millilitre is:" + str(value * 0.001))
        print("In Kilogram/metre cube is:" + str(value))
        print("In Pound/foot cube  is:" + str(value * 0.062422))
        print("In Pound/inch cube is:" + str(value * 0.000036))
        massflow()
    elif index == "3":
        print("In Gram/millilitre is:" + str(value * 0.01602))
        print("In Kilogram/metre cube is:" + str(value * 16.02))
        print("In Pound/foot cube  is:" + str(value))
        print("In Pound/inch cube is:" + str(value * 0.000579))
        massflow()
    elif index == "4":
        print("In Gram/millilitre is:" + str(value * 27.68))
        print("In Kilogram/metre cube is:" + str(value * 27680))
        print("In Pound/foot cube  is:" + str(value * 1727.84))
        print("In Pound/inch cube is:" + str(value))
        massflow()

    else:
        massflow()
def mass():
    print("Which unit do you have:")
    print("1. Grams\n"
          "2. Kilograms\n"
          "3. Metric tonnes\n"
          "4. Short ton\n"
          "5. Long ton\n"
          "6. Pounds\n"
          "7. Ounces\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":

        print("in Grams is:" + str(value))
        print("in Kilograms is:" + str(value * 0.001))
        print("in Metric tonnes is:" + str(value * 0.000001))
        print("in Short ton is:" + str(value * 0.000001))
        print("in Long ton is:" + str(value * 9.84e-07))
        print("in Pounds is:" + str(value * 0.002205))
        print("in Ounces is:" + str(value * 0.035273))
        mass()
    elif index == "2":

        print("in Grams is:" + str(value * 1000))
        print("in Kilograms is:" + str(value))
        print("in Metric tonnes is:" + str(value * 0.001))
        print("in Short ton is:" + str(value * 0.001102))
        print("in Long ton is:" + str(value * 0.000984))
        print("in Pounds is:" + str(value * 2.204586))
        print("in Ounces is:" + str(value * 35.27337))
        mass()
    elif index == "3":

        print("in Grams is:" + str(value * 1000000))
        print("in Kilograms is:" + str(value * 1000))
        print("in Metric tonnes is:" + str(value))
        print("in Short ton is:" + str(value * 1.102293))
        print("in Long ton is:" + str(value * 0.984252))
        print("in Pounds is:" + str(value * 2204.586))
        print("in Ounces is:" + str(value * 35273.37))
        mass()
    elif index == "4":

        print("in Grams is:" + str(value * 907200))
        print("in Kilograms is:" + str(value * 907.2))
        print("in Metric tonnes is:" + str(value * 0.9072))
        print("in Short ton is:" + str(value))
        print("in Long ton is:" + str(value * 0.892913))
        print("in Pounds is:" + str(value * 2000))
        print("in Ounces is:" + str(value * 32000))
        mass()
    elif index == "5":

        print("in Grams is:" + str(value * 1016000))
        print("in Kilograms is:" + str(value * 1016))
        print("in Metric tonnes is:" + str(value * 1.016))
        print("in Short ton is:" + str(value * 1.119929))
        print("in Long ton is:" + str(value))
        print("in Pounds is:" + str(value * 2239.859))
        print("in Ounces is:" + str(value * 35837.74))
        mass()
    elif index == "6":
        print("in Grams is:" + str(value * 453.6))
        print("in Kilograms is:" + str(value * 0.4536))
        print("in Metric tonnes is:" + str(value * 0.000454))
        print("in Short ton is:" + str(value * 0.0005))
        print("in Long ton is:" + str(value * 0.000446))
        print("in Pounds is:" + str(value))
        print("in Ounces is:" + str(value * 16))
        mass()
    elif index == "7":
        print("in Grams is:" + str(value * 28))
        print("in Kilograms is:" + str(value * 0.02835))
        print("in Metric tonnes is:" + str(value * 0.000028))
        print("in Short ton is:" + str(value * 0.000031))
        print("in Long ton is:" + str(value * 0.000028))
        print("in Pounds is:" + str(value * 0.0625))
        print("in Ounces is:" + str(value))
        mass()
    else:
        mass()
def speed():
    print("Which unit do you have:")
    print("1. Meter/second\n"
          "2. Meter/minute\n"
          "3. Kilometer/hour\n"
          "4. Foot/second\n"
          "5. Foot/minute \n"
          "6. Miles/hour\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("in Meter/second is:" + str(value))
        print("in Meter/minute is:" + str(value * 59.988))
        print("in Kilometer/hour is:" + str(value * 3.599712))
        print("in Foot/second is:" + str(value * 3.28084))
        print("in Foot/minute  is:" + str(value * 196.8504))
        print("in Miles/hour is:" + str(value * 2.237136))
        mass()
    elif index == "2":

        print("in Meter/second is:" + str(value * 0.01667))
        print("in Meter/minute is:" + str(value))
        print("in Kilometer/hour is:" + str(value * 0.060007))
        print("in Foot/second is:" + str(value * 0.054692))
        print("in Foot/minute  is:" + str(value * 3.281496))
        print("in Miles/hour is:" + str(value * 0.037293))
        mass()
    elif index == "3":

        print("in Meter/second is:" + str(value * 0.2778))
        print("in Meter/minute is:" + str(value * 16.66467))
        print("in Kilometer/hour is:" + str(value))
        print("in Foot/second is:" + str(value * 0.911417))
        print("in Foot/minute  is:" + str(value * 54.68504))
        print("in Miles/hour is:" + str(value * 0.621477))
        mass()
    elif index == "4":

        print("in Meter/second is:" + str(value * 0.3048))
        print("in Meter/minute is:" + str(value * 18.28434))
        print("in Kilometer/hour is:" + str(value * 1.097192))
        print("in Foot/second is:" + str(value))
        print("in Foot/minute  is:" + str(value * 60))
        print("in Miles/hour is:" + str(value * 0.681879))
        mass()
    elif index == "5":

        print("in Meter/second is:" + str(value * 0.00508))
        print("in Meter/minute is:" + str(value * 0.304739))
        print("in Kilometer/hour is:" + str(value * 0.018287))
        print("in Foot/second is:" + str(value * 0.016667))
        print("in Foot/minute  is:" + str(value))
        print("in Miles/hour is:" + str(value * 0.016667))
        mass()
    elif index == "6":
        print("in Meter/second is:" + str(value * 0.447))
        print("in Meter/minute is:" + str(value * 26.81464))
        print("in Kilometer/hour is:" + str(value * 1.609071))
        print("in Foot/second is:" + str(value * 1.466535))
        print("in Foot/minute  is:" + str(value * 87.99213))
        print("in Miles/hour is:" + str(value))
        mass()
    else:
        mass()
def volume():
    print("Which unit do you have:")
    print("1. Centimetre Cube\n"
          "2. Metre Cube\n"
          "3. Litre\n"
          "4. Inch cube\n"
          "5. Foot cube\n"
          "6. US gallons\n"
          "7. Imperial gallons\n"
          "8. US barrel (oil)\n")
    index = input("Unit Type:")
    value = float(input("Numerical Value:"))
    if index == "1":
        print("in MM is:" + str(value))
        print("in CM is:" + str(value * 0.000001))
        print("in M is:" + str(value * 0.001))
        print("in KM is:" + str(value * 0.061024))
        print("in INCH is:" + str(value * 0.000035))
        print("in FEET is:" + str(value * 0.000264))
        print("in YARD is:" + str(value * 0.00022))
        print("in MILE is:" + str(value * 0.000006))
        length()
    elif index == "2":
        print("in MM is:" + str(value * 1000000))
        print("in CM is:" + str(value))
        print("in M is:" + str(value * 1000))
        print("in KM is:" + str(value * 61024))
        print("in INCH is:" + str(value * 35))
        print("in FEET is:" + str(value * 264))
        print("in YARD is:" + str(value * 220))
        print("in MILE is:" + str(value * 6.29))
        length()
    elif index == "3":
        print("in MM is:" + str(value * 1000))
        print("in CM is:" + str(value * 0.001))
        print("in M is:" + str(value))
        print("in KM is:" + str(value * 61))
        print("in INCH is:" + str(value * 0.035))
        print("in FEET is:" + str(value * 0.264201))
        print("in YARD is:" + str(value * 0.22))
        print("in MILE is:" + str(value * 0.00629))
        length()
    elif index == "4":
        print("in MM is:" + str(value * 16.4))
        print("in CM is:" + str(value * 0.000016))
        print("in M is:" + str(value * 0.016387))
        print("in KM is:" + str(value))
        print("in INCH is:" + str(value * 0.000579))
        print("in FEET is:" + str(value * 0.004329))
        print("in YARD is:" + str(value * 0.003605))
        print("in MILE is:" + str(value * 0.000103))
        length()
    elif index == "5":
        print("in MM is:" + str(value * 28317))
        print("in CM is:" + str(value * 0.028317))
        print("in M is:" + str(value * 28.31685))
        print("in KM is:" + str(value * 1728))
        print("in INCH is:" + str(value))
        print("in FEET is:" + str(value * 7.481333))
        print("in YARD is:" + str(value * 6.229712))
        print("in MILE is:" + str(value * 0.178127))
        length()
    elif index == "6":
        print("in MM is:" + str(value * 3785))
        print("in CM is:" + str(value * 0.003785))
        print("in M is:" + str(value * 3.79))
        print("in KM is:" + str(value * 231))
        print("in INCH is:" + str(value * 0.13))
        print("in FEET is:" + str(value))
        print("in YARD is:" + str(value * 0.832701))
        print("in MILE is:" + str(value * 0.02381))
        length()
    elif index == "7":
        print("in MM is:" + str(value * 4545))
        print("in CM is:" + str(value * 0.004545))
        print("in M is:" + str(value * 4.55))
        print("in KM is:" + str(value * 277))
        print("in INCH is:" + str(value * 0.16))
        print("in FEET is:" + str(value * 1.20))
        print("in YARD is:" + str(value))
        print("in MILE is:" + str(value * 0.028593))
        length()
    elif index == "8":
        print("in MM is:" + str(value * 158970))
        print("in CM is:" + str(value * 0.15897))
        print("in M is:" + str(value * 159))
        print("in KM is:" + str(value * 9701))
        print("in INCH is:" + str(value * 6))
        print("in FEET is:" + str(value * 42))
        print("in YARD is:" + str(value * 35))
        print("in MILE is:" + str(value))
        length()
    else:
        length()


print("TechyCalc Unit Calculator By MrTechtroid")
print("Visit github.com/mrtechtroid For More Apps")
unitmenu()
