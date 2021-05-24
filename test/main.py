import tic_tac_toe
from player import player


if __name__ == "__main__":
    continue_playing = True

    print("Welcome to Tic Tac Toe!!!")
    player1 = player(input("Enter the first player's name: "))
    player2 = player(input("Enter the second player's name: "))
    print("Nice! let's start ...")
    game = tic_tac_toe.game(player1, player2)
    
    while continue_playing:
        player1.play_count += 1
        player2.play_count += 1
        game.start()

        print("\nGame Over.\n")
        if game.winner:
            game.winner.win_count += 1
            print(" **** " + game.winner.name + " won! ****")
        else:
            print(" **** It is a DRAW! ****")			
        print(player1.name + " has won " + str(player1.win_count) + " out of " + str(player1.play_count) + " games.")
        print(player2.name + " has won " + str(player2.win_count) + " out of " + str(player2.play_count) + " games.")

        request = input("\n\nenter your command number:\n1. Continue playing\n2. Reset\n3. Quit\n")
        if request == "1":
            game.resetGame()
        elif request == "2":
            print("\n\nWelcome to Tic Tac Toe!!!")
            player1 = player(input("Enter the name of first player:"))
            player2 = player(input("Enter the name of second player:"))
            game = tic_tac_toe.game(player1, player2)
        else:
            print("Good Games;)")
            break
