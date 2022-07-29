import random

def compare(my_ans, com_choice): # To compare the result of user & computer's choice
    result = None
    # condition for draw
    if my_ans == com_choice:
        result = "DRAW"
    # condition for lost
    elif (my_ans == "rock" and com_choice == "paper") or (my_ans == "paper" and com_choice == "scissor") or (my_ans == "scissor" and com_choice == "rock"):
        result = "LOST"
    # condition for win
    elif (my_ans == "paper" and com_choice == "rock") or (my_ans == "scissor" and com_choice == "paper") or (my_ans == "rock" and com_choice == "scissor"):
        result = "WON"
    return result

# Program starts from here
game = ["rock", "paper", "scissor"]
while True:
    my_ans = input("\nENTER YOUR CHOICE (rock/paper/scissor): ")
    my_ans = my_ans.lower()
    if my_ans == "rock" or my_ans == "paper" or my_ans == "scissor": # To ensure the user enters correct string
        #generate random choice from the list
        computer_choice = random.choice(game)
        print(f'\n\nYOUR CHOICE = {my_ans}')
        print(f'COMPUTER\'S CHOICE = {computer_choice} \n\n')
        #compare the user's and computer's choice
        result = compare(my_ans,computer_choice)
        if result.lower() == "won":
            print(f'YAY! YOU {result}\n')
            break
        elif result.lower() == "lost":
            print(f'YOU {result}\n')
            continue
        else:
            print(f'THE GAME IS A {result}\n')
            continue          
    else:
        print(f'YOU ENTERED WRONG KEYWORD\nPLEASE TRY AGAIN')
        continue