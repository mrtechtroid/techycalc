
def normal():
    print("Welcome To Normal Calculator")
    print("Here you can Add(+), Subtract(-), Multiply(*) and Divide(/)")
    num1 = input("Enter the First Number:")
    operator = input("Enter the Operation :")
    num2 = input("Enter the Second Number:")
    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        out = num1 + num2
    elif operator == "-":
        out = num1 - num2
    elif operator == "*":
        out = num1 * num2
    elif operator == "/":
        out = num1 / num2
    else:
        out = "Please Enter A Valid string"
    print("Answer: " + str(out))
    print("Do you want to go back or re-calculate")
    msgres = input("1. Go Back 2. Recalculate:")
    if msgres == "1":
        menu()
    else:
        normal()
def rootsolve():
    print("Welcome To Root solver")
    print("What Type Of Equation Is Your Equation")
    print("1. Linear Equation(One Variable)")
    print("2. Linear Equation(Two Variable)")
    print("3. Pair Of Linear Equations(Two Variable)")
    print("4. Quadratic Equation")
    print("5. Cubic Equation*")
    print("6. Back")
    print("7. Exit")
    print("*-These Are Not Yet Fully Developed and may have bugs.")
    funct = input("What you want to do:")

    def linear_one():
        print("Enter The Values As Per the standard Form- ax+b=0")
        a = input("a:")
        b = input("b:")
        x = - (float(b)) / float(a)
        print("The Value of x is " + str(x))
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            rootsolve()
        else:
            linear_one()

    def linear_two():
        print("Enter The Values As Per the standard Form- ax+by+c=0")
        a = input("a:")
        b = input("b:")
        c = input("c:")
        xint = - float(c) / float(a)
        yint = -float(c) / float(b)
        slope = yint / (0 - xint)

        print("The X intercept is ("+str(xint)+",0)")
        print("The Y intercept is (0,"+str(yint)+")")
        print("Slope Is " + str(slope))
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            rootsolve()
        else:
            linear_two()

    def pair_linear():
        print("Enter The Values As Per the standard Form- a1x+b1y+c1=0 and a2x+b2y+c2=0 ")
        a1 = input("a1:")
        b1 = input("b1:")
        c1 = input("c1:")
        a2 = input("a2:")
        b2 = input("b2:")
        c2 = input("c2:")
        if (float(a1)/float(a2)) != (float(b1)/float(b2)):
            mint = (((float(a1)) * (float(b2))) - ((float(a2)) * (float(b1))))
            xint = (((float(b1)) * (float(c2))) - ((float(b2)) * (float(c1)))) / mint
            yint = (((float(c1)) * (float(a2))) - ((float(c2)) * (float(a1)))) / mint
            print("The solution is" + str(xint) + "," + str(yint))
        elif float(a1)/float(a2) == float(b1)/float(b2) and float(a1)/float(a2) == (float(c1)/float(c2)):
            print("Infinite Solutions")
        else:
            print("No solutions")
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            rootsolve()
        else:
            pair_linear()

    def quadratic():
        import cmath
        print("Enter The Values As Per the standard Form-ax^2+bx+c=0")
        a = input("a:")
        b = input("b:")
        c = input("c:")
        discriminant = (float(b) ** 2) - 4 * (float(a) * float(c))
        root1 = -((float(b)) - cmath.sqrt(discriminant)) / 2 * (float(a))
        root2 = -((float(b)) + cmath.sqrt(discriminant)) / 2 * (float(a))
        print('The roots are {0} and {1}'.format(root1, root2))
        print("The Discriminant is " + str(discriminant))
        print("The Y-Intercept is:" + str(c))
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            rootsolve()
        else:
            quadratic()

    def cubic():
        print("Enter The Values As Per the standard Form-ax^3+bx^2+cx+d=0")
        print("Please Note: This can be used only to find one Root.")
        a = input("a:")
        b = input("b:")
        c = input("c:")
        d = input("d:")
        p = (- float(b))/(3*(float(a)))
        q = ((p**3)+(((float(b))*(float(c)))-(3*((float(a))*(float(d)))))/(6*((float(a))**2)))
        r = ((float(c))/(3*float(a)))
        root = (q + (q**2 + (r-p**2)**3)**1/2)**1/3+(q - (q**2 + (r-p**2)**3)**1/2)**1/3+p
        print("One of the roots is "+str(root))
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            rootsolve()
        else:
            cubic()

    if funct == "1":
        linear_one()
    elif funct == "2":
        linear_two()
    elif funct == "3":
        pair_linear()
    elif funct == "4":
        quadratic()
    elif funct == "5":
        cubic()
    elif funct == "6":
        menu()
    else:
        exit()
