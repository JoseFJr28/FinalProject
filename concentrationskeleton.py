import random
import sys
from argparse import ArgumentParser
from FinalCategoryListTesting2 import Categories
from testingConcentration import Player
import NPC

#################################
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time 
#################################

"""
The following is a game called Concentration. You are able to play by yourself
or with the computer. The goal of the game is to name more object of the
category options. There are 4 modes: easy, intermediate, hard, and impossible.
"""

class Concentration:
    
    """This defines the game"""
    def __init__(self, player_list):
        self.player_listt = player_list
        
    def start_game(self, player_list):
        game_order = self.order(player_list)
        [f"By the power invested in me this how the order of who goes first to last: {x} " for x in game_order]
        difficulty = input("Choose your mode? (Easy/Medium/Hard/Impossible)")
        
        category = input("Now choose a category? (Animals/Card Games/Training) ")
        game_state = self.npc_checker(game_order)
            
            
        
        
    def order(self, player_list):
        """
        How the order of the players will be determined, randomly
        Args:
            player_list(list of Players): the list of players, both human and/or npc
        Returns:
            An order list of who goes 1st, 2nd, 3rd, 4th, etc.
        """
        order = random.sample(player_list, k = len(player_list))
        return order

    def npc_checker (self, player_list):
        return True if "Sheldon" in player_list else False
    
    
    def reset_turns(self, player, player_list):
        """
        This resets the turn for each round
        Args:
            player(Instance of Player):
            player_list(list of Players): the list of players in current game
            
        """
        for player in player_list:
            if player.turn_indicator != False:
                player.turn_indicator = False 
            else:
                continue
        return player_list

    def take_turn(self, player, player_list):
        for player in player_list:
            if player.turn_indictor == False:
                continue #Here the player would take its turn by getting asked what belongs in that category
                #We call the timer function 
                #while timer: (while the timer doesn't reach zero)
                    #the player has that amount of time to put in his response
                    #if (the word is not under that category
                        #print('That word doesnt belong in the category)
                        #player_list[player].pop()
                    #elif word is in game.used_words:
                        #print('That word has already been used. You are elminated)
                        #player_list[player].pop()
            # else:
                # continue
        self.reset_turns(player, player_list)
    
    def handicap_npc(self, mode):
        """
        Will give a handicap to the NPC on how "smart" it is;
        Args:
            mode(str): The mode for the npc
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
        if mode.lower() == 'easy'.lower():
            return random.randrange(1,11)
        elif mode.lower() == 'medium'.lower():
            return random.randrange(1,20)
        elif mode.lower() == 'hard'.lower():
            return random.randrange(30,50)
        elif mode.lower() == 'impossible'.lower():
            return self.brain
        else:
            return f"That mode is not available" 
    
    def add_players(self, player_list, player):
        """
        Adds the current players in the game in a list
        Args:
            player_listt (list): list of players, mix of human and npc
            player (Instance of Player): 
        Side effects:
            adds to the players list
        """
        return player_list.append(player)
    
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
    
    
    # def timer(self):
    #     start_time = time.time()
    #     response = time.time()
    #     time_lasp = start_time - response
    #     return time_lasp
    #     if time_lasp > avg_time():
    #         return f"You hestitated, {winner} wins"
    #     else():
            # pass
    
    
def main():
    answer = input("Welcome To Concentration 64!!!! Ready to begin your journey of fun (Yes/No)?")
    if answer.lower() == 'Yes'.lower():
        print("Great! Lets begin!")
        print("""NOTE: If there is only 1 player in the game you will automatically have a computer player to go against.
              If you want to include a computer player just type npc""")
        player_count = int(input("How many players will be there? (1-4)"))
        if player_count == 1:
            player_name = input("What is your name? ")
            player1 = Player(player_name)
            npc_player = NPC(mode)
            Concentration.players_list.append(player1)
            Concentration.players_list.append(npc_player)
            print("Let the games begin")
            start_game(Concentration.players_list)
        elif player_count > 1:
            start = 0
            while start < player_count:
                player = input("What's your name? ")
                if player == 'npc':
                    new_npc = NPC(mode)
                    Concentration.players_list.append(new_npc)
                else:
                    Concentration.players_list.append(player)
                start += 1
            print("Let the games begin")
            start_game(Concentration.players_list)
        elif player_count > 4:
            print("Sorry! That is too many players. The game will crash now")
    elif answer.lower() == 'No'.lower():
        print("Okay! We tried :( Just know I could've beaten you with half my power!)")
    else:
        print("""So you don't know wha to say? Well I will say it for you. Thank You come again! \n
              Don't forget to leave a 5 star rating on Yelp""")


if __name__ == '__main__':
    main()

#this is where the leaderboard starts where Mo added
#Make sure to mention any pip installs
    'Writes the players score onto a csv file'
    def record_score(self, name, score, category):
        with open('leaderboard.csv', mode = 'a', encoding='utf-8') as filepath:
            record = csv.writer('leaderboard.csv', dialect='excel', delimeter = ' ')
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
    
