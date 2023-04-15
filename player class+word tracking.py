
 class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = set()

    def update_used_words(self, word):
        self.used_words.add(word)

    def is_eliminated(self, word):
        return word in self.used_words