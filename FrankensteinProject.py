
while True:
    print('\n')
    print ('-'*80)
    print('Frankenstein - The Game'.title())
    print ("Welcome to Frankenstein! You are going to be Victor Frankenstein and encounter all the difficulties of life while following your passion.")
    print('\n')
    print('In the game you can only answer with "yes" or "no". If you write something else the whole game will restart and you will lose your progress.<3')
    print('\n')
    print ("You are an only child and you live in Geneva. You have a lovely family."   ) 
    print ('\n')
    anw1 = input("Do you want a sister?")
    print('\n')
    if anw1 == "yes":
        print ("Your family adopts a girl. She has blue eyes and blond hair. As the years are passing you fall in love with her.")
    elif anw1 == "no":
        print ("You don't have the right to vote. Your family adopts a girl. She has blue eyes and blond hair.  As the years are passing you fall in love with her.")
    else:
        print ("Invalid answer.")
        continue
    print ('\n')
    print('Time is passing and you grow up with passion to explore and learn new things. One day a friend of your father comes and tells you new things about science. You have the opportunity to go to university but your best friend cannot come with you.')
    print ('\n')
    anw2 = input("Will you go to The University of Ingolstadt?")
    if anw2 == "yes":
        print('\n')
        print("Ok. You go when you are 17 years old.")
    elif anw2 == "no":
        print ('\n')
        anw3 = input("Do you want to study law in the nearest university?")
        if anw3 == "yes":
            print ('\n')
            print("You go to The University of Geneva")
            print("You get into a bad social circle, start smoking, drinking and taking drugs and soon die because of a disease.")
            continue
            print('\n')
        elif anw3 == "no":
            print ('\n')
            anw4 = input("Do you want to start helping a local farmer?")
            if anw4 == "yes":
                print ('\n')
                print("This will be your new future.")
                print("The farmer soon dies and the farm is yours now.")
                print("You hire people to work for you and then go home.")
            elif anw4 == "no":
                print ('\n')
                print("You get so bored and tired of your life so you don't have any will to live. You commit suicide.")
                continue
                print('\n')
            else:
                print("Invalid answer.")
                continue
                print('\n')
        else:
            print ("Invalid answer.")
            continue
            print('\n')
    else:
        print("Invalid answer.")
        continue
    print ('\n')    
    print("Your mother catches scarlet fever and she dies.")
    print ('\n')
    anw5 = input("Will you be next to your sister?")
    if anw5 == "yes":
        print ('\n')
        print("You stay with your sister and as your mom wanted you propose to her and soon get married.")
        print ('\n')
        anw6 = input("Do you want children?")
        print ('\n')
        if anw6 == "yes":
            print("*3 years later* Now you have 2 children: a boy and a girl. You named them Jack and Anne.")
            print ('\n')
            anw7 = input("Your wife wants more kids, do you?")
            print ('\n')
            if anw7 == "yes":
                    print ('\n')
                    print("*5 years later* Now you have 6 children-Jack, Anne, Richard, Tom, Jane and Amelia.")
                    print("You spend the next 15 years taking care of your kids.")
                    print("One day when you are out to get the newspaper, you get shot by a mysterious figure standing across the street.")
            elif anw7 == "no":
                    print('\n')
                    print("She wants to leave you and take the children with her.")
                    anw8 = input("Will you try to stop her?")
                    if anw8 == "yes":
                        print('\n')
                        print("She listens to you and stays.")
                        print("One night she kills you while you are sleeping.")
                        continue
                        print('\n')
                    elif anw8 == "no":
                        print('\n')
                        print("You are alone now.")
                        print("You start drinking and smoking and after a couple of years you get a rare disease.")
                        print("Doctors are unable to save you so you die.")
                        continue
                        print('\n')
                    else:
                        print("Invalid answer.")
                        continue
                        print('\n')
            else:
                    print("Invalid answer.")
                    continue
                    print('\n')
        elif anw6 == "no":
            print("She says that she is going to kill herself because that means you don't love her anymore.")
            print('\n')
            anw9 = input("Do you love her?")
            if anw9 == "yes":
                print("She doesn't believe you. She stabs herself with a knive.")
                print("One afternoon while you are reading a book, you suddenly receive a heart attack and die.")
                continue
                print('\n')
            elif anw9 == "no":
                print("She gets angry. In a moment of insanity she stabs you exactly where your heart is and you die within a few minutes.")
            else:
                print("Invalid answer.")
                continue
                print('\n')
    elif anw5 == "no":
            print('\n')
            print("You go to the university of Ingolstadt.")
            print("You meet professor Krempe.")
            print("You talk to him and he says that you have wasted your time studying the alchemists.")
            print("You attend a chemistry lecture and decide that this will be your future.")
            print('\n')
    else:
            print("Invalid answer.")
            continue
            print('\n')    
    print("Years are passing and you study anatomy, death and decay.")
    print("You discover the secret of life.")
    print("You start working on creating a creature.")
    print("\n")
    print("*a few years later*")
    print("\n")
    print("One stormy night you complete your creature. You are terrified from his look and go to bed but have nightmares.")
    print("You get up in the morning and find the creature sitting on your bed smiling.")
    print('\n')
    anw10 = input("Will you run out of your home?")
    if anw10 == "yes":
        print("You go outside.")
        print("You walk down the streets for some time and then go to an inn.")
    elif anw10 == "no":
        print("The monster grabs you and eats you alive.")
        print("You die.")
        continue
    else:
        print("Invalid answer.")
        continue
        print('\n')
    print("Your best-friend Henry Clerval arrives.")
    print("He tells you that your family is well.")
    anw11 = input("Will you go home with him?")
    if anw11 == "yes": 
        print("You go home.")
        print("The monster isn't there.")
        print("You are happy.")
    elif anw11 == "no":
        print("You get drunk.")
        print("When you are walking home, a car hits you because you are in the middle of the street.")
        continue
    else:
        print("Invalid answer.")
        continue
        print('\n')
        
        
    




