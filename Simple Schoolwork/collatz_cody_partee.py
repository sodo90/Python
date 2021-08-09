def collatz():
    target = False
    while not target:
        try:
            number = int(input("Give me a number! "))
            if number <= 0:
                print("Sorry the number must be greater than 0!")
                collatz()
        except:
            print("Hey, that doesn't seem like a number!")
            continue
        while not target:
            if number == 1:
                target = True
                print("Congo Rats! we have arrived at our destination! Our final number is: " + str(number))
                collatz()
                break
            elif number%2 == 0:
                if number != 1:
                    calc = number // 2
                    print(str(number) + " / 2 = " + str(calc))
                    number = calc 
            elif number%2 != 0:
                if number != 1:
                    calc = 3*number+1
                    print(str(number) + " * 3 + 1 = " + str(calc))
                    number = calc
        
collatz()

