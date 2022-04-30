from player import *
from word import *

from console.console import *




class Game(object):
    def __init__(self, player_name) -> None:
        self.player = Player(player_name)
        self.word = Word("Game\Resources\words.txt")

    def check_player_guess(self, guess):
        if guess in self.word.secret_word:
            return True
        else:
            return False

    def update(self):
        pass

    def run(self):
        Console.game_start_message()
        Console.skip_line()
        
        self.word.start()

        while not self.player.lost and '_' in self.word.encrypted_word:
            Console.show_encrypted_word(self.word.encrypted_word)
            Console.show_tries_left(self.player.guess_left)

            Console.show_input_prompt("Digit a letter")

            guess = self.player.take_guess()

            if guess in self.word.secret_word:
                self.word.update(guess)
            else:
                self.player.erred_guess()
        
        if self.player.lost:
            Console.game_over_message(self.word.secret_word)
        else:
            Console.victory_message(self.player.name)


# Main
game = Game("Augusto")
game.run()