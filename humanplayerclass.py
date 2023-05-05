class HumanPlayer:
    """
    Initializes a human player that is a child of the Player class
    
    Attributes:
            name (str): The name of the human player
            status (str): The status of the human player
            inventory (set): The used words of the human player
    
    """
    def __init__(self, name, status, inventory= set()):
        self.name = name
        self.status = status
        self.inventory = inventory
        self.score = 0
        
    def __repr__(self):
        return f"Player {self.name} is currently {self.status}"
    
    def __getitem__(self):
        return f"Here are the words you used so far: {self.inventory}"
                
   
    def scoring(self, score):
       self.score += len(self.inventory)
       return f"Player {self.name} current score is {self.score}"
   
   
    
        