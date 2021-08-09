import tkinter as tk
import pickle


icon = "sf.ico"
itemcatalog = {}
poshistory = {}
salecounter = 0
getcats = []
staticupc = ""

#pos globals
salerow = 2
amount = 0
makesale = {}

load = False


#-----------------Checks for existing master data file. If one does not exist a blank data file is created in the exe folder
while not load:
    try:
        itemcatalog = pickle.load(open("master.dat", "rb"))
        makesale = pickle.load(open("saledata.dat", "rb"))
        load = True
    except:
        pickle.dump(itemcatalog, open("master.dat", "wb+"))
        pickle.dump(makesale, open("saledata.dat", "wb+"))
        continue
    for cats in itemcatalog:
        if cats not in getcats:
            getcats.append(cats)
#-----------------#

#-----Handles point of sales functions
def open_pos():
    
    def build_sale():
        global salecounter
        global salerow
        global amount
        iupc = str(salev.get())
        if iupc == "":
            return
        if iupc[-1] == "#":
            for category in itemcatalog:
                for upc in itemcatalog[category]:
                    if upc == iupc:
                        amount += 1
                        if salecounter not in makesale:
                            makesale[salecounter] = {}
                        if upc in makesale[salecounter]:
                            makesale[salecounter][upc]["qtylabel"]["text"] = amount
                            item_upc.delete(0, tk.END)
                        if upc not in makesale[salecounter]:
                            makesale[salecounter][upc] = {}
                            name = upc + " " + itemcatalog[category][upc]["Name"]
                            shortname = ""
                            print(name)
                            if len(name) > 30:
                                for i in name[0:30]:
                                    shortname += i
                                name = shortname
                            makesale[salecounter][upc]["itemlabel"] = tk.Label(sale_frame, justify="left", text=name)
                            makesale[salecounter][upc]["pricelabel"] = tk.Label(sale_frame, justify="center", text="$" + str(itemcatalog[category][upc]["Price"]))
                            makesale[salecounter][upc]["qtylabel"] = tk.Label(sale_frame, justify="right", text=str(int(amount)))
                            makesale[salecounter][upc]["itemlabel"].grid(row=salerow, column=1, sticky="w")
                            makesale[salecounter][upc]["pricelabel"].grid(row=salerow, column=2)
                            makesale[salecounter][upc]["qtylabel"].grid(row=salerow, column=3, sticky="e")
                            item_upc.delete(0, tk.END)
                            salerow += 1

        
        
                    
    pos_win = tk.Tk()
    pos_win.title("Point of Sales")

    pos_win.resizable(False, False)
    tk.Canvas(pos_win, height=600, width=300).pack()

    action_frame = tk.Frame(pos_win, bg="#1b298f")
    action_frame.place(anchor="n", relx=0.5, rely=0.005, relwidth=0.99, relheight=0.99)

    sale_frame = tk.Frame(action_frame)
    sale_frame.place(anchor="n", relx=0.5, rely=0.1, relheight=0.8, relwidth=0.98)
    sale_frame.columnconfigure(1, weight=1)
    sale_frame.columnconfigure(2, weight=1)
    sale_frame.columnconfigure(3, weight=1)
    item_header = tk.Label(sale_frame, justify="left", text="Item Name", borderwidth=2, relief="groove")
    item_header.grid(row=1, column=1, sticky="ew")
    price_header = tk.Label(sale_frame, justify="center", text="Price", borderwidth=2, relief="groove")
    price_header.grid(row=1, column=2, sticky="ew")
    qty_header = tk.Label(sale_frame, justify="right", text="QTY", borderwidth=2, relief="groove")
    qty_header.grid(row=1, column=3, sticky="ew")
    
    item_upc_label = tk.Label(action_frame, text="Type or Scan UPC")
    item_upc_label.place(anchor="n", relx=0.5, rely=0.005)
    salev = tk.StringVar(pos_win)
    salev.trace("w", lambda name, mode, index, salev=salev: build_sale())
    item_upc = tk.Entry(action_frame, justify="center", textvariable=salev)
    item_upc.place(anchor="n", relx=0.5, rely=0.045, width=100)
    item_upc.focus()

    

    
    pos_win.iconbitmap(icon)
    pos_win.mainloop()
    
