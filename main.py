import random
import os
from art import logo
EASY_LEVEL_TURN=10
HARD_LEVEL_TURNS=5

def check(guess,answer,turns):
    
    if guess>answer:
        print("Too high!")
        return turns-1
    elif guess<answer:
        print("Too low!")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}.")     
def set():
    chosen_difficulty=input("Choose a difficulty.('e' for 'easy' and 'h' for 'hard')")
    if chosen_difficulty=='e':
        
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURNS    
def start():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100:")
    answer=random.randint(1,101)
    print(answer)
    turns=set()
    guess=0
    while guess!=answer and turns>0:
        print(f"You have {turns} attempts remaining to guess the number")
        guess=int(input("Make a guess:"))
        turns=check(guess,answer,turns)
        if turns==0:
            print("You've run out of guesses,you lose!")
            return
        elif guess!=answer:
            print("Guess again!")    
    os.system('cls')
start()