import random
import time
from betatestinglist import Categories

class Concentration:
    
    def __init__(self):
        self.player_list = []
        self.managewords = set()
        
    def __repr__(self):
        return f"{self.player_list}"
    
    def clap_mode(self):
        time.sleep(0.5)
        print("clap")
        time.sleep(0.5)
        print("clap")
        time.sleep(0.5)
        print("clap")
    
    def sequence(self, placement):
        if placement == 1:
            return f"first"
        elif placement == 2:
            return f"second"
        elif placement == 3:
            return f"thrid"
        elif placement == 4:
            return f"fourth"
    
    def start_game(self):
        game_order = self.order(self.player_list)
        print(game_order)
        
        print(f"Concentration!")
        self.clap_mode()
        print("Sixty-four!")
        self.clap_mode()
        print("No repeats!")
        self.clap_mode()
        print("Or hesitations!")
        self.clap_mode()
        
        count = 0
        length = len(game_order)
        placement = 1
        x = 0
        while count < length:
            print(f"I, {game_order[x]}, will go {self.sequence(placement)}")
            self.clap_mode()
            placement += 1
            x += 1
            count += 1
        self.round_start(game_order)
    
    def round_start(self,player_list):
        round = Concentration()
        category = input(("Category is: "))
        
        if "Sheldon" in player_list:
            #npc,difficulty,category
            'Sheldon'.handicap_npc('Sheldon', 'Sheldon'.difficulty, category)
            'Sheldon'.npc_reader('Sheldon'.difficulty, category)
        count = 0
        infinite = 0
        #Sidenote: make sure categories can be tpyed in upper/lowercase
        words = Categories.get(category)
        
        length2 = 0
        for x in Categories:
            if x.lower() == category.lower():
                length2 += len(Categories.get(category))
        limit = 5
        t1 = time.time()
        #figureout to access values and have them equal lower case as well
        while count < length2 and infinite < len(player_list):
                
                print("You have 5 seconds to provie an answer")
                word = input(f"{player_list[infinite]} type your word: ")
                
                if word not in round.managewords and word in words or time.time() - t1 < limit:
                    round.managewords.add(word)
                    print(round.managewords)
                    player_list[infinite].words.add(word)#has no attribute
                    print(player_list[infinite].words)
                    # self.check_words(round.managewords, player_list[infinite].words)
                else:
                    print(f"{player_list[infinite]} you provided a used word or you ran out of time.")
                    self.round_over(player_list[infinite], player_list)
                    if self.is_there_a_winner(player_list):
                        self.game_over(player_list)
                        break
                    else: 
                        self.round_start(player_list)
                        
                infinite += 1
                count += 1
            
                if infinite == len(player_list):
                    infinite = 0
                else:
                    continue
    
    def round_over(self, player, player_list):
        player.ingame = False
        if player in player_list:
            player_list.remove(player)
            # print(f"{player} has been elminated")
        return self.is_there_a_winner(player_list)
    
    def is_there_a_winner(self, player_list):
        current = len(player_list)
        if current == 1:
            return True
        else:
            return False
        
    def game_over(self, player_list):
        return print(f"Player {player_list[0]} is your winner")
        
    
    def add_players(self, player_obj):
        self.player_list.append(player_obj)
    
    def player_status(self, player_list, player):
        if player.ingame == False:
            return f"Sorry Player {player} is not in the game"
        else:
            return f'The current players are still in the game: {player_list}'
            
    def order(self,player_list):
        player = len(player_list)
        order = random.sample(player_list, k= player)
        return order
    
    def timer(self, player,player_list):
        '''
        This method controls the timer in the game 
        it gives the players a certain amount of time to make a guess
        '''
        limit = 30
        t1 = time.time()
        while time.time()- t1 < limit:
            if t1 <= limit: 
                continue
            else: 
                t1 > limit
                self.round_over(player, player_list)
                return f"You hestitated, {player} is eliminatined"
    
    def check_words(self, game_words, player_words):
        self.game_words = game_words
        x = set(game_words.managewords)
        y = set(player_words.words)
        z = x & y
        print(z)
        

class Player:
    
    def __init__(self, name, ingame = True):
        self.name = name
        self.ingame = ingame
        self.words = set()
    
    def __repr__(self):
        return f"{self.name}"

