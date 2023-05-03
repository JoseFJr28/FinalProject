import random
import time 
"""
The following is a game called Concentration. You are able to play by yourself
or with the computer. The goal of the game is to name more object of the
category options. There are 4 modes: easy, intermediate, hard, and impossible.
"""

class Concentration:
    
    "This defines the game"
    def __init__(self, game, player_dict):
        self.game = game
        self.player_dict = player_dict
    
    """Decides which player/npc goes first, second, third, etc.
    It will be determined by choosing a number 1-10"""
    def take_turn(self, player_dict):
        return new_player_dict
    
    
    """Retursn a random number for the npc"""
    def npc_num(self, npc):
        return random(range(1,11))
    
    
    'Adds player to the game'
    def add_players(self, player_dict):
        return player_dict[self.name]
    
    
    def timer(self):
        '''
        This method controls the timer in the game 
        it gives the players a certain amount of time to make a guess
        '''
        limit = 45
        t1 = time.time()
        while time.time()- t1 < limit:
            if t1 <= limit: 
                Player = 1
            else: 
                t1 > limit
                elimination = player_dict.pop(Player)
                return f"You hestitated, {elimination} is eliminatined"
        
            

def player_words(self, player_words):
    '''
    This functions holds player words and keeps track of the guess made
    by all players 
    '''
    
    self.player_words = player_words
    player_words = {Player:[]} 
    
        
    