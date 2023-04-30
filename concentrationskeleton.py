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
    
    
    def timer():
        start_time = time.time()
        response = time.time()
        time_lasp = start_time - response
        return time_lasp
        if time_lasp > avg_time():
            return f"You hestitated, {winner} wins"
        
            

def player_words():
    pass
    