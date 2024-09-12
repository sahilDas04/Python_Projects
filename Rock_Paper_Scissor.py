import random

player_points = 0
computer_point = 0
choices = ('r', 'p', 's')

def player():
    global choices
    symbol = input("Chose the Rock(r), Paper(p), Scissor(s) : ").lower()
    if symbol not in choices:
        print("You did not enter the valid option")
        player()
    else:
        return symbol
    
def computer():
    return random.choice(choices)

def game():
    global player_points, computer_point
    
    players = player()
    computers = computer()
    
    print("\n player choice : ", players, "\n")
    print("\n Computer choice : ", computers, "\n")
    
    if(players == 'r' and computers == 's') or (players == 's' and computers == 'p') or (players == 'p' and computers == 'r'):
        print("Hurry ! Your win the match")
        player_points += 1
    
    else:
        print("Aww ! You lose the match")
        computer_point += 1

print("Welcome To Rock Paper Sciccor!!!")
while(True):
    for i in range(5):
        game()
    
    print("Thank you for your pricious time")
    print(f"\n Player Score {player_points}\n Computer Score {computer_point}")
    
    again = int(input("\n 1 To continue game \n 2 Reset and continue \n 3 Exit : "))
    if again == 1:
        continue 
    elif again == 2:
        player_points = 0
        computer_point = 0
        continue
    else:
        break