# SPACE PYTHON
import random
balance=100
def startgame():
    Start_Game = input ("Would you like to Start Game? ")
    if Start_Game[0].lower() == "y":
        print ("Great")
        greet()
                
    elif  Start_Game[0][0].lower() == "n":
        endgame()
    else:
        print("Please write yes or no")
        endgame()

def greet():
    name = input("Hello! What is your name? ")
    print(f"hi {name}! you are given £100 to spend how you like") 
    print("You are given a various life decisions, try not to lose you money!")
    print("Your bank pin is 3333 to get your money out")
    lotto(100)

def endgame():
    print('GAME OVER')
    userEnd=input("play again? ")
    if userEnd[0].lower() == 'y':
        startgame()
    else:
        print('fine, dont play')

def cashmachine(pin,amount,balance): 
    if pin==3333:
         
        balance= balance-amount
        print(f"(taking £{amount} from your account. Your new balance is £{balance})")
        return balance   
    else:
        print('wrong pin')
        lotto(balance)
   
def lotto(balance):
    lottery = input("Do you want to spend £5 of your money on a lottery game? ")
    while balance>0:
    
        if lottery[0].lower()=="y":
            pin = int(input("Please enter your pin "))
            balance=cashmachine(pin, 5, balance)
            play_lotto(balance)      

        elif lottery[0].lower()=="n":
            balance=cashmachine(3333, 0, balance)
            dosomething(balance)  

        else:
            print("Please write yes or no next time ") 
            lotto(balance)

def play_lotto(balance):

    print ("Your numbers for today are: ")   
    lottery_numbers = list(range(1,31))
    random.shuffle(lottery_numbers)
    three_nums = lottery_numbers[:3]
    print(three_nums)
    gennums(three_nums,balance) 

def gennums(three_nums,balance):
    result = str(input ("Would you like today's results? "))
    if  result[0].lower() == ("y"):
        print ("Today's winning numbers are:")
        
        Correct_numbers = list (range(1,31))
        random.shuffle(Correct_numbers)
        three_winning = Correct_numbers[:3]
        print (three_winning)
        counter = 0
        for number in three_nums:
            if number in three_winning:
                counter += 1
        print ("You matched "+str(counter) +" numbers!")
        # prize = 0
        if counter==0:
            prize=0
            print ("You win £ "+str(prize))
            balance=cashmachine(3333,-prize, balance)
            lotto(balance)
        elif counter==1:
            prize=100
            print ("You win £ "+str(prize))
            balance=cashmachine(3333,-prize, balance)
            afterlotto(balance)
        elif counter==2:
            prize=400
            print ("You win £ "+str(prize))
            balance=cashmachine(3333,-prize, balance)
            afterlotto(balance)
            password_puzzle()            
        elif counter==3:
            prize=1000
            print ("You win £ "+str(prize))
            balance=cashmachine(3333,-prize, balance)
            gamecomplete()
        
      
    else:
        print ("Please enter 'yes/no'") 
        gennums(three_nums,balance)

def afterlotto(balance):
    options= input ("buy another one or do something with the money? a/d ")
    if options[0].lower()=="a":
        play_lotto(balance)
    elif options[0].lower()=="d":
        dosomething(balance)
    else:
        print("Either write 'a' or 'd'")
        afterlotto()

def pet_snake():
    while True:
        buy_snake = input ("You can afford a regular pet snake! To buy enter Y     ")
        if not buy_snake[0].lower() == ("y"):
            print ("Please enter Y     ")
            continue 
        else: 
            print ("Excellent. Which colour? RED or GREEN ")
            break 
    colour_snake = input()
    while colour_snake != ("red") and colour_snake != ("green"):
        print ("please choose red or green")
        colour_snake = input()
    if colour_snake == ("green"):
        print ("You have a green snake.")
        password_puzzle()
    if colour_snake == ("red"): 
        print ("You have a red snake. it bites you!")
        endgame()
def gamecomplete():
    print("CONGRATULATIONS, you completed the game!!")

def dosomething(balance):
    charity = int(input("How much of your money will you give to charity? £"))
    
    if charity==0:
        print("karma gets you")
        cashmachine(3333,20,balance)
        boat_seat=input("man or lady? Type M or L ")
        

        if boat_seat[0].lower()==("m"):
            print("man")
            code_puzzle() 

        elif boat_seat[0].lower()==("l"):
            input("lady")
            riddle()
        
    elif charity<5:
        print("thats not much, but something")
        cashmachine(3333,charity,balance)
        friend = input ("Do you want to meet you friends?")
        if friend[0].lower()=="y":
            print("yes")
            print("You got coronavirus for being too social! Go home!")
            endgame() 
        elif friend[0].lower()=="n":
            print("Being unsocial huh? ") 
            code_puzzle()

    elif charity<70:
        print("thank you")
        cashmachine(3333,charity,balance)

    elif charity>=100:
        print("holy fk")
        cashmachine(3333,charity,balance)
       
    else:
        print("put a number in zero or above")
        dosomething()   

def password_puzzle():
    print("the snake asks you a question")
    puzzle = input("Combine two strings to make the password: 'Which is the most common programming language' + 'the lowest common multiple of 5 and 7? ")
    if puzzle.lower() == ("python35"):
        print("Correct answer. You getthe snake. On the way back to the boat the guide falls down abottomless pit. You return to the boat nearby")
        gamecomplete()
    else:
        endgame()

def riddle():
    print("solve this riddle...")
    riddle=input("When was the last year that was the same upside down? ")
    if riddle==("1961"):
        print("""Woohoo! """)
        gamecomplete()
    else:
        print("wrong")
        lotto()

def code_puzzle():
    input("Here is the puzzle- # identify if a word has the same start and end letter!   press enter to continue")
    print("")
    print("word = 'randomword'")
    print("if ...")
    print("     print('Same start and end letter')")
    print("else:")
    print("     print('different start and end letter')")
    print("")
    answer=input("what should replace the '...' (exclude spaces!): ")
    if answer== "word[0]==word[-1]:":
        print("CORRECT!!")
        gamecomplete()
    else:
        print("WRONG!")
        lotto()

startgame()  