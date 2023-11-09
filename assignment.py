#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    print("===Title Screen===")
    print("1.Show Instuctions")
    print("2.Quit")
    choice=input("Enter your choice:")
    if choice=="1":
        instructions()
    elif choice=="2":
        print("Goodbye!")
        quit()
    else:
        print("Invalid choice. Please try again.")
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
    # Author:
    # Modified:
    return None 



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    while True:
        title()
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()



vol=float(input("enter the volume of the cube:"))
length=vol**(1/3)
print("the length of tghe cube is",length)