def menu():
    print("1. Normal Calculator")
    print("2. Scientific Calculator")
    print("3. Graphing Calculator")
    print("4. Solving The Roots Of Equations")
    print("5. Geometry")
    print("6. Unit Converter")
    print("7. Help Center")
    print("8. Text Hasher")
    print("9. Exit")
    opt = input("Enter The Category:")
    if opt == "1":
        normal()
    elif opt == "2":
        scientific()
    elif opt == "3":
        graphingcalc()
    elif opt == "4":
        rootsolve()
    elif opt == "5":
        geometry()
    elif opt == "6":
        print("Use the app named unitconverter.py")
        input("Press Enter to continue:")
        menu()
    elif opt == "7":
        helpcenter()
    elif opt == "misc":
        print("Use the app named plugins.py")
        input("Press Enter to continue:")
        menu()
    elif opt == "8":
        passhash()
    elif opt == "9":
        exit()
    else:
        menu()
def helpcenter():
    print(
        "[______] ____ ____     \\\\  // _____  _____   ||     _____      \n"
        "   ||    ||   ||   || ||\\\\//  ||    ||   ||  ||     ||    /|   ____  \n"
        "   ||    ||__ ||   ||-|| ||   ||    ||---||  ||     ||     |   |  |   \n"
        "   ||    ||__ ||__ || || ||   ||___ ||   ||  ||____ ||___  | 0 |__|      \n"
    )
    print("Hello Everyone, By Using This App You Agree to the following extra Terms and Conditions\n"
          "1. You can use this app or parts of it by Mentioning Us In A Credits Page\n"
          "2. You will not modify the app into something malicious and reproduce it\n"
          "3. This App is for Educational Purposes Only. \n"
          "4. Other terms and conditons can be viewed at our Web Interface at Github"
          "If you have any suggestions to make, or report any bugs contact us at github.com/mrtechtroid\n"
          "For the beginner's guide you can visit this website: https://mrtechtroid.github.io/b-guide.html")
    input("Press Enter to continue")
    menu()