#-----Check-in window handles scanning shipments into inventory
def open_ci():
    global staticupc
    def upc_search():
        match = False
        global staticupc
        upcsv = str(searchvar.get())
        itemquantity = int(item_quantity.get()) + 1
        print(upcsv)
        if upcsv == "":
            return
        if upcsv[-1] == "#":
            if upcsv != staticupc:
                item_quantity.delete(0, tk.END)
                item_quantity.insert(0, 0)
            staticupc = upcsv
            for cat in itemcatalog:
                for upc in itemcatalog[cat]:
                    if upc == upcsv:
                        upc_in.delete(0, tk.END)
                        item_name.delete(0, tk.END)
                        item_name.insert(0, itemcatalog[cat][upc]["Name"])
                        item_price.delete(0, tk.END)
                        item_price.insert(0, itemcatalog[cat][upc]["Price"])
                        item_quantity.delete(0, tk.END)
                        item_quantity.insert(0, itemquantity)
                        item_description["text"] = itemcatalog[cat][upc]["Description"]
                        match = True
        if upcsv[-1] == "#":
            if match == False:
                upc_in.delete(0, tk.END)
                item_name.delete(0, tk.END)
                item_price.delete(0, tk.END)
                item_description["text"] = "ITEM NOT FOUND IN INVENTORY"
                
                  
    def submit_ci(upcsv, quantity):
        global staticupc
        for cat in itemcatalog:
            for upc in itemcatalog[cat]:
                if upc == upcsv:
                    itemcatalog[cat][upc]["Quantity"] += int(quantity)
                    item_name.delete(0, tk.END)
                    item_price.delete(0, tk.END)
                    item_quantity.delete(0, tk.END)
                    item_quantity.insert(0, 0)
                    item_description["text"] = ""
                    staticupc = ""
                    pickle.dump(itemcatalog, open("master.dat", "wb+"))
                else:
                    continue
                
    check_ins = tk.Tk()
    check_ins.title("Check-in")

    check_ins.resizable(False, False)
    tk.Canvas(check_ins, height=450, width=300).pack()

    action_frame = tk.Frame(check_ins, bg="#1b298f")
    action_frame.place(anchor="n", relx=0.5, rely=0.005, relwidth=0.99, relheight=0.99)


    searchvar = tk.StringVar(check_ins)
    searchvar.trace("w", lambda name, mode, index, searchvar=searchvar: upc_search())
    upc_in = tk.Entry(action_frame, justify="center", textvariable=searchvar)
    upc_in.place(anchor="n", relx=0.5, rely=0.054, relwidth=0.99)
    upc_in.focus()
    upc_label = tk.Label(action_frame, text="Scan Barcode:")
    upc_label.place (anchor="n", relx=0.5, rely=0.005)
    

    item_name_label = tk.Label(action_frame, text="Item Name:", justify="left", anchor="w")
    item_name_label.place(anchor="n", relx=0.175, rely=0.125, width=100)
    item_name = tk.Entry(action_frame)
    item_name.place(anchor="nw", relx=0.35, rely=0.127, width=195)
    
    item_price_label = tk.Label(action_frame, text="Price:", justify="left", anchor="w")
    item_price_label.place(anchor="n", relx=0.175, rely=0.177, width=100)
    item_price = tk.Entry(action_frame, justify="center")
    item_price.place(anchor="nw", relx=0.35, rely=0.179, width=50)

    item_quantity_label = tk.Label(action_frame, text="Quantity:", justify="left", anchor="w")
    item_quantity_label.place(anchor="n", relx=0.698, rely=0.177, width=75)
    item_quantity = tk.Entry(action_frame, justify="right")
    item_quantity.place(anchor="nw", relx=.83, rely=0.179, width=50)
    item_quantity.insert(0, 0)

    item_description = tk.Label(action_frame, anchor="nw", justify="left")
    item_description.place(anchor="n", relx=0.5, rely=0.24, width=290, height=300)

    check_in = tk.Button(action_frame, text="Check-In", command = lambda: submit_ci(staticupc, item_quantity.get()))
    check_in.place(anchor="s", relx=0.5, rely=0.985)

    check_ins.iconbitmap(icon)
    check_ins.mainloop()

    
