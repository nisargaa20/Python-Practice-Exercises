import random
import os

from game_data import data
from game_art import logo, vs

def clear():
   
    os.system('cls' if os.name == 'nt' else 'clear')

def assign():
    return random.choice(data)

def compare(p1, p2, user_input):
    sum1 = p1['follower_count']
    sum2 = p2['follower_count']
    max_follower = p1 if sum1 > sum2 else p2
    return max_follower['name'] == user_input

def play_higher_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing = True
        
        while still_guessing:
            clear()
            print(logo)
            person1 = assign()
            person2 = assign()
            
            if score > 0:
                person1 = person2
                person2 = assign()
                while person1 == person2:
                    person2 = assign()
            
            print(f"Name: {person1['name']}, Desc: {person1['description']}")
            print(vs)
            print(f"Name: {person2['name']}, Desc: {person2['description']}")
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")
            
            guess = input("Enter name of person with Higher Followers: ")
            
            if compare(person1, person2, guess):
                score += 1
            else:
                still_guessing = False
                
        play_again = input("Want to Play Again? (y/n): ").lower()
        
        if play_again == 'y':
            continue
        elif play_again == 'n':
            playing_game = False
            clear()
            print("Game Exited Successfully")
        else:
            playing_game = False
            print("Invalid Input Taken as no.")

want_to_play = input("Do you want to play Higher Lower? (y/n)\n").lower()
if want_to_play == 'y':
    clear()
    play_higher_lower()
elif want_to_play == 'n':
    print("Program Exit Successful.")
else:
    print("Invalid Input, Program Exited.")
