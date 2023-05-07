import random
from argparse import ArgumentParser
from alphatestingcategorieslist import Categories
from TrainingClass import Training
#################################

#################################
class Player:
    """
    This initilizes what a player consit of
    Attributes:
        name(str): The name of the player
        
    
    """
    def __init__(self, name, turn_indicator):
        self.name = name
        self.turn_indicator = turn_indicator
        self.used_words = set()
        
    def __repr__(self):
        return f'{self.name}'


"""
The following is a game called Concentration. You are able to play by yourself
or with the computer. The goal of the game is to name more object of the
category options. There are 4 modes: easy, intermediate, hard, and impossible.
"""

class Concentration:
    
    """This defines the game"""
    def __init__(self):
        self.player_list = []
        
    def start_game(self, player_list):
        #This is the order of the game
        game_order = self.order(player_list)
       
       #Player gets to decide 
        difficulty = input("Choose your mode? (Easy/Medium/Hard/Impossible)")
        if difficulty.lower() == "Impossible".lower():
            Training()
        elif 
        
        category = input("Now choose a category? (Animals/Card Games/Training) ")
        game_state = self.npc_checker(game_order)
              
    def current_players(self, player_list):
        """
        Shows the current players in the game
        Args:
            player_list(list of players): list of players
        Return:
            the current players of the game
        """
        return f'The current players are still in the game: {player_list}'
        
        
    def order(self, player_list):
        """
        How the order of the players will be determined, randomly
        Args:
            player_list(list of Players): the list of players, both human and/or npc
        Returns:
            An order list of who goes 1st, 2nd, 3rd, 4th, etc.
        """
        player = len(self.player_list)
        order = random.sample(self.player_list, k = player)
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
    
    
    def add_players(self,player):
        """
        Adds the current players in the game in a list
        Args:
            player_listt (list): list of players, mix of human and npc
            player (Instance of Player): 
        Side effects:
            adds to the players list
        """
        self.player_list.append(player)

class NPC:
    """
    
    Attributes:
        mode (str): The difficulty of the the npc
        npc_name(str): the name of the computer, default value of Sheldon
        score(int): the score for the npc
    """
    def __init__(self, mode, npc_name= "Sheldon"):
        """
        Initilizes the mode the computer will be in
        
        Args:

        """
        self.mode = mode
        self.npc_name = "Sheldon"
        self.head = []
    
    
    def __repr__(self):
        """
        This will print out hte NPC name and provide the current score 
        """
        return f"Current mode for NPC {self.npc_name} is {self.mode}"   
    
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
            
        else:
            return f"That mode is not available"        

    
    
    def npc_reader(self, category,mode):
        """
        Will read the file and from there will see what difficulty of the npc
        and return a list of the words the computer will know. The words will be
        chosen at random
        
        Ars:
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
            brain_size = self.handicap_npc(mode)
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
            
    
def main():
    new_game = Concentration()
    answer = input("Welcome To Concentration 64!!!! Ready to begin your journey of fun (Yes/No)? ")
    if answer.lower() == 'Yes'.lower():
        print("Great! Lets begin!")
        print("""NOTE: If there is only 1 player in the game you will automatically
        have a computer player to go against. If you want to include a computer player just type npc""")
        player_count = int(input("How many players will be there? (1-4) "))
        if player_count == 1:
            player_name = input("What is your name? ")
            player1 = Player(player_name)
            difficulty = input("what mode would you prefer to play? (Easy/Medium/Hard/Impossible) ")
            npc_player = NPC(difficulty)
            new_game.add_players(player1)
            new_game.add_players(npc_player)
            print("Let the games begin")
            new_game.start_game(new_game.players_list)
        elif player_count > 1 and player_count <= 4:
            start = 0
            while start < player_count:
                player = input("What's your name? ")
                if player == 'npc':
                    difficulty = input("what mode would you prefer to play? (Easy/Medium/Hard/Impossible) ")
                    npc_player = NPC(difficulty)
                    new_game.add_players(npc_player)
                else:
                    new_game.add_players(player)
                start += 1
            print("Let the games begin")
            new_game.start_game(new_game.current_players)
        elif player_count > 4:
            print("Sorry! That is too many players. The game will crash now")
    elif answer.lower() == 'No'.lower():
        print("Okay! We tried :( Just know I could've beaten you with half my power!)")
    else:
        print("""So you don't know wha to say? Well I will say it for you. Thank You come again!
              Don't forget to leave a 5 star rating on Yelp""")


if __name__ == '__main__':
    main()