#-----------------View Catalog contents and make changes to items
def open_catalog():
    
    #-----Handles Catalog updates and search filtering by category
    def refresh(filterparam):
        info_name.delete(0, tk.END)
        info_upc.delete(0, tk.END)
        info_price.delete(0, tk.END)
        info_quantity.delete(0, tk.END)
        info_description["text"] = ""
        edit_description.delete(0, tk.END)
        
        if filterparam == "ALL":
            itemlist.delete(0, tk.END)
            for category in itemcatalog:
                if category != {}:
                    for upc in itemcatalog[category]:
                        posid = 1
                        itemlist.insert(posid, itemcatalog[category][upc]["Name"])
                        posid =+ posid
                        
        if filterparam in getcats:
            itemlist.delete(0, tk.END)
            posid = 1
            for upc in itemcatalog[filterparam]:
                itemlist.insert(posid, itemcatalog[filterparam][upc]["Name"])
                posid =+ 1
                
    #-----Updates selected item's database entries everything put UPC can be changed
    def update_iteminfo(name, upc, monies, quan, desc):
        for cat in itemcatalog:
            for itemid in itemcatalog[cat]:
                if upc == itemid:
                    itemcatalog[cat][upc]["Name"] = name
                    itemcatalog[cat][upc]["Price"] = monies
                    itemcatalog[cat][upc]["Quantity"] = quan
                    if len(desc) > 1:
                        itemcatalog[cat][upc]["Description"] = desc
        refresh(fv.get())
        pickle.dump(itemcatalog, open("master.dat", "wb"))
        
    #-----Removes selected item from catalog database                  
    def remove_iteminfo(name, upc, monies, quan, desc):
        for cat in itemcatalog:
            for itemid in itemcatalog[cat]:
                if upc == itemid:
                    del itemcatalog[cat][itemid]
                    itemlist.delete(0, tk.END)
                    break
        refresh(fv.get())          
        pickle.dump(itemcatalog, open("master.dat", "wb"))
        
    #-----Event bound to listbox selection            
    def open_iteminfo(event):
        itemindex = itemlist.curselection()
        itemname = itemlist.get(itemindex)
        for category in itemcatalog:
            if category != {}:
                for upc in itemcatalog[category]:
                    if itemcatalog[category][upc]["Name"] == itemname:
                        info_name.delete(0, tk.END)
                        info_name.insert(0, itemcatalog[category][upc]["Name"])
                        
                        info_upc.delete(0, tk.END)
                        info_upc.insert(0, upc)

                        info_price.delete(0, tk.END)
                        info_price.insert(0, itemcatalog[category][upc]["Price"])

                        info_quantity.delete(0, tk.END)
                        info_quantity.insert(0, itemcatalog[category][upc]["Quantity"])

                        info_description["text"] = itemcatalog[category][upc]["Description"]

    cat_win = tk.Tk()
    cat_win.title("Catalog View")

    cat_win.resizable(False, False)
    tk.Canvas(cat_win, height=450, width=450).pack()

    action_frame = tk.Frame(cat_win, bg="#1b298f")
    action_frame.place(anchor="n", relx=0.5, rely=0.005, relwidth=0.99, relheight=0.99)

    itemlist = tk.Listbox(cat_win, exportselection = False)
    posid = 1
    for category in itemcatalog:
        if category != {}:
            for upc in itemcatalog[category]:
                itemlist.insert(posid, itemcatalog[category][upc]["Name"])
                posid =+ 1
    itemlist.place(anchor="n", relx=0.15, rely=0.01, relheight=0.80)

    #-----Used to be confirm button for listbox, but is now the refresh button
    conf = tk.Button(action_frame, text="Refresh", command = lambda: refresh(fv.get()))
    conf.place(anchor="s", relx=0.144, rely=0.985, width=124.5)
    #-----
    
    info_name = tk.Entry(action_frame)
    info_name_label = tk.Label(action_frame, text="Item Name:")
    info_name_label.place(anchor="n", relx=0.382, rely=0.01)
    info_name.place(anchor="n", relx=0.64, rely=0.06, width=300)

    info_upc = tk.Entry(action_frame, justify="center")
    info_upc_label = tk.Label(action_frame, text="Item UPC:")
    info_upc_label.place(anchor="n", relx=0.372, rely=0.12)
    info_upc.place(anchor="n", relx=0.388, rely=0.169, width=75)

    info_price = tk.Entry(action_frame, justify="center")
    info_price_label = tk.Label(action_frame, text="Item Price:")
    info_price_label.place(anchor="n", relx=0.65, rely=0.12)
    info_price.place(anchor="n", relx=0.65, rely=0.169, width=100)

    info_quantity = tk.Entry(action_frame, justify="right")
    info_quantity_label = tk.Label(action_frame, text="Quantity:")
    info_quantity_label.place(anchor="n", relx=0.91, rely=0.12)
    info_quantity.place(anchor="n", relx=0.91, rely=0.169, width=56)

    info_description = tk.Label(action_frame, wraplength=292, justify="left", anchor="nw")
    edit_description = tk.Entry(action_frame)
    edit_description.place(anchor="n", relx=0.7227, rely=0.225, width=225)
    info_description_label = tk.Label(action_frame, text="Description:")
    info_description_label.place(anchor="n", relx=0.382, rely=0.22)
    info_description.place(anchor="n", relx=0.64, rely=0.28, width=300, height=240)

    info_update = tk.Button(action_frame, text="Update Item", command = lambda: update_iteminfo(info_name.get(), info_upc.get(), info_price.get(), info_quantity.get(), edit_description.get()))
    info_update.place(anchor="s", relx=0.888, rely=0.985)

    remove_item = tk.Button(action_frame, text="Remove Item", command = lambda: remove_iteminfo(info_name.get(), info_upc.get(), info_price.get(), info_quantity.get(), edit_description.get()))
    remove_item.place(anchor="s", relx=0.7, rely=0.985)
    
    itemlist.select_set(0)
    itemselect = itemlist.bind('<<ListboxSelect>>', open_iteminfo)

    fv = tk.StringVar(action_frame)
    fv.set("ALL")
    filter_cat = tk.OptionMenu(action_frame, fv, "ALL", *getcats)
    filter_cat.place(anchor="s", relx=0.144, rely=0.9, width=123.5)

    cat_win.iconbitmap(icon)
    cat_win.mainloop()
    