def scientific():
    print("Welcome To scientific Calculator")
    print("What do you want to solve")
    print("1. Trigonometric Functions")
    print("2. Logarithms")
    print("3. Squares And Cubes")
    print("4. Square And Cube Roots")
    print("5. Imaginary Numbers")
    print("6. Dot And Cross Products")
    print("7. Factor Calculator")
    print("8. Multiple Calculator")
    print("9. Back")
    print("10. Exit")

    def trigno():
        print("This is Trignometry Calculator")
        print("1. Functions")
        print("2. Inverse Functions")
        print("3. Back")

        def trigfunctions():
            import math
            print("Write the angle in degrees")
            angle = int(input("Angle:"))
            degtorad = (22/7)/180
            print("Sin:" + str(math.sin(angle * degtorad)))
            print("Cos:" + str(math.cos(angle * degtorad)))
            print("Tan:" + str(math.tan(angle * degtorad)))
            print("These Values are approximated and may not be up to mark")
            print("Exact Values can be found using the plugins available. ")

        def invtrigfunctions():
            import math
            print("Write the Value")
            value = float(input("Value:"))
            print("Sin inv:" + str(math.degrees(math.asin(value))))
            print("Cos inv:" + str(math.degrees(math.acos(value))))
            print("Tan inv:" + str(math.degrees(math.atan(value))))
            print("These Values are approximated and may not be up to point")

        trigfunct = input("Index:")
        if trigfunct == "1":
            trigfunctions()
        elif trigfunct == "2":
            invtrigfunctions()
        else:
            scientific()

    def logs():
        import math
        print("Write in the following format number")
        number = float(input("Number:"))
        base = int(input("Base:"))
        print(f"Logarithm in base {base} is:" + str(math.log(number, base)))
        print("Natural Logharithm is:" + str(math.log(number)))
        print("Logarithm in Base 2 is:" + str(math.log2(number)))
        print("Logarithm in Base 10 is:" + str(math.log10(number)))
        print("Inverse Log in Base 10 is:" + str(number**2))

    def sqacubes():
        num1 = input("Enter The Number:")
        power = input("Enter the Power:")
        print(str(float(num1) ** float(power)))

    def sqacubesroots():
        num1 = input("Enter The Number:")
        power = input("Enter the Power of root:")
        print("+/-"+str(float(num1)**(1/float(power))))

    def imaginaryno():
        print("Choose One Of The Below")
        print("1. Basic Arithmetics")
        print("2. Advanced Arithmetic")
        print("3. Back")

        def basicimg():
            print("Write in the following type (a1+b1j) and (a2+b2j)")
            imgno1 = float(input("Number 1:"))
            imgno2 = float(input("Number 2:"))
            addimg = (imgno1 + imgno2)
            subimg = (imgno1 - imgno2)
            multimg = imgno1 * imgno2
            print("Addition:"+str(addimg))
            print("Subtraction:" + str(subimg))
            print("Multiplication:" + str(multimg))
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                imaginaryno()
            else:
                basicimg()

        def adving():
            import math
            import cmath
            print("Write in the following type (a+bj)")
            aimg = float(input("a:"))
            bimg = float(input("b:"))
            fortan = bimg/aimg
            print("Conjugate is:" + str(complex(aimg, -bimg)))
            print("Magnitude is:" + str(math.sqrt(aimg**2+bimg**2)))
            print("Argument is:" + str(math.degrees(math.atan(fortan))))
            print("Polar Coordinates:" + str(cmath.polar(complex(aimg, bimg))))
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                imaginaryno()
            else:
                adving()
        msginput = input("Your Choice:")
        if msginput == "1":
            basicimg()
        elif msginput == "2":
            adving()
        else:
            scientific()

    def dotandcross():
        print("Which dimension is your vector in?")
        print("1. Two Dimensional")
        print("2. Three Dimensional")
        print("3. Back")

        def twodime():
            print("Write in the form A[a1,b1] and B[a2,b2]")
            a1 = float(input("a1:"))
            b1 = float(input("b1:"))
            a2 = float(input("a2:"))
            b2 = float(input("b2:"))
            dotp = (a1*a2)+(b1*b2)
            print("The Dot Product Is:" + str(dotp))

        def threedime():
            print("Write in the form A[a1,b1,c1] and B[a2,b2,c2]")
            a1 = float(input("a1:"))
            b1 = float(input("b1:"))
            c1 = float(input("c1:"))
            a2 = float(input("a2:"))
            b2 = float(input("b2:"))
            c2 = float(input("c2:"))
            dotp = (a1 * a2) + (b1 * b2) + (c1*c2)
            crosspi = ((b1*c2)-(b2*c1))
            crosspj = -((a1*c2)-(a2*c1))
            crosspk = ((a1*b2)-(a2*b1))
            print("The Dot Product Is:" + str(dotp))
            print("The Cross Product Is:(" + str(crosspi)+"," + str(crosspj)+"," + str(crosspk)+")")
        dime = input("Dimension:")
        if dime == "1":
            twodime()
        elif dime == "2":
            threedime()
        else:
            scientific()

    def factorcalc():
        def print_factors(x):
            print("The factors of", x, "are:")
            for i in range(1, x + 1):
                if x % i == 0:
                    print(i)

        num = int(input("Enter your number:"))
        print_factors(num)
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            menu()
        else:
            factorcalc()

    def multiple():
        num = int(input("Enter the number:"))
        multipl = int(input("Enter the number of multiples:"))
        for i in range(1, multipl + 1):
            print(num, 'x', i, '=', num * i)
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            menu()
        else:
            multiple()

    funct = input("What you want to do:")
    if funct == "1":
        trigno()
    elif funct == "2":
        logs()
    elif funct == "3":
        sqacubes()
    elif funct == "4":
        sqacubesroots()
    elif funct == "5":
        imaginaryno()
    elif funct == "6":
        dotandcross()
    elif funct == "7":
        factorcalc()
    elif funct == "8":
        multiple()
    elif funct == "9":
        menu()
    else:
        exit()
