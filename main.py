import random

#potential choices for the game of rock, paper, scissors
OPTIONS = ['rock', 'paper', 'scissors']

#dictionary with winning option as the key and losing option as the value
WINNERS_AND_LOSERS = {
    'paper':'rock', #paper beats rock
    'scissors':'paper', #scissors beats paper
    'rock':'scissors' #rock beats scissors
}

def random_option():
    '''Returns a random option from the list of potential options'''
    idx = random.randint(0,2)
    return OPTIONS[idx]

def pick_winner(player1, player2):
    '''Given two choices of rock, paper, and scissors, determines the winner based on the rules, hardcoded in the
    dictionary WINNERS_AND_LOSERS.'''
    if player2 == WINNERS_AND_LOSERS[player1]: #if player2's choice is the loser of player1's choice, player1 wins
        return player1
    elif player1 == WINNERS_AND_LOSERS[player2]: #if player1's choice is the loser of player2's choice, player2 wins
        return player2
    else: #otherwise, the two players must have chosen the same option, so no one wins
        return None

def is_valid_option(user_choice):
    '''Returns a boolean of whether or not the given string is in the list of options'''
    return user_choice in OPTIONS


def play_game():
    print("________________________________________________________________")
    print("         Welcome to the Rock, Paper, Scissors Simulator!")
    print("   Rules: Rock beats scissors, scissors beats paper, and paper beats rock.", '\n')

    rematch = 'yes'
    num_wins = 0
    num_losses = 0
    num_ties = 0

    while rematch != 'no':

        user_choice = input("Please enter your choice: ").lower()
        while not is_valid_option(user_choice):
            print("         Sorry, " + user_choice + " is not a valid option. Please enter rock, paper, or scissors to play!")
            user_choice = input("Please enter your choice (rock, paper, or scissors): ").lower()

        opponent_choice = random_option()
        print("     Your opponent chose: " + opponent_choice)

        winner = pick_winner(user_choice, opponent_choice)

        if winner == None:
            print("It's a tie!")
            num_ties += 1
        elif winner == user_choice:
            print("You win!! ")
            num_wins += 1
        else:
            print("You lose :(")
            num_losses += 1

        rematch = input('\n' + "Would you like to play again? [yes/no]").lower()
        print()

    print()
    print("Thanks for playing! Here's your record: ")
    print("     Wins: ", num_wins, " | ", "Ties: ", num_ties, " | ", "Losses: ", num_losses)
    print("________________________________________________________________")



play_game()