#-----------------Add new catalog item interface and functions
def new_item_entry():

    #-----Removes selected category if parameters are met *catalog is empty and the default new category is not slected
    def remove_cat(selected_cat, upc):
        if upc == "":
            if selected_cat != "NEW":
                if itemcatalog[selected_cat] == {}:
                    del itemcatalog[selected_cat]
                    del getcats[getcats.index(selected_cat)]
                    ie_win.destroy()
                    new_item_entry()
                    pickle.dump(itemcatalog, open("master.dat", "wb"))
        
                
    #-----New catalog item submission function
    def add_new_item(cat, monies, desc, name, upc, newcat):
        item_upc.delete(0, tk.END)
        item_name.delete(0, tk.END)
        item_desc.delete(0, tk.END)
        item_price.delete(0, tk.END)
        new_cate.delete(0, tk.END)
        if cat == "NEW":
            itemcatalog[newcat] = {}
            if upc != "":
                itemcatalog[newcat][upc] = {"Name" : name, "Description" : desc, "Price" : monies, "Quantity" : 0}
            pickle.dump(itemcatalog, open("master.dat", "wb"))
            for cats in itemcatalog:
                if cats not in getcats:
                    getcats.append(cats)
            ie_win.destroy()
            new_item_entry()
        else:
            itemcatalog[cat][upc] = {"Name" : name, "Description" : desc, "Price" : monies, "Quantity" : 0}
            pickle.dump(itemcatalog, open("master.dat", "wb"))
    #-----
            
    ie_win = tk.Tk()
    ie_win.title("New Item Entry")

    ie_win.resizable(False, False)
    tk.Canvas(ie_win, height=200, width=500).pack()

    action_frame = tk.Frame(ie_win, bg="#1b298f")
    action_frame.place(anchor="n", relx=0.5, rely=0.01, relwidth=0.99, relheight=0.98)
    
    upc_frame = tk.Frame(action_frame)
    upc_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    upc_label = tk.Label(upc_frame, text="ITEM UPC", width=15, anchor="w")
    upc_label.pack(side=tk.LEFT)
    item_upc = tk.Entry(upc_frame, justify="center")
    item_upc.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    item_upc.focus()

    iname_frame = tk.Frame(action_frame)
    iname_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=0)
    iname_label = tk.Label(iname_frame, text="ITEM NAME", width=15, anchor="w")
    iname_label.pack(side=tk.LEFT)
    item_name = tk.Entry(iname_frame, justify="center")
    item_name.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

    idesc_frame = tk.Frame(action_frame)
    idesc_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    idesc_label = tk.Label(idesc_frame, text="ITEM DESCRIPTION", width=15, anchor="w")
    idesc_label.pack(side=tk.LEFT)
    item_desc = tk.Entry(idesc_frame, justify="center")
    item_desc.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

    iprice_frame = tk.Frame(action_frame)
    iprice_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=0)
    iprice_label = tk.Label(iprice_frame, text="ITEM PRICE", width=15, anchor="w")
    iprice_label.pack(side=tk.LEFT)
    item_price = tk.Entry(iprice_frame, justify="center")
    item_price.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

    sv = tk.StringVar(action_frame)
    sv.set("NEW")
    icat_frame = tk.Frame(action_frame)
    icat_frame.place(anchor="n", relx=0.235, rely=0.8, width=225)
    icat_label = tk.Label(icat_frame, text="CATEGORY", width=10, anchor="w")
    icat_label.pack(side=tk.LEFT)
    item_cat = tk.OptionMenu(icat_frame, sv, "NEW", *getcats)
    item_cat.pack(side=tk.RIGHT)

    new_cate = tk.Entry(action_frame, justify='center')
    new_cate.place(anchor="s", relx=0.235, rely=0.79, width=225)

    remove_category = tk.Button(action_frame, width=25, text="Remove Category", command = lambda: remove_cat(sv.get(), item_upc.get()))
    remove_category.place(anchor="s", relx=0.8043, rely=0.77)

    submit_frame = tk.Frame(action_frame)
    submit_frame.place(anchor="n", relx=0.8043, rely=0.82)
    submit_item = tk.Button(submit_frame, width=25, text="Submit Item", command = lambda: add_new_item(sv.get(), item_price.get(), item_desc.get(), item_name.get(), item_upc.get(), new_cate.get()))
    submit_item.pack()

    ie_win.iconbitmap(icon)
    ie_win.mainloop()

#-----------------Main function screen
win = tk.Tk()
win.title("StoreFront IMS")

win.resizable(False, False)
tk.Canvas(win, height=158, width=250).pack()

action_frame = tk.Frame(win, bg="#1b298f")
action_frame.place(anchor="n", relx=0.5, rely=0.01, relwidth=0.99, relheight=0.98)

new_item = tk.Button(action_frame, text="New Item", command = lambda: new_item_entry())
new_item.pack(fill="x", padx=10, pady=10)

view_catalog = tk.Button(action_frame, text="Catalog", command = lambda: open_catalog())
view_catalog.pack(fill="x", padx=10, pady=0)

inventory_management = tk.Button(action_frame, text="Check-in", command = lambda: open_ci())
inventory_management.pack(fill="x", padx=10, pady=10)

qbooks = tk.Button(action_frame, text="Point of Sales", command = lambda: open_pos())
qbooks.pack(fill="x", padx=10, pady=0)

win.iconbitmap(icon)       
win.mainloop()
