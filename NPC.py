"""
This is the computer class or NPC for short. It will set up the npc reaction for
the game of concentration. 

"""

import random

class NPC:
    """
    
    Attributes:
        mode (str): The difficulty of the the npc
        npc_name(str): the name of the computer, default value of Sheldon
        score(int): the score for the npc
    """
    def __init__(self, mode, score, npc_name= "Sheldon"):
        """
        Initilizes the mode the computer will be in
        
        Args:

        """
        self.score = score
        self.mode = mode
        self.npc_name = "Sheldon"
        self.head = []
    
    
    def __repr__(self):
        """
        This will print out hte NPC name and provide the current score 
        """
        return f"Current mode for NPC {self.npc_name} is {self.mode}"

    def handicap_npc(self, dict, brain):
        """
        Will give a handicap to the NPC on how "smart" it is;
        Args:
            mode(str): The difficulty for the npc
            dict(dictionary of list): a dictionary of list with the categories
            brain(int)= the amount of words it can remember
        Returns:
            if self.mode == lower("easy") and word_count >= 20 and word_count <= 30:
                return brain = random(1,11)
            elif  self.mode == lower("intermediate") and word_count > 30 and word_count <= 50:
                return brain = random(1, 20)
            elif self.mode == lower("hard") and word_count > 50 and word_count <= 100:
                return brain = random(30, 50)
            else:
                return brain = word_count
        """
        pass
    
    def npc_reader(self, filepath, difficulty, brain):
        """
        Will read the file and from there will see what difficulty of the npc
        and return a list of the words the computer will know. The words will be
        chosen at random
        Ars:
            file(filepath): the vocab file
            difficulty(str): the mode of npc
            brain(int): amount of words the computer will remember
        Returns:
            A list of random words from the categories list of words
        """
        pass

        
                    
    
    
            
            
        