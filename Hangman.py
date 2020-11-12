import time
print("-"*50)
name = input("\tWhat is your name?\n\t")
print ("\thello {}, Time to play Hangman".format(name))
print("-"*50)
time.sleep(1)
while True:    
    print ("\n\tStart Guessing, you have 15 chances!")
    time.sleep(0.5)
    # What level of Difficulty does the user wishes to play is being asked.
    n= input("\n\t{} choose level of difficult\n\t1.Beginner\n\t2.Intermediate\n\t3.Pro\n\t".format(name))
    
    if n == "1":
    	# For beginner the questions are from 0 - 3.
        print("\n\tselect a number from (0-3)")
        num = input("\n\t")
    elif n =="2":
    	# For beginner the questions are from 4 - 7.
        print("\n\tselect a number from (4-7)")
        num = input("\n\t")
    elif n =="3":
    	# For beginner the questions are from 8 - 10.
        print("\n\tselect a number from (8-10)")
        num = input("\n\t")
    # for x in range(1):
    	# Under each if statement their are clues for the particular number the player has choose 
    if num == "0":
        print("\n\tClue:Organisers...")
        word ="speckbit"
    elif num =="1":
        print("\n\tClue:Today ")
        word ="sunday"
    elif num == "2":
        print("\n\tClue:Today's event at Bengaluru..")
        word ="ind vs aus"
    elif num == "3":
        print("\n\tClue: who sets up business")
        word ="entrepreneur"
    elif num == "4":
        print("\n\tClue:current location")
        word ="microsoft mpr1"
    elif num =="5":
        print("\n\tClue: India is a ?")
        word = "republic"
    elif num == "6":
        print("\n\tClue:Ag = 47")
        word ="silver"
    elif num =="7":
        print("\n\tClue: He sat under a tree and discovered something...")
        word = "newton"
    elif num == "8":
        print("\n\tClue: Weak")
        word ="feeble"
    elif num == "9" :
        print("\n\tClue:Is a sneaky person who has tricks up his sleeve, not like a magician,\n\
            \tbut like someone who would steal your wallet or cheat at cards.")        
        word ="rouge"
    elif num =="10":
        print("\n\tClue:Realsed date: 22-sept-94\n\tIMDB rating:9.3/10\n\tdirector:Frank Darabont\n\tcast:tim roberts and morgan freeman")
        word = "the shawshank redemption"
    elif num >"10":
        exit()
    guess = ""
    # Each player gets 15 chances to guess the word
    turns = 15
    while turns > 0:         
        fail = 0             
        for char in word:      
            if char in guess:   
                print ("\t"+char)   
            else:
                print ("\n\t-")     
                fail += 1    

        if fail == 0:
            print("*"*50)        
            print ("\n\tYou Won :-)\n\t")
            print("*"*50)
            break            
        print("   ")
        choice = input("\n\tguess a character:") 
        guess += choice      
        # if guess goes wrong his/her chances reduces by one. 
        if guess not in word:  
            turns -= 1        
            print ("\n\tWrong")
            print ("\n\tYou have {} guesses left".format(turns)) 
            # if he/she has zero guessses left, its GameOver!
            if turns == 0:           
                print ("\n\tYou Lose :-<")
            
    break  
