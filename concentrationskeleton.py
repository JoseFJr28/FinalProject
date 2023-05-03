import random
<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import csv
=======
import time 
>>>>>>> b220e78665792e45dcebded0a7b30b9fec488643
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
    
<<<<<<< HEAD
    'Writes the players score onto a csv file'
    def record_score(self, name, score, category):
        with open('leaderboard.csv', mode = 'a') as filepath:
            record = csv.writer(filepath, delimeter = ' ')
            record.writerow([self.name, self.score, self.category])
        
    'Displays leaderboard'
    def leaderboard(self):
        data = pd.read("leaderboard.csv")
        data = data["score" > 5]
        data = data.groupby("name")
        print(data)
        
    'Displays Score Distribution'
    def score_distribution(self):
        names = []
        scores = []
        categories = []
        
        with open(csv_filename, mode='r') as scores_file:
            score_reader = csv.reader(scores_file)
            for row in score_reader:
                names.append(row[0])
                scores.append(int(row[1]))
                categories.append(row[2])
                
        fig, ax = plt.subplots()
        ax.bar(names, scores)
        ax.set_xlabel('Names')
        ax.set_ylabel('Scores')
        ax.set_title('Scores by Category')
        ax.set_xticklabels(categories)
        plt.show()
        
        
        

    
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
        
            

<<<<<<< HEAD
def player_words(self, player_words):
    '''
    This functions holds player words and keeps track of the guess made
    by all players 
    '''
    
    self.player_words = player_words
    player_words = {Player:[]} 
    
