import os


def main():

    stockdict = {
                 "blnd": {"name": "Blend Labs Inc.", "price": "$20.09"},
                 "wei": {"name": "Weidai Ltd.ADR", "price": "$1.23"},
                 "io": {"name": "ION Geophysical Corp.", "price": "$1.72"},
                 "ctk": {"name": "CooTek(Caymen) Inc.ADR", "price": "$2.00"},
                 "gdxd": {"name": "MicroSectors Gold Miners", "price": "$19.78"},
                 "cabo": {"name": "Cable One Inc.", "price": "$1,887.49"},
                 "tfx": {"name": "Teleflex Inc.", "price": "$390.32"},
                 "mkl": {"name": "Markel Corp.", "price": "$1,216.01"},
                 "hubs": {"name": "HubSpot Inc.", "price": "$559.59"},
                 "azo": {"name": "AutoZone Inc.", "price": "$1,605.30"},
                 }

    try:
        for i, k in enumerate(stockdict):
            print(f"{i+1}.", k.upper())

        selection = input("Select ticker index to check info: ")
        os.system("cls")
        print(f"Ticker: {selection.upper()}")
        print(f"Name: {stockdict[selection.lower()]['name']}")
        print(f"Price: {stockdict[selection.lower()]['price']}")
        userchoice = input("\n\n\nPress enter to lookup another ticker or type 'q' to quit: ")
        if userchoice.upper() == "Q":
            pass
        else:
            os.system("cls")
            main()
    except Exception as e:
        print(e)
        input("Press enter to choose another ticker")
        os.system("cls")
        main()


if __name__ == "__main__":
    main()
