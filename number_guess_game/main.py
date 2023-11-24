from art import *
import random
#ascii title art
print(title)
print("Welcome to the number Guessing game ")


while True:
    user_input = input("choose a difficulty : Type 'easy' or 'hard' ").lower()
    if user_input == 'easy':
        random_number = random.randint(1,100)
        print('easy player will have 10 attempts')
        player_attempts = 10
        if player_attempts == 0:
            break
        
        while player_attempts!=0:
            print("your attempts : ",player_attempts)
            player_input = int(input("guess number : "))
            if player_input == random_number:
                print("you won ")
                break
            if player_attempts == 0:
                print('attempts are overed')
                break
            if player_input < random_number:
                player_attempts -= 1
                print("too low.")
            if player_input > random_number:
                player_attempts -= 1
                print("too high")
    
    elif user_input == 'hard':
        random_number = random.randint(1,100)
        print('easy player will have 10 attempts')
        player_attempts = 5
        if player_attempts == 0:
            break
        
        while player_attempts!=0:
            print("your attempts : ",player_attempts)
            player_input = int(input("guess number : "))
            if player_input == random_number:
                print("you won ")
                break
            if player_attempts == 0:
                print('attempts are overed')
                break
            if player_input < random_number:
                player_attempts -= 1
                print("too low.")
            if player_input > random_number:
                player_attempts -= 1
                print("too high")
