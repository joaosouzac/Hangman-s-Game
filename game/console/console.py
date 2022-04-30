class Console(object):
    
    @staticmethod
    def skip_line():
        print("\n", end="")

    @staticmethod
    def game_start_message():
        print('Welcome to the Hangman\'s Game!')
        print('*******************************') 

    @staticmethod   
    def game_over_message(secret_word):
        print("Game Over!")
        print(f"The word was: {secret_word}")

    @staticmethod
    def victory_message(player_name):
        print(f"Congratulations, {player_name}! You won a fabulous prize: ")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    @staticmethod
    def show_encrypted_word(encrypted_word):
        print(f"{encrypted_word}") 

    @staticmethod
    def show_tries_left(guess_left):
        print(f"Guess left: {guess_left}")

    @staticmethod
    def show_input_prompt(input_message):
        print(f"{input_message}: ", end="")



