import os

vehicleList = []


class Vehicle:
    def __init__(self, make, model, color, fueltype, *options):
        self.options = options
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fueltype

    def getmake(self):
        return self.make

    def getmodel(self):
        return self.model

    def getcolor(self):
        return self.color

    def getfueltype(self):
        return self.fuelType

    def getoptions(self):
        return ", ".join(self.options[0])


class Car(Vehicle):
    def __init__(self, make, model, color, fueltype, enginesize, numdoors, *options):
        super().__init__(make, model, color, fueltype, *options)
        self.engineSize = enginesize
        self.numDoors = numdoors

    def getenginesize(self):
        return self.engineSize

    def getnumdoors(self):
        return self.numDoors

    def printdetails(self):
        print(f"Car: {self.getmake().capitalize()} {self.getmodel().capitalize()}\nColor: {self.getcolor().capitalize()}"
              f"\nFuel Type: {self.getfueltype().capitalize()}\nEngine: {self.getenginesize().capitalize()}"
              f"\nDoors: {self.getnumdoors().capitalize()}\nOptions: {self.getoptions()}")
        print("-" * 15)


class Pickup(Vehicle):
    def __init__(self, make, model, color, fueltype, cabstyle, bedlength, *options):
        super().__init__(make, model, color, fueltype, *options)
        self.cabStyle = cabstyle
        self.bedLength = bedlength

    def getcabstyle(self):
        return self.cabStyle

    def getbedlength(self):
        return self.bedLength

    def printdetails(self):
        print(f"Pickup: {self.getmake().capitalize()} {self.getmodel().capitalize()}\nColor: {self.getcolor().capitalize()}"
              f"\nFuel Type: {self.getfueltype().capitalize()}\nCab style: {self.getcabstyle().capitalize()}"
              f"\nBed style: {self.getbedlength().capitalize()}\nOptions: {self.getoptions()}")
        print("-" * 15)


def main():
    os.system("cls")

    def addvehicle():
        def optionselection(vehicle_type, *options):
            print(f"{vehicle_type} option selection")
            for option in vehicle_options:
                selection = input(f"Would you like {option}? (y)es or (N)o: ")
                if selection.upper() == "Y" or selection.upper() == "YES":
                    objectoptions.append(option)
                else:
                    pass

        vehicletype = input("Car or Pickup: ")
        if vehicletype.upper() == "CAR" or vehicletype.upper() == "PICKUP":
            pass
        else:
            print("You selection does not exist...")
            input("Press enter to continue")
            main()
        vehicle_options = ["Sunroof", "Backup Camera", "XM Radio", "Bose Speakers",
                           "GPS", "Remote Start", "Cruise Control", "Power Windows"]
        objectoptions = []
        vehiclemake = input(f"Type in the make of {vehicletype}: ")
        vehiclemodel = input(f"Type in the model of {vehicletype}: ")
        vehiclecolor = input(f"Type in the color of {vehicletype}: ")
        vehiclefueltype = input(f"Type in the fuel type of {vehicletype}: ")

        if vehicletype.upper() == "CAR":
            carenginesize = input("Type in the engine size of Car: ")
            cardoornum = input("Type in the number of doors: ")
            optionselection(vehicletype, vehicle_options)

            vehicleList.append(Car(vehiclemake, vehiclemodel,
                                   vehiclecolor, vehiclefueltype, carenginesize, cardoornum, objectoptions))

        elif vehicletype.upper() == "PICKUP":
            pickupcab = input("Type in the cab style of Pickup: ")
            pickupbed = input("Type in the bed length of Pickup: ")
            optionselection(vehicletype, vehicle_options)

            vehicleList.append(Pickup(vehiclemake, vehiclemodel,
                                      vehiclecolor, vehiclefueltype, pickupcab, pickupbed, objectoptions))

    try:
        print("What user mode would you like to enter? You can 'add' a vehicle, 'list' vehicles, or 'quit'...")
        usermode = input("[1] add, [2] list, or [3] quit: ")
        if usermode.upper() == "ADD" or usermode == "1":
            addvehicle()
            main()
        elif usermode.upper() == "LIST" or usermode == "2":
            print("-" * 15)
            for vehicle in vehicleList:
                vehicle.printdetails()
            input("Press enter to continue")
            main()
        elif usermode.upper() == "QUIT" or usermode == "3":
            pass
        else:
            print("Wrong selection made")
            input("Press enter to continue")
            main()
    except Exception as e:
        print(e.upper())
        input("Press enter to continue")
        main()


if __name__ == '__main__':
    vehicleList.append(Car("Mazda", "626", "White", "Regular", "4-cylinder", "4door",
                           ["Bose Speakers", "GPS", "Remote Start", "Cruise Control", "Power Windows"]))

    vehicleList.append(Pickup("Ford", "Ranger", "Charcoal", "Regular", "Extended", "Short",
                              ["Sunroof", "Backup Camera", "XM Radio", "Bose Speakers", "GPS"]))
    main()
