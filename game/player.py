from unicodedata import name


class Player(object):
    def __init__(self, name) -> None:
        self.name = name
        self.lost = False
        self.guess_left = 6
    
    def take_guess(self):
        return input().upper()

    def erred_guess(self):
        
        self.guess_left -= 1
        if self.guess_left <= 0:
            self.lost = True


# Test Area
