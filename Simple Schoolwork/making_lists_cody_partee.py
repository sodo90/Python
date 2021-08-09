import pickle
import os


#Dictionary to store all todo lists and builds the cross references used to call them in list_select.
#indexvalue is updated within main() when a new list is created. This keeps the indexes synced when the list of lists is printed on screen
#when compared to the key in the "indexes" dictionary.
master_list = {}
master_list["lists"] = {}
master_list["indexes"] = {}
indexvalue = 1
load = False


#Checks for the required data files if they exist and have the above variables inside of them they are loaded.
#If the data files used cannot be loaded they are created with the above values and then loaded.
#The program then exits the loop and continues on to call the main() function.
while not load:
    try:
        indexvalue = pickle.load(open("indexes.dat", "rb"))
        master_list = pickle.load(open("master.dat", "rb"))
        load = True
    except:
        pickle.dump(indexvalue, open("indexes.dat", "wb+"))
        pickle.dump(master_list, open("master.dat", "wb+"))
        continue


#Handles list actions for active list selected in list_select
def list_action(selected_list):
    global indexvalue
    action_name = ""
    newindexvalue = 1
    action = False
    os.system("cls")
    while not action:
        print("\n\n\n")
        print("-----------------------------------------------------------")
        print(selected_list + " is now the active list!")
        print("-----------------------------------------------------------")
        what_to_do = str(input("What would you like to do? Add, Edit, Remove, View, Back, or Delete " + selected_list + ": "))
        action_name = what_to_do


        #Deletes the active list, rebuilds the index dictionary to keep it in sync, and then returns to main
        if str.lower(action_name) == "delete " + str.lower(selected_list):
            try:
                os.system("cls")
                delaction = str(input("Are you sure you want to delete " + selected_list + "? Yes or No: "))
                if str.lower(delaction) == "yes" or str.lower(delaction) == "y":
                    del master_list["lists"][selected_list]
                    master_list["indexes"] = {}
                    newindexvalue = 1
                    for k in master_list["lists"]:
                        master_list["indexes"][str(newindexvalue)] = str(k)
                        newindexvalue += 1
                    indexvalue = newindexvalue
                    pickle.dump(master_list, open("master.dat", "wb"))
                    pickle.dump(indexvalue, open("indexes.dat", "wb"))   
                    main()
                else:
                    continue
            except:
                print("The correct format is: delete " + selected_list)
                continue

                
        #Appends a new item into the active list
        if str.lower(action_name) == "add":
            try:
                os.system("cls")
                to_do = str(input("Add something to " + selected_list + ": "))
                if str.lower(to_do) == "":
                    continue
                else:
                    master_list["lists"][selected_list].append(to_do)
                    print(to_do + " --- has been added to " + selected_list)
                    pickle.dump(master_list, open("master.dat", "wb"))
            except:
                print("Something went wrong try again!")
                continue

        
        #Allows the user to overwrite a selected item in the active list
        if str.lower(action_name) == "edit":
            try:
                os.system("cls")
                listitem = 1
                print("-----------------------------------------------------------")
                for v in master_list["lists"][selected_list]:
                    print(str(listitem) + ": " + v)
                    listitem += 1
                print("-----------------------------------------------------------")
                listitem = int(input("Select the list item you want to overwrite: ")) - 1
                print("Editing --- " + master_list["lists"][selected_list][listitem])
                changetext = str(input("Enter your new item: "))
                if str.lower(changetext) == "":
                    continue
                else:
                    master_list["lists"][selected_list][listitem] = changetext
                    pickle.dump(master_list, open("master.dat", "wb"))
            except:
                print("Something went wrong try again!")
                continue

        
        #Removes a selected item from the active list
        if str.lower(action_name) == "remove":
            try:
                os.system("cls")
                listitem = 1
                print("-----------------------------------------------------------")
                for v in master_list["lists"][selected_list]:
                    print(str(listitem) + ": " + v)
                    listitem += 1
                print("-----------------------------------------------------------")
                listitem = int(input("Select the list item you want to remove: ")) - 1
                if listitem == "":
                    continue
                else:
                    print(master_list["lists"][selected_list][listitem] + " --- has been marked off the list!")
                    del master_list["lists"][selected_list][listitem]
                    pickle.dump(master_list, open("master.dat", "wb"))
            except:
                print("Something went wrong try again!")
                continue


        #Shows all items on the active list
        if str.lower(action_name) == "view":
            try:
                os.system("cls")
                listitem = 1
                print("Here is the list you requested! --- " + selected_list)
                print("-----------------------------------------------------------")
                for v in master_list["lists"][selected_list]:
                    print(str(listitem) + ": " + v)
                    listitem += 1
                print("-----------------------------------------------------------")
                pickle.dump(master_list, open("master.dat", "wb"))
            except:
                print("Something went wrong try again!")
                continue

        
        #Calls the main function allowing the user to create more lists or select a new list to view or edit
        if str.lower(action_name) == "back":
            try:
                os.system("cls")
                main()
            except:
                print("Something went wrong try again!")
                continue


#Select a list to modify
def list_select():
    selection = False
    while not selection:
        try:
            index_select = int(input("Select the index value of the list you want to edit: "))
            list_choose = master_list["indexes"][str(index_select)]
            list_action(list_choose)
            selection = True  
        except:
            print("Something went wrong try again!")
            main()
            selection = True
    
       
#Creates new lists within the "lists" dicitonary and creates index entries in the "indexes" dictionary
def main():
    global indexvalue
    global master_list
    makelist = True
    todo_name = ""
    while makelist == True:
        makeindex = str(indexvalue)
        try:
            newlist = input("Would you like to make a new list? Yes or No: ")
            if str.lower(newlist) == "yes" or str.lower(newlist) == "y":
                os.system("cls")
                todo_name = input("Enter the name for your list: ")
                if str.lower(todo_name) == "":
                    os.system("cls")
                    continue
                else:
                    master_list["lists"][todo_name] = []
                    master_list["indexes"][makeindex] = todo_name
                    indexvalue += 1
                    pickle.dump(indexvalue, open("indexes.dat", "wb"))
                    pickle.dump(master_list, open("master.dat", "wb"))

                    
            #Prints the list of lists you have created and calls the list_select function
            elif str.lower(newlist) == "no" or str.lower(newlist) == "n":
                makelist = False
                findindex = 1
                print("Select a list to view and edit using the index number")
                print("-----------------------------------------------------------")
                for k in master_list["lists"]:
                    print(str(findindex) + ": " + str(k))
                    findindex += 1
                print("-----------------------------------------------------------")

                
            #Resets the data files to a clean slate !!!intentionally hidden from the user!!!
            elif str.lower(newlist) == "flush":
                master_list = {}
                master_list["lists"] = {}
                master_list["indexes"] = {}
                indexvalue = 1
                pickle.dump(indexvalue, open("indexes.dat", "wb"))
                pickle.dump(master_list, open("master.dat", "wb"))
        except:
            print("Something went wrong try again!")
            continue

            
    list_select()
    

main()


