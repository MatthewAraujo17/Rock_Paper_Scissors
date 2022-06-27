"""This project is a game of Rock-Paper-Scissors with user playing  against a /
computer that generates its choice of rock, paper or scissor using a random 
number generator. The game is played until the player/computer wins 2 games.
"""

import random


def RockPaperScissor() -> None:
    computer_wins = 0
    guest_wins = 0    
    while computer_wins != 2 or guest_wins != 2: 
        computer_wins = computer_wins
        guest_wins = guest_wins
        random_number = random.randint(1, 3)
        computer_choice = ''  
        if random_number == 1:
            computer_choice = 'R'
        elif random_number == 2:
            computer_choice = 'P'
        else:
            computer_choice = 'S'
            
        user_choice = input("Rock(R)?, Paper(P)?, or Scissors(S)")
        
        if computer_choice == user_choice:
            print('Redo, you got the same!')
        elif computer_choice == 'S' and user_choice == 'P':
            print('Good Try!')
            computer_wins = computer_wins + 1
        elif computer_choice == 'P' and user_choice == 'S':
            print('Nice!')
            guest_wins = guest_wins + 1
        elif computer_choice == 'R' and user_choice == 'S':
            print('Good Try!')
            computer_wins = computer_wins + 1            
        elif computer_choice == 'S' and user_choice == 'R':
            print('Nice!')
            guest_wins = guest_wins + 1
        elif computer_choice == 'P' and user_choice == 'R':
            print('Good Try!')
            computer_wins = computer_wins + 1
        elif computer_choice == 'R' and user_choice == 'P':
            print('Nice!')
            guest_wins = guest_wins + 1            
                  
        if computer_wins == 2:
            print("You lost, better luck next time")
        elif guest_wins == 2:
            print("Congratulations! You won the game!")
            
    
RockPaperScissor()
  