def geometry():
    print("Welcome To Geometry Calculator:")
    print("1. Two Dimensional Area")
    print("2. Three Dimensional Area")
    print("3. Parallelograms And Triangles")
    print("4. Heron's Formula")
    print("5. Triangle Checker")
    print("6. Back")
    geoindex = input("INDEX:")

    def twodimearea():
        print("Welcome To Area solve")
        print("1. Triangle")
        print("2. Quadrilaterals")
        print("3. n-gon")
        print("4. Circles And Elipses")
        print("5. Back")

        def triangle():
            height = float(input("Height:"))
            base = float(input("Base:"))
            print("Area is:" + str((1/2)*base*height))
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                twodimearea()
            else:
                triangle()

        def quadilaterals():
            print("Choose from the following quadilaterals")
            print("1. Trapezium")
            print("2. Parallelogram")
            print("3. Rectangle")
            print("4. Rhombus")
            print("5. Square")
            print("6. Kite")
            print("7. Back")

            def trapezium():
                para = float(input("Parallel side A:"))
                parb = float(input("Parallel side B:"))
                unpar = float(input("Un-parallel side:"))
                height = float(input("Height:"))
                print("Area is:" + str(0.5*(para+parb)*height))
                print("Perimeter is:" + str(para+parb+2*unpar))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    quadilaterals()
                else:
                    trapezium()

            def parallelogram():
                altitude = float(input("Altitude:"))
                base = float(input("Base:"))
                side = float(input("Side:"))
                print("Area is:" + str(altitude * base))
                print("Perimeter is:" + str(2 * (base + side)))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    quadilaterals()
                else:
                    parallelogram()

            def rectangle():
                length = float(input("Length:"))
                breadth = float(input("Breadth:"))
                print("Area is:" + str(length*breadth))
                print("Perimeter is:" + str(2*(length+breadth)))
                print("Diagonal is:" + str(((length**2)+(breadth**2))**0.5))
                print("Area of two triangles" + str(0.5*length*breadth))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    quadilaterals()
                else:
                    rectangle()

            def rhombus():
                diagnol1 = float(input("Longer Diagonal:"))
                diagnol2 = float(input("Shorter Diagonal:"))
                print("Area is:" + str(0.5 * diagnol1 * diagnol2))
                print("Side is:" + str((((diagnol1**2) + (diagnol2**2))**0.5)/2))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    quadilaterals()
                else:
                    rhombus()

            def square():
                side = float(input("Side:"))
                print("Perimeter is:" + str(4*side))
                print("Area is:" + str(side**2))
                print("Length Of Diagnol is:" + str((2**1/2)*side))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    quadilaterals()
                else:
                    square()

            def kite():
                diagnol1 = float(input("Longer Diagonal:"))
                diagnol2 = float(input("Shorter Diagonal:"))
                print("Area is:" + str(0.5*diagnol1*diagnol2))
                shodiagcut = float(input("Shorter Part of Longer Diagonal:"))
                side1 = (((diagnol2/2)**2)+shodiagcut**2)**0.5
                side2 = (((diagnol2/2)**2)+(diagnol1 - shodiagcut)**2)**0.5
                print("Sides are:" + str(side1) + "," + str(side2))
                print("Perimeter is:" + str((2*side1)+(2*side2)))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    quadilaterals()
                else:
                    kite()

            index = input("Option:")
            if index == "1":
                trapezium()
            elif index == "2":
                parallelogram()
            elif index == "3":
                rectangle()
            elif index == "4":
                rhombus()
            elif index == "5":
                square()
            elif index == "6":
                kite()
            else:
                twodimearea()

        def ngon():
            import math
            sides = float(input("Sides:"))
            sl = float(input("Side Length:"))
            print("Exterior Angle of Regular Polygon with "+str(sides)+" sides is:" + str(360/sides))
            print("Sum of interior angles of this polygon is:" + str((sides-2)*180))
            print("Number of diagnols in this polygon" + str(sides*(sides-3)/2))
            apothem = sl/(2*(math.tan(180/sides)))
            print("Apothem is:" + str(apothem))
            print("Area is:" + str((1/2)*(sides*sides)*apothem))
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                twodimearea()
            else:
                ngon()

        def circlesandellipses():
            print("1. Circles")
            print("2. Ellipses")
            print("3. Ring")
            print("4. Sector and Segment")
            index = input("Option:")

            def circles():
                import math
                radius = float(input("Radius:"))
                print("Perimeter is:" + str(2*math.pi*radius))
                print("Area is:" + str(math.pi * (radius**2)))
                print("Perimeter of The Semi Circle is:" + str((math.pi * radius)+2*radius))
                print("Area of a Semicircle of same radius:" + str((math.pi*(radius**2))/2))
                print("Perimeter of The Semi Circle is:" + str(((math.pi * radius)/2) + 2 * radius))
                print("Area of a Quadrant of same radius:" + str((math.pi * (radius ** 2)) / 4))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    circlesandellipses()
                else:
                    circles()

            def ellipses():
                print("Hello")
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    circlesandellipses()
                else:
                    ellipses()

            def ring():
                import math
                radiusa = float(input("Radius of Larger Circle"))
                radiusb = float(input("Radius of Shorter Circle"))
                print("Area of the ring:" + str(math.pi*(radiusa+radiusb)*(radiusa - radiusb)))
                print("Perimeter of the Rings combined are:" + str(2*math.pi*(radiusa+radiusb)))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    circlesandellipses()
                else:
                    ring()

            def secseg():
                import math
                radius = float(input("Radius:"))
                angle = float(input("Angle:"))
                print("Area of Sector:" + str((angle/360)*(math.pi * (radius**2))))
                print("Perimeter of Sector:" + str(((angle/360)*(2*math.pi*radius))+(2*radius)))
                areaseg = ((angle/360)*(math.pi * (radius**2)) - (0.5*(radius**2)*math.sin(angle)))
                periseg = ((math.pi*radius*angle)/180) + 2*radius*(math.sin(angle/2))
                print("Area of Segment:" + str(areaseg))
                print("Perimeter of Segment:" + str(periseg))
                print("Do you want to go back or re-calculate")
                msgres = input("1. Go Back 2. Recalculate:")
                if msgres == "1":
                    circlesandellipses()
                else:
                    secseg()
            if index == "1":
                circles()
            elif index == "2":
                ellipses()
            elif index == "3":
                ring()
            elif index == "4":
                secseg()
            else:
                circlesandellipses()

        areamenu = input("Shape:")
        if areamenu == "1":
            triangle()
        elif areamenu == "2":
            quadilaterals()
        elif areamenu == "3":
            ngon()
        elif areamenu == "4":
            circlesandellipses()
        else:
            geometry()

    def trinaglecheck():
        print("This Tool Can Be Used To Check if a traingle can be formed or not")
        a = float(input("Side A:"))
        b = float(input("Side B:"))
        c = float(input("Side C:"))
        if a+b > c and a+c > b and b+c > a:
            print("This triangle is possible")
        else:
            print("This triangle cannot be formed")
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            geometry()
        else:
            trinaglecheck()

    def parrandtri():
        print("This tool can be used to find the area of triangles and parallelograms")
        base = float(input("Base:"))
        hght = float(input("Height:"))
        print("The area of triangle formed is:" + str((base*hght)/2))
        print("The area of triangle formed is:" + str(base * hght))
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            geometry()
        else:
            parrandtri()

    def heronform():
        import math
        print("This tool can be used to calculate area of triangle by Heron's Formula")
        a = float(input("Side A"))
        b = float(input("Side B"))
        c = float(input("Side C"))
        semip = (a+b+c)/2
        area = math.sqrt(semip*(semip-a)*(semip-b)*(semip-c))
        print("Semi-Perimeter is:" + str(semip))
        print("Area is:" + str(area))
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            geometry()
        else:
            heronform()

    def threedimearea():
        print("Welcome To Area solve")
        print("1. Cuboid")
        print("2. Cube")
        print("3. Cylinder")
        print("4. Cone")
        print("5. Sphere")
        print("6. Back")

        def cuboid():
            length = float(input("Length:"))
            breadth = float(input("Breadth:"))
            height = float(input("Height:"))
            print("Surface Area is" + str(2*((length*breadth)+(breadth*height)+(height*length))) + "m^3")
            print("Volume is" + str(length*breadth*height))
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                threedimearea()
            else:
                cuboid()

        def cube():
            side = float(input("Side:"))
            print("Surface Area is:" + str(6*(side**2)))
            print("Volume is;" + str(side**3))
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                threedimearea()
            else:
                cube()

        def cylinder():
            radius = float(input("Radius:"))
            height = float(input("Height:"))
            print("Total Surface Area is " + str(2*(22/7)*(radius+height)))
            print("Curved surface Area is " + str(2*(22/7)*radius*height))
            print("Volume is" + str((22/7)*(radius**2)*height))
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                threedimearea()
            else:
                cylinder()

        def cone():
            import math
            radius = float(input("Radius:"))
            height = float(input("Height:"))
            slant = math.sqrt((radius**2)+(height**2))
            print("Total Surface Area is " + str((22 / 7) * (radius + slant)))
            print("Curved surface Area is " + str(2 * (22 / 7) * radius * height))
            print("Volume is" + str((1/3)*(22 / 7) * (radius ** 2) * height))
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                threedimearea()
            else:
                cone()

        def sphere():
            radius = float(input("Radius:"))
            print("Surface Area of Sphere:" + str(4*(22/7)*(radius**2)))
            print("Curved Surface Area of Hemisphere:" + str(2*(22/7)*(radius**2)))
            print("Total Surface Area of Hemisphere:" + str(3*(22/7)*(radius**2)))
            print("Volume of Sphere:" + str((4/3)*(22/7)*(radius**3)))
            print("Volume of Hemisphere:" + str((2/3)*(22/7)*(radius**2)))
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                threedimearea()
            else:
                sphere()

        areamenu = input("Shape:")
        if areamenu == "1":
            cuboid()
        elif areamenu == "2":
            cube()
        elif areamenu == "3":
            cylinder()
        elif areamenu == "4":
            cone()
        elif areamenu == "5":
            sphere()
        else:
            geometry()

    if geoindex == "1":
        twodimearea()
    elif geoindex == "2":
        threedimearea()
    elif geoindex == "3":
        parrandtri()
    elif geoindex == "4":
        heronform()
    elif geoindex == "5":
        trinaglecheck()
    else:
        menu()
