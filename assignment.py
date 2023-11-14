#!python3
# Volume Calculator
# Feel free to rename your variables
# Authers: Talan Elle

import math, time

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: elle
    # Modified: Talan added lope
    # title
    print("=====Title Screen=====\n1.Show Instuctions\n2.Quit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            instructions()
            break
        elif choice == "2":
            print("Goodbye!")
            quit()
        else:
            print("Invalid choice. Please try again. ")

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Talan
    # Modified:
    print("Enter in values for the specified varible when prompted to by the calculater.\nOnly enter units when prompted to by the calculater.")

def getRectangleValues():
    # Author: Talan
    while True:
        l = input("Enter lingth of the rectangle: ")
        try:
            l = float(l)
            if 0 < l < 10000:
                break
        except:
            print("Invalid input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    while True:
        w = input("Enter Width of the rectangle: ")
        try:
            w = float(w)
            if 0 < w < 10000:
                break
        except:
            print("Invalid input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    while True:
        h = input("Enter hight of the rectangle: ")
        try:
            h = float(h)
            if 0 < h < 10000:
                break
        except:
            print("Invalid input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    m = input("Enter units for your rectangle: ")
    return l, w, h, m

def RectangleVolume():
    # Author: Talan
    print("=====Rectangle Volume Caculater=====")
    l, w, h, m = getRectangleValues()
    try:
        v = l * w * h
        print(f"The volume of your rectangl is {round(v,1)}{m}3")
    except:
        print("Invalid values.")
        RectangleVolume()

def RectangleSrfaceArea():
    # Author: Talan
    print("=====Rectangle Srface Area Caculater=====")
    l, w, h, m = getRectangleValues()
    try:
        sa = (2 * l * w) + (2 * l * h) + (2 * w * h)
        print(f"The srface area of your rectangl is {round(sa,1)}{m}2")
    except:
        print("Invalid Valuse.")
        RectangleSrfaceArea()

def getConeValues():
    # Author: Talan
    while True:
        r = input("Enter the radius of the cone: ")
        try:
            r = float(r)
            if 0 < r < 10000:
                break
        except:
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    while True:
        h = input("Enter the hight of the cone: ")
        try:
            h = float(h)
            if 0 < h < 10000:
                break
        except:
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    m = input("Enter units for your cone: ")
    return r, h, m

def ConeVolume():
    # Author: Talan
    print("=====Cone Volume Caculater=====")
    r, h, m = getConeValues()
    try:
        v = math.pi * (r**2) * (h/3)
        print(f"The volume of your cone is {round(v,1)}{m}3")
    except:
        print("Invalid valuse.")
        ConeVolume()

def ConeSrfaceArea():
    # Author: Talan
    print("=====Cone Srface Area Caculater=====")
    r, h, m = getConeValues()
    try:
        sa = math.pi * r * (r + math.sqrt((h**2) + (r**2)))
        print(f"The srface area of your cone is {round(sa,1)}{m}2")
    except:
        print("Invalid values.")
        ConeSrfaceArea()

def CubeLength():
    # Author: Elle
    print("=====Cube Length Caculater=====")
    while True:
        vol=input("Enter the volume of the cube:")
        try:
            vol=float(vol)
            break
        except:
            print("oops! Invalid input please enter in a integer.")
        
    length=vol**(1/3)   
    print("the length of the cube is",length)

def CylinderVolume():
    # Author: Elle
    print("=====Cylinder Volume Caculater=====")
    while True:
        try:
            radius=int(input("Enter the radius of the cylinder:"))
            height=int(input("Enter the height of cylinder:"))
            volume=math.pi*(radius**2)*height
            print("the volume of the cylinder is:",volume)
            break
        except:
            print("oops! Invalid input please enter in a integer.")
    
def rectangularpyramid():
    # Author: Elle
    print("=====Rectanglarpyramid Volume Caculater=====")
    while True:
        try:
            length=int(input("enetr the lenth of the pyramid:"))
            width=int(input("enetr the width of the pyramid:")) 
            height=int(input("enetr the height of the pyramid:"))
            volume=(length*width*height)/3
            print("the volume of rectangular pyramid is:",volume)
            break
        except:
            print("oops! Invalid input please enter in a integer.")

def pythagoreanTheorem():
    # Author: Elle
    print("=====Pythagorean Theorem Caculater=====")
    while True:
        try:
            side_a=int(input("Enter the length of side A: "))
            side_b=int(input("Enter the length of side B: "))
            hypotenuse=math.sqrt(side_a**2+side_b**2)
            print("The length of the hypotenuse is: ",hypotenuse)
            break
        except:
            print("Invalid input. Please enter a vaild number.") 

def choseCalculater():
    # Author: Talan
    print("\n=====Chose your Calculater=====")
    print("1.Volume of a rectangler prisum.\n2.Srface Area of a rectangler prisum.\n3.Volume of a cone.\n4.Srface Area of a cone.\n5.side Lingth of a cube from the Volume.\n6.Volume of a cylinder.\n7.Volume of a rectangler pyramid.\n8.Hypothonus of a right triangle useing Pythagures")
    while True:
        choose = input("Enter the calculater number: ")
        time.sleep(1)
        print("\n\n")
        if choose == '1':
            RectangleVolume()
            break
        elif choose == '2':
            RectangleSrfaceArea()
            break
        elif choose == '3':
            ConeVolume()
            break
        elif choose == '4':
            ConeSrfaceArea()
            break
        elif choose == '5':
            CubeLength()
            break
        elif choose == '6':
            CylinderVolume()
            break
        elif choose == '7':
            rectangularpyramid()
            break
        elif choose == '8':
            pythagoreanTheorem()
            break
        else:
            print("invaled response. Enter the number of calculater.")




def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    while True:
        title()
        time.sleep(2)
        choseCalculater()
        time.sleep(2)
        print("\n\n")
        # keep giving options to choose menu options until they choose to exit

if __name__ == "__main__":
    main()
