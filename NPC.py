import random
from FinalCategoryListTesting2 import Categories
from concentrationskeleton import handicap_npc
"""
This is the computer class or NPC for short. It will set up the npc reaction for
the game of concentration. 

"""

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

    
    
    def npc_reader(self, category,mode):
        """
        Will read the file and from there will see what difficulty of the npc
        and return a list of the words the computer will know. The words will be
        chosen at random
        
        Args:
           mode(str): difficulty of the npc
            categorty(dict): This chosen category that will have the list of 
            words in that category
        Returns:
            A list of random words from the categories list of words
        """
        #This allows to go through how many answers we have in total
        length = 0
        for x in Categories:
            if x.lower() == category.lower():
                length += len(Categories.get(category))
        
        #This allows access the available words
        #Making sure that he doesn't go over the required amount of words to know
            brain_size = handicap_npc(mode)
            if len(self.head) != brain_size:
                newcount = 0
                final = []
    #Now as we go through the restricted number of words to know    
                while newcount < brain_size:
                    #we pick a random number from the size of the available words
                    pick = random.randrange(length)
    #Access the words the itself
                    for x in Categories.get(category):
    #We make sure the random number is the key we want and its not in the list and 
    #the word is not in the list( to prevent repeats) we add it
                        if x == pick and x not in final:
                            final.append(Categories[category][x])
                        else:
                            continue
                #prevents the infinite loop            
                    newcount += 1
                return final