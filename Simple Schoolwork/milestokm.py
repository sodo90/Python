# os module is used to clear screen after user chooses to run the program again.
import os


# Helper function called by main passing in user input and returns calculation to the console.
def miles_km(miles):
    km = miles * 1.60934
    return print(f"Total distance in Miles:\t{miles:.2f} mi\nTotal distance in Kilometers:\t{km:.3f} km")


# Main entry of the program that contains user interaction.
def main():
    # Try/except blocks used to prevent sudden termination on wrong input.
    try:
        miles = float(input("Enter mileage to convert to Kilometers: "))
        miles_km(miles)
        status = input("Press enter to continue or type 'quit': ")
        # if statement is used to trigger another loop or end the program.
        if status.lower() == "quit":
            pass
        else:
            os.system("cls")
            main()

    except Exception as e:
        print(str(e).upper())
        input("Press enter to try again...")
        main()


# If file is not imported into another project __name__ == '__main__' will be true and if statement will trigger...
# If imported __name__ == '__main__' will be false.
if __name__ == '__main__':
    # starts the main entry into the program.
    main()
