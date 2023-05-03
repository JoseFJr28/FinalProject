import random
import sys
from argparse import ArgumentParser

"""
The following is a game called Concentration. You are able to play by yourself
or with the computer. The goal of the game is to name more object of the
category options. There are 4 modes: easy, intermediate, hard, and impossible.
"""

class Concentration:
    
    """This defines the game"""
    def __init__(self, game, player_list):
        self.game = game
        self.player_listt = player_list
        
    
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
    
    
    def handicap_npc(self, mode, npc):
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
        if mode.lower() == 'easy':
            return npc.brain == random.randrange(1,11)
        elif mode.lower() == 'medium':
            return npc.brain == random.randrange(1,20)
        elif mode.lower() == 'hard':
            return npc.brain == random.randrange(30,50)
        elif mode.lower() == 'impossible':
            return npc.brain == self.brain
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
    
    # def timer(self):
    #     start_time = time.time()
    #     response = time.time()
    #     time_lasp = start_time - response
    #     return time_lasp
    #     if time_lasp > avg_time():
    #         return f"You hestitated, {winner} wins"
    #     else():
            # pass

def argesparse(args):
    
    cmd_obj = ArgumentParser()
    cmd_obj.add_argument("name1", help="name1 is the Players name")
    cmd_obj.add_argument("npc1", help="The computer player")
    
    return cmd_obj.parse_args(args)
    
    
def main(name1, name2, name3, name4, npc_name = "Sheldon"):
    filenames = ['categories1.json', 'categories2.json']
    categories = load_words(filenames)

    players = [ComputerPlayer()] + [HumanPlayer(f'Human {i}') for i in range(1, 3)]

    while True:
        print("Choose a category:", ', '.join(categories.keys()))
        category = input().strip()

        if category not in categories:
            print("Invalid category. Please choose from the list.")
            continue

        for player in players:
            if isinstance(player, ComputerPlayer):
                word = player.choose_word(category, categories)
                print(f"{player.name} chose: {word}")
            else:
                word = player.choose_word()

            if player.is_eliminated(word):
                print(f"{player.name} is eliminated!")
                return
            else:
                player.update_used_words(word)

if __name__ == '__main__':
    args = argesparse(sys.argv[1:])
    main(args.filepath, args.name)


    