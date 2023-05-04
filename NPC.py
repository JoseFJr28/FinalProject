import random
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

    
    
    def npc_reader(self, category, brain):
        """
        Will read the file and from there will see what difficulty of the npc
        and return a list of the words the computer will know. The words will be
        chosen at random
        
        Ars:
            file(filepath): the vocab file
            brain(int): amount of words the computer will remember
            categorty(dict): This chosen category that will have the list of 
            wordsi n that category
        Returns:
            A list of random words from the categories list of words
        """
        with open(category, 'r', encoding='utf-8') as file:
        #This allows to go through how many answers we have in total
            length = 0
            for x in category.values():
                for y in x:
                    length +=1
        
        #This allows access the available words
        #Making sure that he doesn't go over the required amount of words to know
            if len(self.head) != self.brain:
                newcount = 0
                final = []
    #Now as we go through the restricted number of words to know    
                while newcount < self.brain:
                    #we pick a random number from the size of the available words
                    pick = random.randrange(length)
    #Access the words the itself
                    for x in file.values():
                        for y in x:
    #We make sure the random number is the key we want and its not in the list and 
    #the word is not in the list( to prevent repeats) we add it
                            if y == pick and x[y] not in final:
                                self.head.append(x[y])
                #prevents the infinite loop            
                    newcount += 1
                return final