#!python3
# Volume Calculator
# Feel free to rename your variables
# Authers: Talan Elle

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Talan
    # Modified:
    print("Enter in values for the specified varible when prompted to by the calculater, \nonly enter units(eg. cm) if specified by the calculater")

def getRectangleValues():
    while True:
        l = input("Enter lingth of the rectangle: ")
        try:
            l = int(l)
            if -10000 < l < 10000:
                break
        except:
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds for digits.")
    while True:
        w = input("Enter Width of the rectangle: ")
        try:
            w = int(w)
            if -10000 < w < 10000:
                break
        except:
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds for digits.")
    while True:
        h = input("Enter hight of the rectangle: ")
        try:
            h = int(h)
            if -10000 < h < 10000:
                break
        except:
            print("Invaled input please enter in a integer.")
        else:
            print("Value exceds for digits.")
    return l, w, h

def RectangleVolume():
    l, w, h = getRectangleValues()
    m = input("Enter units: ")
    v = l * w * h
    print(f"the volume is {v}{m}3")
    

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    #main()
    RectangleVolume()