def graphingcalc():
    def pointplot():
        import numpy as np
        import matplotlib.pyplot as plt
        index = float(input("Point X:"))
        indey = float(input("Point Y:"))
        x = np.array([index])
        y = np.array([indey])
        plt.scatter(x, y)
        plt.show()
        print("Do you want to go back or re-calculate")
        msgres = input("1. Go Back 2. Recalculate:")
        if msgres == "1":
            graphingcalc()
        else:
            pointplot()

    def trignometricfunct():
        def sin():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.sin(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                trignometricfunct()
            else:
                sin()

        def cos():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.cos(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                trignometricfunct()
            else:
                cos()

        def tan():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.tan(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                trignometricfunct()
            else:
                tan()

        def sininv():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.arcsin(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                trignometricfunct()
            else:
                sininv()

        def cosinv():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.arccos(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                trignometricfunct()
            else:
                cosinv()

        def taninv():
            import numpy as np
            import matplotlib.pyplot as plt
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = n * (np.arctan(x))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                trignometricfunct()
            else:
                taninv()

        print("Which function do you want to solve?")
        print("1. sin\n"
              "2. cos\n"
              "3. tan\n"
              "4. sin inv\n"
              "5. cos inv\n"
              "6. tan inv\n"
              "7. Back\n"
              )
        ind = input("Function:")
        if ind == '1':
            sin()
        elif ind == '2':
            cos()
        elif ind == '3':
            tan()
        elif ind == '4':
            sininv()
        elif ind == '5':
            cosinv()
        elif ind == '6':
            taninv()
        else:
            menu()

    def addsubtrig():
        print("Choose from the following options:")
        print("1. msin(x)+ncos(x)\n"
              "2. mcos(x)+ntan(x)\n"
              "3. mtan(x)+nsin(x)\n"
              "4. msin(x)+ncos(x)+ptan(x)\n"
              )
        ind = input("Choose:")

        def sincos():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = (m * (np.sin(x)) + n * (np.cos(x)))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                addsubtrig()
            else:
                sincos()

        def costan():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = (m * (np.cos(x)) + n * (np.tan(x)))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                addsubtrig()
            else:
                costan()

        def tansin():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            x = np.linspace(0, 10, 30)
            y = (m * (np.tan(x)) + n * (np.sin(x)))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                addsubtrig()
            else:
                tansin()

        def sincostan():
            import numpy as np
            import matplotlib.pyplot as plt
            m = float(input("Enter the constant m:"))
            n = float(input("Enter the constant n:"))
            p = float(input("Enter the constant p:"))
            x = np.linspace(0, 10, 30)
            y = ((m * (np.sin(x))) + (n * (np.cos(x))) + (p * (np.tan(x))))
            plt.plot(x, y, color="black")
            plt.show()
            print("Do you want to go back or re-calculate")
            msgres = input("1. Go Back 2. Recalculate:")
            if msgres == "1":
                addsubtrig()
            else:
                sincostan()

        if ind == "1":
            sincos()
        elif ind == "2":
            costan()
        elif ind == "3":
            tansin()
        elif ind == "4":
            sincostan()
        else:
            menu()

    print("1. Points Plotter")
    print("2. Trigonometric Function Grapher")
    print("3. Addition And Subtraction of Trigonometric Functions")
    print("4. Back")
    menuin = input("Menu:")
    if menuin == "1":
        pointplot()
    elif menuin == "2":
        trignometricfunct()
    elif menuin == "3":
        addsubtrig()
    else:
        graphingcalc()


def passhash():
    print("This Feature is still under Development. so it requires DevPass to run")
    print("Enter the string you want to hash")
    string1 = input("String:")

    def hashalgorithm(string1):
        import hashlib
        hash1 = hashlib.md5(string1.encode())
        print("Your MD5 Hashed string Is " + hash1.hexdigest())
        hash2 = hashlib.sha1(string1.encode())
        print("Your SHA1 Hashed string Is " + hash2.hexdigest())
        hash3 = hashlib.sha224(string1.encode())
        print("Your SHA224 Hashed string Is " + hash3.hexdigest())
        hash4 = hashlib.sha256(string1.encode())
        print("Your SHA256 Hashed string Is " + hash4.hexdigest())
        hash5 = hashlib.sha384(string1.encode())
        print("Your SHA284 Hashed string Is " + hash5.hexdigest())
        hash6 = hashlib.sha512(string1.encode())
        print("Your SHA512 Hashed string Is " + hash6.hexdigest())
        hash7 = hashlib.blake2b(string1.encode())
        print("Your BLAKE2b Hashed string Is " + hash7.hexdigest())
        hash8 = hashlib.blake2s(string1.encode())
        print("Your BLAKE2s Hashed string Is " + hash8.hexdigest())
    hashalgorithm(string1)
    menu()


print("TechyCalc 1.0 By MrTechtroid")
print("Visit github.com/mrtechtroid For More Apps")
menu()
