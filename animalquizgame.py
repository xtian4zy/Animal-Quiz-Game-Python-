# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:05:40 2021

@author: Idemudia Christian Uwa
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from IPython.display import clear_output
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again""\n")
                
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
        
    
score = 0
qustion = {}
print("Guess the Animal")
guess1 = input("The first nonhuman mammal with a proven ability to keep a beat is? ""\n")
clear_output()
check_guess(guess1, "Sea Lion")
guess2 = input("Honeybees can flap their wings __ times per second? ""\n")
clear_output()
check_guess(guess2, "200")
guess3 = input("Reindeer eyeballs turn __ in winter to help them see at lower light levels? ""\n")
clear_output()
check_guess(guess3, "blue")
guess4 = input("The __ can only eat when its head is upside-down? ""\n")
clear_output()
check_guess(guess4, "flamingo")
guess5 = input("The __ is the only mammal that can fly.? ""\n")
clear_output()
check_guess(guess5, "bat")
guess6 = input("__ will selflessly help each other out? ""\n")
clear_output()
check_guess(guess6, "Parrots")
guess7 = input("Only the males are called __. Females are called Peahens. ""\n")
clear_output()
check_guess(guess7, "Peacock")
guess8 = input("__ can taste with their feet. ""\n")
clear_output()
check_guess(guess8, "Butterflies")
print("Your Score is "+ str(score))