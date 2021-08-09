"""
-ask user for zip code or city
-use provided information to make api call to openweathermap.org
-display data in a readable format
-use comments within the application where appropriate
-use functions including a main function
-allow the user to run the program multiple times
-validate user input
-use try/except blocks
"""

import requests
from tkinter import *
from tkinter import ttk
from apikey import apiK


class weatherGui:
    def __init__(self, root):
        root.title("Weather Man")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.bind("<Return>", self.getForecast)

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.zipCode = StringVar()
        self.cnameVar = StringVar()
        self.ctempVar = StringVar()
        self.fltempVar = StringVar()
        self.ltempVar = StringVar()
        self.htempVar = StringVar()
        self.create_widgets()



    def create_widgets(self):
        ttk.Label(self.mainframe, text="Enter 5-digit Postal code").grid(column=0, row=0, sticky=(E,W))
        zipEntry = ttk.Entry(self.mainframe, textvariable=self.zipCode)
        zipEntry.grid(column=0, row=1, sticky=(E,W))

        htemp = ttk.Label(self.mainframe, textvariable=self.htempVar)
        htemp.grid(column=3, row=4, sticky=(E,W))

        ltemp = ttk.Label(self.mainframe, textvariable=self.ltempVar)
        ltemp.grid(column=0, row=4, sticky=(E,W), pady=5)

        cname = ttk.Label(self.mainframe, textvariable=self.cnameVar)
        cname.grid(column=0, row=2, sticky=(E,W), pady=10)

        ctemp = ttk.Label(self.mainframe, textvariable=self.ctempVar)
        ctemp.grid(column=3, row=3, sticky=(E,W))

        fltemp = ttk.Label(self.mainframe, textvariable=self.fltempVar)
        fltemp.grid(column=0, row=3,sticky=(E,W), pady=5)

        search = ttk.Button(self.mainframe, text="Get Forecast", command=self.getForecast)
        search.grid(column=3, row=0, rowspan=2, sticky=(N,S,E,W), padx=5)

        zipEntry.focus()

    def convertK(self, tempk):
        degreeC = float(tempk) - 273.15
        degreeF = (float(degreeC)/5 * 9) + 32
        return f"{degreeF:.0f}F"

    def getForecast(self, *args):
        zipvalid = FALSE
         
        for char in self.zipCode.get():
            if char not in validZip or len(self.zipCode.get()) > 5:
                self.cnameVar.set("Sorry it seems like your zipcode is invalid!")
            zipvalid = TRUE

        if zipvalid:    
            try:
                apiCall = requests.get(f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipCode.get()}&appid={apiK}")
                weatherData = apiCall.json()
                dataShort = weatherData['main']
                self.cnameVar.set(weatherData['name'])
                self.ctempVar.set(f"Current Temp: {self.convertK(dataShort['temp'])}")
                self.fltempVar.set(f"Feels Like: {self.convertK(dataShort['feels_like'])}")
                self.ltempVar.set(f"Low Temp: {self.convertK(dataShort['temp_min'])}")
                self.htempVar.set(f"High Temp: {self.convertK(dataShort['temp_max'])}")
            except:
                pass


validZip = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


if __name__ == "__main__":
    root = Tk()
    weatherGui(root)
    root.mainloop()
