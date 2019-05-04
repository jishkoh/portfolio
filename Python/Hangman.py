from __future__ import print_function
import random
import colorama
from colorama import Fore, Back, Style

colorama.init()

# This is the list of words that will be used in the hangman game. They will
# be chosen at random and assigned to the variable "secret" 

secretwords = []

secretfile = open("secretwords.txt", "r")
filewords = secretfile.readlines()

for word in filewords:
    word = word.strip("\n")
    secretwords.append(word)
    
secretfile.close()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alreadyplayed = False
totalscore = 0
name = ""

def hangman_display(guessed, secret):
    
    ''' 

    <--- Hangman display function --->
    
    
    Takes arguments "guessed" and "secrets", which are both strings. 
    
    This function takes the "guessed" and "secret" strings and makes a 
    comparison as to which letters in the "guessed" string are in the "secret"
    string. If the guessed letters (represented by the variable "letter") are 
    in the secret string, that letter is appended to "displaylist", which keeps 
    track of the letters to display. If the guessed letter is NOT in the 
    "secret" string, a "-" is appended to the displaylist instead. If there is a
    space in the "secret string, the space is not replaced by anything, and 
    instead, a space is appended to the displaylist. After the letters of the 
    "secret" string have been iterated, a string called "displaystring" will 
    obtain the join()-ed list of "displaylist".
    
    This function returns "displaystring".

    '''
    
    displaylist = []
    
    for letter in secret:
        
        if letter in guessed:
            displaylist.append(letter)
        elif letter == " ":
            displaylist.append(letter)
        else:
            displaylist.append("-")
            
    displaystring = ''
    displaystring = displaystring.join(displaylist)
    
    return displaystring
    
def restart():
    
    ''' 

    <--- Game Restart Function --->
    
    
    This function takes no arguments.
    
    This function is called at the end of the game and asks the player if they
    would like to try again. If they say yes, the main game function is called
    again.
    
    This function returns no values, but calls the hangman() function.

    '''
    
    print(Fore.YELLOW)
    print("Your score is only saved when you quit the game.")
    restartin = raw_input(Fore.GREEN + "Do you want to restart? (Y/N) ")
    
    if "y" in restartin.lower():
        hangman()
        
    else:
        scoreboard = open("scoreboard.txt", "a+")
        scoreboard.write(name + ": " + str(totalscore) + "pts\n")
        print()
        print(Fore.WHITE + "Score saved.")
        scoreboard.close()
        
        print()
        scoredisp = raw_input(Fore.RED + "Would you like to see the \
scoreboard? (Y/N) ")

        if "y" in scoredisp.lower():
            print(Fore.CYAN)
            scoreboard = open("scoreboard.txt", "r")
            
            print(scoreboard.read())
            scoreboard.close()

    
def hangman():
    
    ''' 

    <--- Main Game Function (Hangman) --->
    
    
    This function takes no arguments.
    
    This is the main hangman function. In this function, the player goes into 
    a loop which allows them to make their guesses. The guess is put into the 
    variable "guessed", which becomes an argument in the display_list() 
    function. The loop then analyzes the result and makes sure that the input 
    is valid, then calls display_list(). The loop continues while tries is not
    0.
    
    This function returns no values, but calls restart() at the end.

    '''
    
    global alreadyplayed
    global totalscore
    global name
    
    score = 0
    
    if alreadyplayed == False:
    
        print(Fore.WHITE)
        print("Welcome to Computer Science Hangman!")
        print()
        name = raw_input("What is your name?: " + Fore.YELLOW)
        print(Fore.WHITE)
        print("Welcome, " + Fore.YELLOW + name + Fore.WHITE + "!")
        print()
        play = raw_input("Press enter to continue... ")

    maximumtries = 8
    tries = maximumtries
    recentguessed = ''
    guessed = ''
    secret = random.choice(secretwords)
    
    print(Fore.WHITE)
    print("<---- " + Fore.YELLOW + "WELCOME TO HANGMAN! "+Fore.WHITE+ "---->")
    print(Fore.YELLOW)
    print("How to play:")
    print(Fore.RED + "Type letters to guess them!")
    print("Type the secret word if you think you've got it!")
    print(Fore.BLUE)
    print("Your score is calculated by multiplying (tries left) by (length of \
the secret word).")
    print("Your scores are saved under your name ONLY when you quit the game.")
    print(Fore.YELLOW)
    print(hangman_display(guessed, secret))
    
    while tries > 0:
        
        print(Fore.GREEN)
        print("Guess the secret word!")
        print("Tries left = " + Fore.RED + str(tries))
        
        
        # developer mode
        #print()
        #print("Answer =", Fore.WHITE, secret)
        
        print(Fore.BLUE)
        recentguessed = raw_input("Type a letter or guess the word here: " \
+ Fore.WHITE)
        recentguessed = recentguessed.lower()
        
        if recentguessed == secret:
            
            print()
            print(Fore.YELLOW + "You got it!")
            break
        
        elif recentguessed == "":
            
            print()
            print("Please actually type something in, mate.")
            
        elif len(recentguessed) > 1:
            
            if recentguessed == recentguessed.upper():
                print()
                print("There's no need to yell.")
                
            if len(recentguessed) == len(secret):
                print()
                print("Seems incorrect to me.")
                
            elif len(recentguessed) > 3:
                print()
                print("There's no need to spam.")
                
            else:
                print()
                print("One letter at a time, please.")
                
            recentguessed = ""
            
        elif recentguessed not in alphabet:
            
            print()
            print("That's not even part of the alphabet...")
            
        elif recentguessed in guessed:
            
            print()
            print("You already guessed that.")
            tries = tries + 1
        
        elif recentguessed not in secret:
            
            print()
            print("Incorrect!")
            
        elif recentguessed in secret:
            
            print(Fore.CYAN)
            print("You got a letter!!")
            tries = tries + 1
        
        guessed = guessed + recentguessed
        print(Fore.YELLOW)
        print(hangman_display(guessed, secret))
        print()
        
        # Increment tries
        tries = tries - 1
        
        if "-" not in hangman_display(guessed, secret):
            
            print(Fore.YELLOW + "You Win!")
            break
    
    score = tries*len(secret)
    totalscore = score + totalscore
        
    if tries == 0:
        
        print("You lose!")

    print("*************************")
    
    
    print(Fore.RED)
    print("Points gained:" + Fore.WHITE, score)
    print(Fore.RED + name + "'s total score:" + Fore.WHITE, totalscore)
    alreadyplayed = True
    
    restart()
    
''' <---- Call game functions ----> '''

hangman()