class NPC:
    """
    
    Attributes:
        difficulty (str): The difficulty of the the npc
        npc_name(str): the name of the computer, default value of Sheldon
        score(int): the score for the npc
    """
    def __init__(self, difficulty, brain = 0, npc_name= "Sheldon"):
        """
        Initilizes the difficulty the computer will be in
        
        Args:

        """
        self.difficulty = difficulty
        self.brain = brain
        self.npc_name = npc_name
        self.head = set()
        self.usedwords = set()
    
    
    def __repr__(self):
        """
        This will print out hte NPC name and provide the current score 
        """
        return f"{self.npc_name}"   
    
    def handicap_npc(self,npc, difficulty, category):
        """
        Will give a handicap to the NPC on how "smart" it is;
        Args:
            difficulty(str): The difficulty for the npc
            dict(dictionary of list): a dictionary of list with the categories
            brain(int)= the amount of words it can remember
        Returns:
            if self.difficulty == lower("easy") and word_count >= 20 and word_count <= 30:
                return brain = random(1,11)
            elif  self.difficulty == lower("intermediate") and word_count > 30 and word_count <= 50:
                return brain = random(1, 20)
            elif self.difficulty == lower("hard") and word_count > 50 and word_count <= 100:
                return brain = random(30, 50)
            else:
                return brain = word_count
        """
        if difficulty.lower() == 'easy'.lower():
            return npc.brain == random.randrange(1,11)
        elif difficulty.lower() == 'medium'.lower():
            return random.randrange(1,20)
        elif difficulty.lower() == 'hard'.lower():
            return random.randrange(30,50)
        elif difficulty.lower() == 'impossible'.lower():
            return npc.bain == len(Categories.get(category))
        else:
            return f"That difficulty is not available"        

    
    
    def npc_reader(self, npc_obj,category):
        """
        Will read the file and from there will see what difficulty of the npc
        and return a list of the words the computer will know. The words will be
        chosen at random
        
        Ars:
           difficulty(str): difficulty of the npc
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
            if len(npc_obj.head) != npc_obj.brain:
                newcount = 0
    #Now as we go through the restricted number of words to know    
                while newcount < npc_obj.brain and len(npc_obj.head) < npc_obj.brain:
                    #we pick a random number from the size of the available words
                    pick = random.randrange(length)
    #Access the words the itself
                    for x in Categories.get(category):
    #We make sure the random number is the key we want and its not in the list and 
    #the word is not in the list( to prevent repeats) we add it
                        if x == pick and x not in npc_obj.head:
                            npc_obj.head.add(Categories[category][x])
                        else:
                            continue
                #prevents the infinite loop            
                    newcount += 1

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
            difficulty = input("what difficulty would you prefer to play? (Easy/Medium/Hard/Impossible) ")
            npc_player = NPC(difficulty)
            new_game.add_players(player1)
            new_game.add_players(npc_player)
            print("Let the games begin")
            new_game.start_game(new_game.players_list)
        elif player_count > 1 and player_count <= 4:
            start = 0
            while start < player_count:
                player_name = input("What's your name? ")
                if player_name == 'npc':
                    difficulty = input("what difficulty would you prefer to play? (Easy/Medium/Hard/Impossible) ")
                    npc_player = NPC(difficulty)
                    new_game.add_players(npc_player)
                else:
                    new_game.add_players(Player(player_name))
                start += 1
            print("Let the games begin")
            new_game.start_game()
        elif player_count > 4:
            print("Sorry! That is too many players. The game will crash now")
    elif answer.lower() == 'No'.lower():
        print("Okay! We tried :( Just know I could've beaten you with half my power!)")
    else:
        print("""So you don't know wha to say? Well I will say it for you. Thank You come again!
              Don't forget to leave a 5 star rating on Yelp""")


if __name__ == '__main__':
    main()


# p1 = Player("Joe")
# p2 = Player("Rob")
# p3 = Player("Lucy")
# p4 = Player("Lucky")
# new_game = Concentration()

# new_game.add_player(p1)
# new_game.add_player(p2)
# new_game.add_player(p3)
# new_game.add_player(p4)


# # print(new_game)

# print(new_game.player_status(new_game.player_list, p1))

# print(new_game.order())