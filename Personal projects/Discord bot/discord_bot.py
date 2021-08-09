import discord
import os
from random import randint
from discord.utils import find
import keep_alive
import pickle


#global variables
client = discord.Client()


#Dictionaries
master = {}
#Loads the master DB
master = pickle.load(open("master.dat", "rb"))

#lists
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_", "A",
           "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
           "P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z", "/"]

npcletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_", "A",
              "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
              "P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z", "/", " "]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ,"0", "/"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("**FETCH...THE COMFY CHAIR!**".format(guild.name))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    #global  variable values
    global master
    

    #creates the server database
    if message.content.find('!new') != -1:
        master[str(message.author.guild)] = {}
        master[str(message.author.guild)]["chars"] = {}
        master[str(message.author.guild)]["initiative"] = {}
        master[str(message.author.guild)]["campaign"] = {}
        master[str(message.author.guild)]["ivalue"] = []
        master[str(message.author.guild)]["iname"] = []
        master[str(message.author.guild)]["dmdude"] = ""
        master[str(message.author.guild)]["locate"] = "none"
        master[str(message.author.guild)]["npc"] = "none"
        await message.channel.send("Server database created!")
        print(master)
        
    #roll the dice in 1d20+2 format
    if message.content.find('!r') != -1:
      roll = list(message.content)
      number_of_dice = ""
      bonus = 0
      sides = ""
      bonus_build = ""
      total_roll = 0
      individual_roll = ""
      for dnum in roll[2::1]:
          if dnum in numbers:
              number_of_dice += dnum
              del roll[roll.index(dnum)]
          if dnum in letters:
              break
      for dnum in roll[roll.index("d")::1]:
          if dnum in numbers:
              sides += dnum
              del roll[roll.index(dnum)]
          if dnum == "+":
              del roll[roll.index("d")]
              break
          if dnum == "-":
              del roll[roll.index("d")]
              break
      if "+" in roll:
          bonus_build = ""
          for bop in roll[roll.index("+")::1]:
                  for bnum in roll[roll.index("+")::1]:
                      if bnum in numbers:
                          bonus_build += bnum
                          del roll[roll.index(bnum)]            
          del roll[roll.index("+")]
      if "-" in roll:
          bonus_build = "-"
          for bop in roll[roll.index("-")::1]:
                  for bnum in roll[roll.index("-")::1]:
                      if bnum in numbers:
                          bonus_build += bnum
                          del roll[roll.index(bnum)]
          del roll[roll.index("-")]
      bonus = int(bonus_build)
      while number_of_dice > 0:
          if number_of_dice == 1:
              droll = randint(1, int(sides))
              individual_roll += str(droll) + " Bonus = " + str(bonus)
              total_roll += droll
              number_of_dice -= 1
          else:
              droll = randint(1, int(sides))
              individual_roll += str(droll) + " + "
              total_roll += droll
              number_of_dice -= 1
      total_roll += bonus   
      print("individual rolls: " + str(individual_roll))
      print("total roll: " + str(total_roll))
      print("dice sides: " + sides)
      print("how many dice: " + number_of_dice)
      print("proficiency bonus: " + str(bonus))
                  

    #adds a new character to the character dictionary    
    #sets character hp and max hp !chp
    if message.content.find('!chp') != -1:
        chpvalues = list(message.content)
        gname = str(message.author.guild)
        cname = ""
        curhp = ""
        maxhp = ""
        if chpvalues[-3] == " ":
          for alphabet in chpvalues[5:-3]:
            if alphabet in letters:
              cname += alphabet
          for hp in chpvalues[0:-3:1]:
            if hp in numbers:
              curhp += hp
          for hp in chpvalues[-3::1]:
            if hp in numbers:
              maxhp += hp
          master[gname]["chars"][cname] = {}
          master[gname]["chars"][cname]["Current HP"] = curhp
          master[gname]["chars"][cname]["Max HP"] = maxhp
          print("\n")
          print("character name: " + cname)
          print("\n")
          print("current hp: " + curhp)
          print("\n")
          print("max hp: " + maxhp)
          print("\n")
          print(master[gname]["chars"][cname])
          await message.channel.send(cname + " has been added to the character list! " + "\nMax HP: " + maxhp + "\nCurrent HP: " + curhp)
        if chpvalues[-2] == " ":
          for alphabet in chpvalues[5:]:
            if alphabet in letters:
              cname += alphabet
          for hp in chpvalues[0:-2:1]:
            if hp in numbers:
              curhp += hp
          for hp in chpvalues[-2::1]:
            if hp in numbers:
              maxhp += hp
          master[gname]["chars"][cname] = {}
          master[gname]["chars"][cname]["Current HP"] = curhp
          master[gname]["chars"][cname]["Max HP"] = maxhp
          print("\n")
          print("character name: " + cname)
          print("\n")
          print("current hp: " + curhp)
          print("\n")
          print("max hp: " + maxhp)
          print("\n")
          print(master[gname]["chars"][cname])
          await message.channel.send(cname + " has been added to the character list! " + "\nMax HP: " + maxhp + "\nCurrent HP: " + curhp)
        pickle.dump(master, open("master.dat", "wb"))
    
    
    #calls the character dictionary
    if message.content.find('!clist') != -1:
      await message.channel.send("Here is the character list for this campaign!")
      gname = str(message.author.guild)
      for k,v in master[gname]["chars"].items():
        character = k
        await message.channel.send("Character Name: " + str(character) + "\n" + "Max HP: " + str(master[gname]["chars"][character]["Max HP"]) + "\n" + "Current HP: " + str(master[gname]["chars"][character]["Current HP"]) + "\n\n\n")
    
    
    #Heals selected character
    if message.content.find('!heal') != -1:
      hvalue = list(message.content)
      gname = str(message.author.guild)
      cname = ""
      hpheal = ""
      for alphabet in hvalue[5:]:
        if alphabet in letters:
          cname += alphabet
      for hp in hvalue[5:]:
        if hp in numbers:
          hpheal += hp
      newhp = int(master[gname]["chars"][cname]["Current HP"]) + int(hpheal)
      if newhp > int(master[gname]["chars"][cname]["Max HP"]):
        newhp = int(master[gname]["chars"][cname]["Max HP"])
        updhp = str(newhp)
        master[gname]["chars"][cname]["Current HP"] = updhp
      else:
        updhp = str(newhp)
        master[gname]["chars"][cname]["Current HP"] = updhp
      await message.channel.send(cname + " has been healed for " + hpheal + " and now has " + updhp + " hitpoints!")
      print(hpheal)
      print(cname)
      print(updhp)
      print(master[gname]["chars"][cname]["Current HP"])
      pickle.dump(master, open("master.dat", "wb"))
  
    
    #damage selected character
    if message.content.find('!dmg') != -1:
      hvalue = list(message.content)
      gname = str(message.author.guild)
      cname = ""
      hpheal = ""
      for alphabet in hvalue[4:]:
        if alphabet in letters:
          cname += alphabet
      for hp in hvalue[4:]:
        if hp in numbers:
          hpheal += hp
      newhp = int(master[gname]["chars"][cname]["Current HP"]) - int(hpheal)
      if newhp < 0:
        newhp = 0
        updhp = str(newhp)
        master[gname]["chars"][cname]["Current HP"] = updhp
      else:
        updhp = str(newhp)
        master[gname]["chars"][cname]["Current HP"] = updhp
      await message.channel.send(cname + " has been hit for " + hpheal + " and now has " + updhp + " hitpoints!")
      print(hpheal)
      print(cname)
      print(updhp)
      print(master[gname]["chars"][cname]["Current HP"])
      pickle.dump(master, open("master.dat", "wb"))


    #add initiative to table
    if message.content.find('!initadd') != -1:
      inibonus = list(message.content)
      gname = str(message.author.guild)
      iniadd = ""
      iniroll = randint(1, 20)
      enttype = ""
      for alphabet in inibonus[8:]:
        if alphabet in letters:
          enttype += alphabet
      for bonus in inibonus[8:]:
        if bonus in numbers:
           iniadd += bonus
      if iniadd == "":
          iniadd = "0"
      if enttype == "p":
        enttype = message.author.name
      if "-" in inibonus[8:]:
          iniint = int(iniadd)
          totini = iniroll - iniint
      else:
          iniint = int(iniadd)
          totini = iniroll + iniint
      master[gname]["iname"].append(enttype)
      master[gname]["ivalue"].append(int(totini))
      print(master[gname]["iname"])
      print(master[gname]["ivalue"])
      await message.channel.send(enttype + " rolled: " + str(totini))
      pickle.dump(master, open("master.dat", "wb"))


    #call the initiative table by parsing iname and ivalue lists
    if message.content.find("!initiatives") != -1:
      await message.channel.send("Here is the initiative table for this fight! **!initr to reset initiative table**")
      gname = str(message.author.guild)
      intable = ""
      rmivalue = []
      rminame = []
      for i in master[gname]["ivalue"][0:]:
        indloc = master[gname]["ivalue"].index(int(max(master[gname]["ivalue"])))
        print(str(indloc))
        print(master[gname]["iname"][indloc] + ": " + str(master[gname]["ivalue"][indloc]))
        orderedinit = master[gname]["iname"][indloc] + ": " + str(master[gname]["ivalue"][indloc]) + "\n"
        intable += orderedinit
        rminame.append(master[gname]["iname"][indloc])
        rmivalue.append(master[gname]["ivalue"][indloc])
        del master[gname]["ivalue"][indloc]
        del master[gname]["iname"][indloc]
      await message.channel.send(intable)
      master[gname]["iname"] = rminame
      master[gname]["ivalue"] = rmivalue


    #resets the initiative table
    if message.content.find("!initr") != -1:
        gname = str(message.author.guild)
        master[gname]["iname"] = []
        master[gname]["ivalue"] = []
        await message.channel.send("Initiative table reset")
    
    
    #DM commands start here
    #sets the active dm
    if message.content.find("!imdm") != -1:
        gname = str(message.author.guild)
        setdm = list(message.content)
        changedm = message.author.name
        master[gname]["dmdude"] = changedm
        await message.author.send("You are now the DM...Give em hell!")


    #changes the campaign location
    if message.content.find("!dmloc") != -1:
      changeplace = list(message.content)
      runningloc = ""
      if dmdude == message.author.name:
        for alphabet in changeplace[7:]:
          if alphabet in npcletters:
            runningloc += alphabet
        locate = runningloc
        await message.author.send("You are now in: " + locate)
      else:
        await message.author.send("Hey! You're not the DM!")


    #changes the selected npc    
    if message.content.find("!dmnpc") != -1:
        changenpc = list(message.content)
        runningnpc = ""
        if dmdude == message.author.name:
            for alphabet in changenpc[7:]:
                if alphabet in npcletters:
                    runningnpc += alphabet
            npc = runningnpc
            await message.author.send("You are now editing: " + npc)
            await message.author.send(npc + ": \n" + camp[locate][npc]["Description"])
        else:
            await message.author.send("Hey! You're not the DM!")


    #creates a new campaign location
    if message.content.find("!dm_newloc") != -1:
      if dmdude == message.author.name:
        newplace = list(message.content)
        npname = ""
        for alphabet in newplace[11:]:
          if alphabet in npcletters:
            npname += alphabet
        locate = npname
        camp[locate] = {}
        print(locate)
        await message.author.send(locate + " has been created!")
      else:
        await message.author.send("Hey! You're not the DM!")
    
    
    #create a new NPC for the DM to reference inside the running location
    if message.content.find("!dm_newnpc") != -1:
      newnpc = list(message.content)
      create_npc = ""
      if dmdude == message.author.name:
        for alphabet in newnpc[11:]:
          if alphabet in npcletters:
            create_npc += alphabet
        npc = create_npc
        camp[locate][npc] = {}
        camp[locate][npc]["Description"] = {}
        await message.author.send(npc + " has been created!")
      else:
        await message.author.send("Hey! You're not the DM!")


    #edit selected npc
    if message.content.find("!dmedit") != -1:
        npcdesc = list(message.content)
        add_desc = ""
        if dmdude == message.author.name:
            for alphabet in npcdesc[8:]:
                if alphabet in npcletters:
                    add_desc += alphabet
            print(npc)
            print(locate)
            print(add_desc)
            camp[locate][npc]["Description"] = add_desc
            await message.author.send("Description for " + npc + " in " + locate + " has been changed!")
        else:
            await messag.eauthor.send("Hey! You're not the DM!")

    #used to force a save of the master DB before shutting down for maintenance and updates   
    if message.content.find("!save") != -1:
        if message.author.name == "Sodo":
            pickle.dump(master, open("master.dat", "wb"))
            await message.channel.send("Campaign data saved!")

    #used to load the master DB if it does not load automatically after a bot reboot
    if message.content.find("!load") != -1:
        if message.author.name == "Sodo":
            master = pickle.load(open("master.dat", "rb"))
            await message.channel.send("Campaign data loaded!")

    #flushes the server DB to reset the bot
    if message.content.find("!flush") != -1:
        if message.author.name == "Sodo":
            gname = str(message.author.guild)
            master = {}
            pickle.dump(master, open("master.dat", "wb"))
            await message.channel.send("This is why we can't have nice things!")

    #lists all the created locations
    if message.content.find("!loclist") != -1:
        if message.author.name == master[str(message.author.guild)]["dmdude"]:
            loclist = ""
            for k in camp:
                loclist += k + "\n"
                for things in camp[k]:
                    loclist += "    -" + things + "\n" 
            print(loclist)
            await message.author.send("Here is the location list you requested!\n" + loclist)


    if message.content.find("!help") != -1:
      await message.channel.send("!r - Roll the dice! **!r 1d20** *I CAN NOT ROLL MORE THAN 9 DICE AT A TIME FOR YOU!!! ....I have tiny hands*\n" +
      "!new - Creates all of the needed tables for the bot to function on your server \n" +
      "!chp - Adds characters to the character list **!chp Vonbrek 10 10** currentHP/maxHP \n" + 
      "!clist - Shows the list of characters\n" + 
      "!heal - Increases characters HP by value **!heal Vonbrek 10**\n" + 
      "!dmg - Lowers character hp by value **!dmg Vonbrek 10**\n" + 
      "!initadd - Adds a player or monster to the initiative table *to add yourself to the table* **!initadd character/monstername bonus**\n" + 
      "!initiatives - Displays the initiative table in order of action\n" +
      "!initr - Resets the initiative table for a new fight\n" +
      "!dmloc - changes the current location and prints NPCs created for that location\n" +
      "!dmnpc - changes the selected npc to allow changing of npc data\n" +
      "!dm_newloc - creates a new location dictionary to store created NPCs\n" +
      "!dm_newnpc - creates a new NPC dictionary within current location **must use !dmloc or !dm_locnew prior to creating an NPC**\n" +
      "!save - saves campaign data tables **only the DM can use this command**\n" +
      "!load - loads the saved campaign data tables **only the DM can use this command**\n" +
      "!flush - resets the campaign data tables **only the DM can use this command**\n")

                        
keep_alive.keep_alive()         
token = ""
client.run(token)
