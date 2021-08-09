import sys
import time

def play_game():
    play = input("Would you like to play a game with me? Yes or no? ")
    
    if str.lower(play) == 'y' or str.lower(play) == 'yes':
        print("\nExcellent!")
        print("---------------------------------------------------")
        from random import randint
        how_many_numbers_low = int(input("How difficult would you like this to be? Choose a low number!: "))
        how_many_numbers_high = int(input("Now choose a high number!: "))
        number_list = [how_many_numbers_low, how_many_numbers_high]
        low = number_list.index(min(number_list))
        high = number_list.index(max(number_list))
        if how_many_numbers_low > how_many_numbers_high:
            print("Looks like someone can't follow instructions... \nlet me rearrange those numbers for you!")
            cont_play = input("Are you ready to take me seriously and play? yes or no: ")
            if str.lower(cont_play) == "y" or str.lower(cont_play) == "yes":
                print("Alright let us continue!")
            else:
                print("That's what I thought. Come back when you're ready to play!")
                time.sleep(10)
                sys.exit()
        answer = randint(number_list[low], number_list[high])
        guessed = False
        guesses = 0
        print("I have chosen a random number between "  + str(number_list[low]) + " and " + str(number_list[high]) +"\nWhat number am I thinking of?")
        
        
        while not guessed:
            try:
                guess = int(input("\nPlease enter your guess. "))
                guesses += 1
            except:
                print("\nGibberish will get you nowhere. Please enter a valid number between "+ str(number_list[low]) + " and " + str(number_list[high]))
                continue            
            if guess == answer:
                print("\nYou've guessed it in " + str(guesses) + " tries. My number was {}.".format(answer),"Congrats!!!\n")
                guessed = True
                play_game()
                break
            elif guess in range(number_list[low],number_list[high]) and guess > answer:
                print("Lower.")                
                continue
            elif guess in range(number_list[low],number_list[high]) and guess < answer:
                print("Higher.")                
                continue
            else:
                print("\nSeriously. Pick a number between "+ str(number_list[low]) + " and " + str(number_list[high]))
        
        

    elif str.lower(play) == 'n' or str.lower(play) == 'no':
        print("\nOh, well. Goodbye!")
    else:
        print("\nThat is not a valid answer. Please try again.\n")
        play_game()
    

play_game()
