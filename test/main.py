import tic_tac_toe


if __name__ == "__main__":
    continue_playing = True

    print("Welcome to Tic Tac Toe!!!")
    player1 = input("Enter the first player's name: ")
    player2 = input("Enter the second player's name: ")
    print("Nice! let's start ...")
    game = tic_tac_toe.game(player1, player2)
    
    while continue_playing:
        game.start()

        print("\nGame Over.\n")

        request = input("\n\nenter your command number:\n1. Continue playing\n2. Reset\n3. Quit\n")
        if request == "1":
            game.resetGame()
        elif request == "2":
            print("\n\nWelcome to Tic Tac Toe!!!")
            player1 = input("Enter the name of first player:")
            player2 = input("Enter the name of second player:")
            game = tic_tac_toe.game(player1, player2)
        else:
            print("Good Games;)")
            break
