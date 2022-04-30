import random


class FileHandler(object):
    def __init__(self, filepath) -> None:
        self.file = open(filepath, 'r')

    def strip_file(self):
        content = []

        for line in self.file:
            line = line.strip()
            content.append(line)
        self.file.close()

        return content


class Word(object):
    def __init__(self, filepath) -> None:
        self.word_list = FileHandler(filepath).strip_file()
        self.secret_word = ""
        self.encrypted_word = ""
        
    def __draw(self):
        id = random.randrange(0, len(self.word_list))

        self.secret_word = self.word_list[id].upper()

    def __encrypt(self):
        encrypt = ['_' for letter in self.secret_word]

        self.encrypted_word = encrypt

    def start(self):
        self.__draw()
        self.__encrypt()
    
    def update(self, guess):
        for n in range(len(self.secret_word)):
            if guess.upper() == self.secret_word[n].upper():
                self.encrypted_word[n] = guess




# Test Area

""" f_handler = FileHandler("Game\Resources\words.txt")

word = Word()
word.start(f_handler.strip_file())

print(f"Secret Word: {word.secret_word}, Encrypted Word: {word.encrypted_word}") """


