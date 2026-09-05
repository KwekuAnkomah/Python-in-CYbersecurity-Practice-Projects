import random

rounds_to_play = 3
valid_choices = ["rock","paper","scissors"]

print("#*#"* 20)
print("PLAY THE GAME")
print("Press 'Q' To Quit The Game!")
print("%"*20)
play_again = "y"

while play_again == "y":

    rounds_played = 0
    player_score = 0
    computer_score = 0
    won = False
    tie = False
    quit_game = False

    while True:
        if rounds_played < rounds_to_play:
            user_input = input("Enter Choice(R/P/S): ")
            game_signs = random.choice(["Rock","Paper","Scissors"])
            if user_input.lower() == "q":
                print("Bye...")
                quit_game = True
                break
            elif user_input.lower() not in valid_choices:
                print("Input Error!")
            elif user_input.lower() == "rock" and game_signs.lower() == "scissors":
                print(f"You Won! {user_input} > {game_signs}")
                player_score += 1
                print(f"Player: {player_score} - Computer: {computer_score}")
                rounds_played += 1
            elif user_input.lower() == "scissors" and game_signs.lower() == "paper":
                print(f"You Won! {user_input} > {game_signs}")
                player_score += 1
                print(f"Player: {player_score} - Computer: {computer_score}")
                rounds_played += 1
            elif user_input.lower() == "paper" and game_signs.lower() == "rock":
                print(f"You Won! {user_input} > {game_signs}")
                player_score += 1
                print(f"Player: {player_score} - Computer: {computer_score}")
                rounds_played += 1
            elif user_input.lower() == game_signs.lower():
                print(f"Tie! {user_input} = {game_signs}")
                print(f"Player: {player_score} - Computer: {computer_score}")
                rounds_played += 1
            else:
                print(f"You Lost! {user_input} < {game_signs}")
                computer_score += 1
                print(f"Player: {player_score} - Computer: {computer_score}")
                rounds_played += 1
        elif rounds_played == rounds_to_play and player_score > computer_score:
            won = True
            break
        elif rounds_played == rounds_to_play and player_score < computer_score:
            won = False
            break
        elif rounds_played == rounds_to_play and player_score == computer_score:
            tie = True
            break

    if quit_game:
        break  # exit the OUTER loop too, skip everything else below

    if won:
        print("You Won The Game!!!")
        print(f"{player_score} - {computer_score}")
    elif tie:
        print("ITS A TIE!!!")
        print(f"{player_score} - {computer_score}")
    elif won == False:
        print("You Lost The Game!!!")
        print(f"{player_score} - {computer_score}")

    play_again = input("Play? (y/n): ")
    if play_again.lower() == "n":
        print("Bye")
        break
    else:
        continue