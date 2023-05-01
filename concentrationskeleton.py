import random
import pandas as pd
import matplotlib.pyplot as plt
import csv
"""
The following is a game called Concentration. You are able to play by yourself
or with the computer. The goal of the game is to name more object of the
category options. There are 4 modes: easy, intermediate, hard, and impossible.
"""

class Concentration:
    
    "This defines the game"
    def __init__(self, game, player_dict):
        pass
    
    
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
        
        
        