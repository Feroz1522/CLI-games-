from art import logo,vs
from profile_data import data
import random

player_life = 1
player_score = 0

#random number for list
def list_number():
    random_number = random.randint(0,49)
    return random_number

#selecting profile from list
def profile_choosing():
    profile = data[list_number()]
    return profile

#Reducing player life 
def reducing_life():
    global player_life
    player_life -= 1 

#increasing player score
def increasing_score():
    global player_score
    player_score += 1
    return player_score

def check_greater(profile_a,profile_b):
    a = profile_a
    b = profile_b
    profile_1 = "a"
    profile_2 = "b"
    if a>b :
        return profile_1
    else :
        return profile_2

#main funciton
game_status = True 
while game_status:
    
    if player_life == 0:
        print(f"Your Final Score : {player_score}")
        print("Bye Mate")
        break
    
    if player_life >= 1 :
        print(logo)
        profile_a = profile_choosing()
        profile_b = profile_choosing()
        
        print(f"Compare A: {profile_a['name']} and his description {profile_a['description']} {profile_a['country']}. ")
        print(vs)
        print(f"Against B: {profile_b['name']} and his description {profile_b['description']} {profile_b['country']}. ")
        
        print(f"your score is {player_score}")
        guessed_answer = input("Who has more Followers? Type A or B : ").lower()
        greater_value = check_greater(profile_a['follower_count'],profile_b['follower_count']) 
        
        if greater_value == guessed_answer:
            increasing_score()
            print("You Won !" )
        else:
            reducing_life()
            print("you lost ")
