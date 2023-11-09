#!python3
# Volume Calculator
# Feel free to rename your variables
# Authers: Talan Elle

import math, time

def title():
    print("===Title Screen===\n1.Show Instuctions\n2.Quit")
    choice = input("Enter your choice:")
    if choice == "1":
        instructions()
    elif choice == "2":
        print("Goodbye!")
        quit()
    else:
        print("Invalid choice. Please try again.")
        title()
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: elle
    # Modified:
    # title
    return None

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
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    while True:
        w = input("Enter Width of the rectangle: ")
        try:
            w = float(w)
            if 0 < w < 10000:
                break
        except:
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    while True:
        h = input("Enter hight of the rectangle: ")
        try:
            h = float(h)
            if 0 < h < 10000:
                break
        except:
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds four positive digits.")
    m = input("Enter units: ")
    return l, w, h, m

def RectangleVolume():
    # Author: Talan
    l, w, h, m = getRectangleValues()
    try:
        v = l * w * h
        print(f"The volume of your rectangl is {round(v,1)}{m}3")
    except:
        print("Invalid values.")
        RectangleVolume()

def RectangleSrfaceArea():
    # Author: Talan
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
    m = input("Enter units: ")
    return r, h, m

def ConeVolume():
    # Author: Talan
    r, h, m = getConeValues()
    try:
        v = math.pi * (r**2) * (h/3)
        print(f"The volume of your cone is {round(v,1)}{m}3")
    except:
        print("Invalid valuse.")
        ConeVolume()

def ConeSrfaceArea():
    # Author: Talan
    r, h, m = getConeValues()
    try:
        sa = math.pi * r * (r + math.sqrt((h**2) + (r**2)))
        print(f"The srface area of your cone is {round(sa,1)}{m}2")
    except:
        print("Invalid values.")
        ConeSrfaceArea()

def choseCalculater():
    # Author: Talan
    print("\n===Chose your Calculater===")
    print("1.Volume of a rectangler prisum.\n2.Srface Area of a rectangler prisum.\n3.Volume of a cone.\n4.Srface Area of a cone.\n5.side Lingth of a cube.\n6.Volume of a cylinder.\n7.Volume of a rectangler pyramid.\n8.Hypothonus of a right triangle")
    choose = input("Enter the calculater number: ")

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    while True:
        title()
        time.sleep(1)
        choseCalculater()
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()