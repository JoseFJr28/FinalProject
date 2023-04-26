
class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = set()

    def update_used_words(self, word):
        self.used_words.add(word)

    def is_eliminated(self, word):
        return word in self.used_words
    
class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer")
        
    def choose_word(self, category, categories):
        return random.choice(categories[category])
    
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_word(self):
        return input(f"{self.name}, say a word: ").strip()
    