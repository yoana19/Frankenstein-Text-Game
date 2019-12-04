
while True:
    print("\n")
    print('^'*80)
    print("\n")
    print("# Copyright 2018 Yoana Stankova")
    print('\n')
    print ('-'*80)
    print('Frankenstein - The Game'.title())
    print("\n")
    print ("Welcome to Frankenstein! You are going to be Victor Frankenstein and encounter all the difficulties of life while following your passion.")
    print('\n')
    print('In the game you can only answer with "yes" or "no". If you write something else the whole game will restart and you will lose your progress <3')
    print('\n')
    print ('^'*80)
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
                print("You live happy and peaceful life.")
                continue
                print("\n")
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
                    print("*5 years later*")
                    print("\n")
                    print("Now you have 6 children-Jack, Anne, Richard, Tom, Jane and Amelia.")
                    print("You spend the next 15 years taking care of your kids.")
                    print("One day when you are out to get the newspaper, you get shot by a mysterious figure standing across the street.")
                    continue
                    print("\n")
            elif anw7 == "no":
                    print('\n')
                    print("She wants to leave you and take the children with her.")
                    print("\n")
                    anw8 = input("Will you try to stop her?")
                    print("\n")
                    if anw8 == "yes":
                        print("She listens to you and stays.")
                        print("One night she kills you while you are sleeping.")
                        continue
                        print('\n')
                    elif anw8 == "no":
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
            print("\n")
            if anw9 == "yes":
                print("She doesn't believe you. She stabs herself with a knive.")
                print("One afternoon while you are reading a book, you suddenly receive a heart attack and die.")
                continue
                print('\n')
            elif anw9 == "no":
                print("She gets angry. In a moment of insanity she stabs you exactly where your heart is and you die within a few minutes.")
                continue
                print("\n")
            else:
                print("Invalid answer.")
                continue
                print('\n')
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
    print("    |--|--|--|--|--|     ")
    print("	   |    -     |   |     ")
    print("	   |  -        |  |     ")
    print("	   |   =      =   |     ")
    print("	    |  -  ||      |     ")
    print("	    |          - |      ")
    print("	    |   ------   |      ")
    print("	    |  -         |      ")
    print("	  ==|____________|==    ")
    print("\n")
    print("One stormy night you complete your creature. You are terrified from his look and go to bed but have nightmares.")
    print("You get up in the morning and find the creature sitting on your bed smiling.")
    print('\n')
    anw10 = input("Will you run out of your home?")
    print("\n")
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
    print("\n")
    anw11 = input("Will you go home with him?")
    print("\n")
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
    print("\n")
    print("You get ill.")
    print("Henry nurses you back to health and you recover.")
    print("Then he gives you a letter from Elizabeth.")        
    print("She expresses her concern about your illness and entreats you to write to your family in Geneva as soon as you can.")
    print("Then your father sends you a letter which says that your brother Williams is dead and your father begs you to go home.")
    print("\n")
    anw12 = input("Will you go back to your family?")
    print("\n")
    if anw12 == "yes":
        print("You go to Geneva.")
        print("You visit the place where your brother was found dead.")
        print("You see the monster in the near trees but it disappears.")
        print("\n")
    elif anw12 == "no":
        print("You continue working.")
        print("One day your neighbors find out about the creature and set your home on fire.")
        print("You die.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print('\n')
    anw13 = input("Will you tell everyone about the monster?")
    print("\n")
    if anw13 == "yes":
        print("Your family thinks that you have gone mad and sends you to a psychiatric hospital.")
        print("After a couple weeks, the man that you share room with, kills you in your sleep.")
        continue
        print("\n")
    elif anw13 =="no":
        print("You decide to keep it to yourself because no one will believe you.")
    else:
        print("Invalid answer.")
        continue
        print('\n')
    print("Everyone believes that the housemaid, Justine, killed your brother.")
    print("After a long trial, she is sentenced to death.")
    print("\n")
    anw14 = input("Will you go on a journey through the mountains?")
    print("\n")
    if anw14 == "yes":
        print("On one of the trips, you go into the valley of Chamonix.")
        print("You pass beautiful green fields, villages and rushed castles.")
        print("You spent the night in an inn.")
        print("\n")
    elif anw14 == "no":
        print("After a couple days, you die because of depression.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You decide to climb the mountain of Montanvert.")
    print("After some time, you find a shelter.")
    print("In the distance you see a huge figure coming towards you.")
    print("You realise this is your creature.")
    print("\n")
    anw15 = input("Will you attack the creature?")
    print("\n")
    if anw15 == "yes":
        print("You attack the creature multiple times.")
        print("This pisses him off and he takes off your head.")
        continue
        print("\n")
    elif anw15 == "no":
        print("The monster goes into the shelter.")
        print("At first, you refuse to go with him, but then you change your mind.")
        print("It starts telling you its story.")
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("The creature has suffered a lot.")
    print("It was chased by people and hurt.")
    print("It has found a cottage in the forest and has stayed in a pigsty.")
    print("The family that lived there was sad and the creature felt sad for them.")
    print("The monster has learnt a lot of things since it was created.")
    print("The family found out about it and decided to move out of the cottage.")
    print("The monster decided to travel to Geneva to find you in order to help him.")
    print("After killing your brother, the creature goes to the mountains.")
    print("The monster wants a female companion.")
    print("\n")
    anw16 = input("Will you create one for him?")
    print("\n")
    if anw16 == "yes":
        print("You agree to make a female for the creature.")
    elif anw16 == "no":
        print("The monster starts screaming and hits you on the head.")
        print("You fall and after a few minutes, you die.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You travel back home.")
    print("\n")
    anw17 = input("Will you travel to begin working on the female companion?")
    print("\n")
    if anw17 == "yes":
        print("You go to Strasbourg.")
        print("You meet your friend, Clerval.")
        print("\n")
    elif anw17 == "no":
        print("You stay home.")
        print("Soon you marry Elizabeth.")
        print("One night the monster comes and kills Elizabeth.")
        print("You are so sad and you decide to end the pain.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You start working on the second creature.")
    print("After a few weeks, you are nearly finished.")
    print("You see the monster standing in front of the window.")
    print("It is smiling.")
    print("\n")
    anw18 = input("Will you destroy the female monster?")
    print("\n")
    if anw18 == "yes":
        print("The creature says that it will ruin your life.")
        print("It disappears into the night.")
        print("\n")
    elif anw18 =="no":
        print("You bring the female monster to life.")
        print("The creature takes her.")
        print("She did not love him and he decided to come and kill you.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You friend, Clerval, sends you a letter, saying that he wants to meet you.")
    print("\n")
    anw19 = input("Will you go see him?")
    print("\n")
    if anw19 == "yes":
        print("You leave after two days.")
    elif anw19 == "no":
        print("The monster returns after a couple of months.")
        print("It grabs you and tears you into pieces.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You get on a boat alone and set off.")
    print("You sleep on the boat and the wind takes you away from the shore.")
    print("After many hours you see a land.")
    print("\n")
    anw20 = input("Will you go there?")
    print("\n")
    if anw20 == "yes":
        print("The people there are angry and they are waiting for you.")
    elif anw20 == "no":
        print("You continue to sail.")
        print("Soon a big shark turns the boat over and eats you alive.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You find out you are in Ireland.")
    print("A man tells you that you have to speak with Mr Kirwin.")
    print("You learn that a man was strangled last night.")
    print("People saw a boat like yours near the shore that night.")
    print("Mr Kirwin takes you to see the body.")
    print("The body belongs to your friend, Clerval.")
    print("\n")
    anw21 = input("Will you say that you are the murderer?")
    print("\n")
    if anw21 == "yes":
        print("You are sent to court.")
        print("You are sentenced to death.")
        print("You are hanged the next day.")
    elif anw21 == "no":
        print("You get sick for a couple months and you are put in a room in a prison.")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("Your father comes to visit you.")
    print("You are released from prison when you are proven to be innocent for the death of Clerval.")
    print("You leave Ireland.")
    print("Soon you arrive in Paris.")
    print("Elizabeth sends you a letter saying you may not love her anymore.")
    print("\n")
    anw22 = input("Will you write her back?")
    print("\n")
    if anw22 == "yes":
        print("You say that you will marry her as soon as possible.")
    elif anw22 == "no":
        print("Months are passing.")
        print("One day you receive a letter saying that Elizabeth has died.")
        print("The monster has kept its promise...")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You leave Paris.")
    print("After a few days you are home.")
    print("\n")
    print("*ten days later*")
    print("\n")
    print("You get married.")
    print("You take off on boat to hotel in Evian.")
    print("You go to an inn there and soon you sent Elizabeth to sleep.")
    print("\n")
    anw23 = input("Will you follow her?")
    print("\n")
    if anw23 == "yes":
        print("You start climbing the stairs.")
        print("You trip and fall.")
        print("You hit your head and die after a few minutes.")
        continue
        print("\n")
    elif anw23 == "no":
        print("You decide to look for the monster.")
        print("You hear a terrible scream, which is followed by a second one.")
        print("You rush into the room and see Elizabeth lying lifeless on the bed.")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("The monster is at the window and it is smiling at you.")
    print("It disappears into the lake.")
    print("You leave Evian.")
    print("Your father is heartbroken when you tell him what has happened.")
    print("\n")
    print("*time is passing*")
    print("\n")
    print("You find yourself in a prison cell because people think you have gone mad.")
    print("Soon you are released and you remember what has happened.")
    print("\n")
    anw24 = input("Will you talk to a judge?")
    print("\n")
    if anw24 == "yes":
        print("You tell him your story.")
    elif anw24 == "no":
        print("This time you really go mad and decide to end your life.")
        print("You drown in the nearest lake.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("He says that he will not be able to find the monster.")
    print("You leave his house filled with anger.")
    print("\n")
    anw25 = input("Will you leave Geneva?")
    print("\n")
    if anw25 == "yes":
        print("You get some money and leave.")
    elif anw25 == "no":
        print("You decide to kill the judge.")
        print("Soon you are found guilty and sentenced to death.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("You go to the cemetery where your relatives are buried.")
    print("You promise to kill the monster.")
    print("You hear an evil laugh from behind.")
    print("You go to the place where the sound came from but the creature is already gone.")
    print("\n")
    print("In the following months you are travelling around the world.")
    print("You are chasing the monster.")
    print("You go north and see the creature not far away from you on a sledge.")
    print("You are ill and cold.")
    print("You are rescued by men.")
    print("They take on a ship and take care of you.")
    print("\n")
    anw26 = input("Will you tell your story to the captain?")
    print("\n")
    if anw26 == "yes":
        print("You start telling him your story.")
        print("It takes you a week.")
    elif anw26 == "no":
        print("He gets mad.")
        print("He takes out his pistol and shoots you.")
        continue
        print("\n")
    else:
        print("Invalid answer.")
        continue
        print("\n")
    print("When you finish your story, you find out that he has been writing it.")
    print("You read the story and make some corrections to it.")
    print("You die peacefully...")
    print("\n")
    print("THE END")
    print("\n")
    print("RESOURCES")
    print("Frankenstein. SparkNotes, www.sparknotes.com/lit/frankenstein/. Accessed 1 June /n 2018.")
    print("Shelley, Mary. Frankenstein. ELI Publishing, 2009.")
    
    

    
    
    
    
            
        
    
        
    
        
    
    
    
    
            

    
    
        
        
    
   

        
    




