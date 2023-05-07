import random
import time
from betatestinglist import Categories
import re

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

class TrainingMemory:
    def mode():
        w_t = input("Would you like to practice with words or numbers (w or n)")
        if w_t == 'w':
            w1 = str(input("Would you like to memorize words with 3-5 letters, 6-8 letters, or 9-15 letters? Respond with 3, 6, or 9."))
            w2 = str(input("Would you like to memorize the word in 2 seconds, 5 seconds, or 8 seconds? Respond with 2, 5, or 8."))
            mode = ('wee' if w1 == str(3) and w2 == str(8) else 'wem' if w1 == str(3) and w2 == str(5) else 'weh' if w1 == str(3) and w2 == str(2) 
                    else 'wme' if w1 == str(6) and w2 == str(8) else 'wmm' if  w1 == str(6) and w2 == str(5) else 'wmh' if w1 == str(6) and w2 == str(2)
                    else 'whe' if w1 == str(9) and w2 == str(8) else 'whm' if w1 == str(9) and w2 == str(5) else 'whh' if w1 == str(9) and w2 == str(2)
                    else 'insane words')
            return mode
        else:
            w3 = str(input("Would you like to memorize the order of 3-5 numbers, 6-9 numbers, or 10-11 numbers? Response with 3, 6, or 10."))
            w4 = str(input("Would you like to memorize the numbers in 3 seconds, 6 seconds, or 9 seconds? Respond with 3, 6, or 9."))
            mode = ('nee' if w3 == str(3) and w4 == str(9) else 'nem' if w3 == str(3) and w4 == str(6) else 'neh' if w3 == str(3) and w4 == str(3) 
                    else 'nme' if w3 == str(6) and w4 == str(9) else 'nmm' if  w3 == str(6) and w4 == str(6) else 'nmh' if w3 == str(6) and w4 == str(3)
                    else 'nhe' if w3 == str(10) and w4 == str(9) else 'nhm' if w3 == str(10) and w4 == str(6) else 'nhh' if w3 == str(10) and w4 == str(3)
                    else 'insane numbers')
            return mode

    def file(mode):
        l_3_5 = []
        l_6_8 = []
        l_9_15 = []
        if re.search("^w.", mode):
            if mode[1] == 'h':
                with open("9-15.txt", "r") as f_9_15:
                    for words in f_9_15:
                        l_9_15.extend(words.split(", "))
                        return l_9_15
            elif mode[1] == 'm':
                with open("6-8.txt", "r") as f_6_8:
                    for words in f_6_8:
                        l_6_8.extend(words.split(", "))
                        return l_6_8
            elif mode[1] == 'e':
                with open("3-5.txt", "r") as f_3_5:
                    for words in f_3_5:
                        l_3_5.extend(words.split(", "))
                        return l_3_5
        elif mode == 'insane words':
            with open("9-15.txt", "r") as f_9_15:
                for words in f_9_15:
                    l_9_15.extend(words.split(", "))
            with open("6-8.txt", "r") as f_6_8:
                for words in f_6_8:
                    l_6_8.extend(words.split(", "))
            with open("3-5.txt", "r") as f_3_5:
                for words in f_3_5:
                    l_3_5.extend(words.split(", "))
            combined = []
            combined.extend(l_9_15)
            combined.extend(l_6_8)
            combined.extend(l_3_5)
            return combined
        else:
            return None

    def training_exercise(mode):
        keep = input("Would you like to start? Type (y/n)")
        count = 0
        wrong = 0

        # print statements indicating the mode
        if mode[1] == 'e':
            (print(f"Your mode is easy.") if mode[2] == 'e' 
            else print(f"Your mode is easy with a medium emphasis on time.") if mode[2] == 'm' 
            else print(f"Your mode is easy with a hard emphasis on time."))
        elif mode[1] == 'm':
            (print(f"Your mode is medium with an easy emphasis on time.") if mode[2] == 'e' 
            else print(f"Your mode is medium.") if mode[2] == 'm' 
            else print(f"Your mode is medium with a hard emphasis on time."))
        elif mode[1] == 'h':
            (print(f"Your mode is hard with an easy emphasis on time.") if mode[2] == 'e' 
            else print(f"Your mode is hard with a medium emphasis on time.") if mode[2] == 'm' 
            else print(f"Your mode is hard."))
        else:
            print("You have messed up while inputting your responses to the prior questions about difficulty mode and time.")
            print("As a result, you've automatically been signed up for insane mode lol, do better")


        if mode[0] == 'n' or mode == 'insane numbers':
            n5 = ([1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1])
            n9 = ([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]) 
            n11 =([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            insanen = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            insanen.extend(n5)
            insanen.extend(n9)
            insanen.extend(n11) 
            
            while keep != "n":
                number = ''
                digits = (random.choice(n5) if mode[1] == 'e' else random.choice(n9) if mode[1] == 'm'
                            else random.choice(n11) if mode[1] == 'h' else random.choice(insanen))
                for i in digits:
                    number += str(random.randint(0, 9))
                printed_number = int(number)
                print(f"The number is {printed_number}.")
                if mode[2] == 'e':
                    time.sleep(9)
                elif mode[2] == 'm':
                    time.sleep(6)
                elif mode[2] == 'h':
                    time.sleep(3)
                else:
                    time.sleep(random.randint(2,12))
                print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                answer = int(input("What number did you see?"))
                
                if mode != "insane numbers":
                    if answer == printed_number:
                        print(f"Good job! You got it right!")
                        print(f"\n")
                        count += 1
                        keep = input("Would you like to keep going? (y/n)")
                    else:
                        print(f"Nice try! The answer is {printed_number}")
                        print(f"\n")
                        wrong += 1
                        keep = input("Would you like to keep going? (y/n)")
                else:
                    if answer == printed_number:
                        print("FRAUD ALERT. You got extremely lucky; I just want you know that. \n")
                        count += 1
                        keep = input("I really hope you quit! It's excruciating watching you hahahahahhahahaha. Are you still going? (y/n)")
                    else:
                        print(f"HAHA you suck. The correct number is {printed_number}, but even with a lot of practice, you wouldn't be able to get that. \n")
                        wrong += 1
                        keep = input("You should quit, you're not going to get anywhere. Are you going to continue? (y/n)")
        else:
            l = TrainingMemory.file(mode)     
            while keep != "n":
                word = random.choice(l)
                print(f"Your word is {word}")
                if mode[2] == 'e':
                    time.sleep(8)
                elif mode[2] == 'm':
                    time.sleep(5)
                elif mode[2] == 'h':
                    time.sleep(2)
                else:
                    time.sleep(random.randint(1,3))
                print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                ans = str(input("What word did you see?"))
                if ans == word:
                    if mode != 'insane words':
                        print(f"Good job! You got it right!")
                        keep = input("Would you like to keep going? (y/n)")
                    else:
                        print(f"Aren't you a lucky bastard. Won't happen again.")
                        keep = input("I hope you quit. Are you going to continue? (y/n)")
                    count += 1
                else:
                    if mode != 'insane words':
                        print(f"Aw, nice try! You can still do this! Keep practicing! The correct answer was {word}.")
                        keep = input("Would you like to keep going? (y/n)")
                    else:
                        print(f"HAHA, not surprised. ")
                        keep = input("PLEASE QUIT, the sight of failure makes me want to throw up. Are you going to continue (y/n)?")
                    wrong += 1

        if mode[0] == 'w' or mode[0] == 'n':
            print("\n")
            print(f"Nice session. Make sure to keep practicing!")
            print(f"Here are your stats: \n")
            print(f"Mode: {mode}")
            print(f"Guessed correct: {count}")
            print(f"Guessed incorrect: {wrong}")
            print(f"Percentage and total: {round(((count)/(count+wrong))*100, 2)}% correct, {count+wrong} words/numbers \n")
            print("Have a great day!")
        else:
            print("\n")
            if (count) / (count + wrong) == 1 and count > 5:
                print(f"You know what. I'll give it to you, you did an ok job.")
                time.sleep(1)
                print(f"Actually, you probably cheated but I couldn't care less to find out. you're not that important.")
                print(f"You got {count} words/numbers right.")
            elif (count) / (count + wrong) == 1 and count < 6:
                print(f"wtf was the point of 'training' when you barely did anything. garbage work ethic. i'm not going to give you any stats, get out of here.")
            else:
                print(f"Finally you're done. I knew you were gonna quit soon. It was unbearable watching you try.")
                print(f"Here are your crappy stats: \n")
                print(f"Mode: {mode}")
                print(f"Lucky Guess(es): {count}")
                print(f"Expected Incorrect Guesses: {wrong}")
                print(f"Percentage and total: {round(((count)/(count+wrong))*100, 2)}% correct, {count+wrong} words/numbers")

def main():
    print("Welcome to our project 'Concentration 64'. We offer two modes: Memory Training and the Game. Which would you like to do? (1/2)")
    print("Option 1: Training\nOption 2: Concentration 64")
    
    which_mode = (input("Answer: "))

    if which_mode == '1':
        modes = TrainingMemory.mode()
        TrainingMemory.training_exercise(modes)
    elif which_mode == '2':
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
                new_game.start_game(new_game.player_list)
    
                new_game.start_game(new_game.player_lists)
    
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