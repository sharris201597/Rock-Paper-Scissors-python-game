import random

#Gets Random Number Function


# goal to return a "String (rock, paper, OR scissors"
def comp_answer():
    answer_lst = ["rock", "paper", "scissors"]
    return answer_lst[random.randrange(3)]


#Gets Player input
# goal to return player input back as a string in lowercase form
def player_input():
    player_choice = input(
        "What Do you want to play?(Rock, Paper, or Scissors):")
    player_cho = player_choice.strip().lower()


#Decides who wins
#goal to decide who wins and update counter and print who won with updated counter


def decider():
    #Counters
    player_counter = 0
    computer_counter = 0
    while True:
        player_yes_no = input(
            "Do you want to play rock paper scissors?(Yes/No)")
        player_while = player_yes_no.lower().strip()
        if player_while == "no":
            break
        while player_while == "yes":
            player_choice = input(
                "What Do you want to play?(Rock, Paper, or Scissors):")
            player_cho = player_choice.strip().lower()
            computer_locked = comp_answer()
            if player_cho == "quit":
                print("Thanks for playing!")
                break
            #player input = rock
            if player_cho == "rock" and computer_locked == "rock":
                print("It is a draw try again")
            elif player_cho == "rock" and computer_locked == "paper":
                print("You lost.")
                computer_counter += 1
            elif player_cho == "rock" and computer_locked == "scissors":
                print("You Win!")
                player_counter += 1
            #player input = paper
            elif player_cho == "paper" and computer_locked == "paper":
                print("It is a draw try again")
            elif player_cho == "paper" and computer_locked == "scissors":
                print("You lost.")
                computer_counter += 1
            elif player_cho == "paper" and computer_locked == "rock":
                print("You Win!")
                player_counter += 1
            #player input = scissors
            elif player_cho == "scissors" and computer_locked == "scissors":
                print("It is a draw try again")
            elif player_cho == "scissors" and computer_locked == "rock":
                print("You lost.")
                computer_counter += 1
            elif player_cho == "scissors" and computer_locked == "paper":
                print("You Win!")
                player_counter += 1
            else:
                print("Please enter a valid input.")
            print(
                f"Your Score Is {player_counter} and the computer score is {computer_counter}"
            )


decider()

#counter updater
#player_counter += 1
#computer_counter += 1


