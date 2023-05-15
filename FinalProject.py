from argparse import ArgumentParser
from matplotlib import pyplot as plt
import csv
import random
import json
import sys
import time
import pandas as pd
import re

class Player:
    """
    A class that is used to instantiate each player object. The object is creaated with a 
    name, an empty set to store the used words, and a score that is used for the leaderboard and visualization.
    
    Author(s): John
    Technique: Optional parameter(s)
    
    
    Args:
        name (str): The name of the player
        words (set): A set of the words that the player has used
        score (int): The score of the player default to 0
        

    """
    def __init__(self, name, score = 0):
        self.name = name
        self.words = set()
        self.score = score
    
    def __repr__(self):
        """
        An informal string representation of the player object's name that is 
        returned so that the player's name can be used throughout the program for scoring
        and game status.
        
        Author(s): John
        Technique: Magic methods
        
        Returns:
                player's name as a string representation
        """
        return f"{self.name}"

class TrainingMemory:
    """
    
    Author: Adithya
    """
    def mode():
        """
        
        Author(s): Adithya
        """
        w_t = input("Would you like to practice with words or numbers (w or n) ")
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
        """
        Author(s): Adithya
        Requirement: with statements
        """
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
        """
        Author(s): Adithya
        Technique: f-strings containing expressions
        """
        keep = input("Would you like to start? Type (y/n) ")
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
            # Thought randomint() only applied to single-digit 0-9 so used this technique to get multiple digits, 
            # but decided to keep this as it was my solution before I realized randomint() was a solution
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
                        keep = input("Would you like to keep going? (y/n) ")
                    else:
                        print(f"Nice try! The answer is {printed_number} ")
                        print(f"\n")
                        wrong += 1
                        keep = input("Would you like to keep going? (y/n)")
                else:
                    if answer == printed_number:
                        print("FRAUD ALERT. You got extremely lucky; I just want you know that. \n")
                        count += 1
                        keep = input("I really hope you quit! It's excruciating watching you hahahahahhahahaha. Are you still going? (y/n) ")
                    else:
                        print(f"HAHA you suck. The correct number is {printed_number}, but even with a lot of practice, you wouldn't be able to get that. \n")
                        wrong += 1
                        keep = input("You should quit, you're not going to get anywhere. Are you going to continue? (y/n) ")
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
                if ans.lower() == word.lower():
                    if mode != 'insane words':
                        print(f"Good job! You got it right!")
                        keep = input("Would you like to keep going? (y/n) ")
                    else:
                        print(f"Aren't you a lucky bastard. Won't happen again.")
                        keep = input("I hope you quit. Are you going to continue? (y/n) ")
                    count += 1
                else:
                    if mode != 'insane words':
                        print(f"Aw, nice try! You can still do this! Keep practicing! The correct answer was {word}.")
                        keep = input("Would you like to keep going? (y/n)")
                    else:
                        print(f"HAHA, not surprised. ")
                        keep = input("PLEASE QUIT, the sight of failure makes me want to throw up. Are you going to continue (y/n)? ")
                    wrong += 1

        if mode[0] == 'w' or mode[0] == 'n':
            print("\n")
            print(f"Nice session. Make sure to keep practicing!")
            print(f"Here are your stats: \n")
            print(f"Mode: {mode} ")
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

class Leaderboard:#Under Maintanence
    """
    Will display the leaderboard with the players score
    
    Author: Mo
    """
    ''
    def __init__(self, name, score, category, filepath = 'leaderboard.csv'):
        self.name = name
        self.score = score
        self.category = category
        self.filepath = filepath
        
    'Writes the players score onto a csv file'
    def record_score(self):
        
        data = []
        data.append([self.name, self.score, self.category])
        
        with open(self.filepath, 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Score', 'Category'])
            
            for row in data:
                writer.writerow(row)
        
    'Displays leaderboard'
    "Technique: filtering operations on Panda DataFrames"
    def leaderboard(self):
        data = pd.read_csv(self.filepath)
        data = data["Score"] > 2
        # data = data.groupby("Name")
        print(data)
        
    'Displays Score Distribution'
    "Technique: Visualizing data with pyplot"
    def score_distribution(self):
        names = []
        scores = []
        categories = []
        
        with open(self.filepath, mode='r') as scores_file:
            score_reader = csv.reader(scores_file)
            for row in score_reader:
                names.append(row[0])
                scores.append(row[1])
                categories.append(row[2])
                
        fig, ax = plt.subplots()
        ax.bar(names, scores)
        ax.set_xlabel('Names')
        ax.set_ylabel('Scores')
        ax.set_title('Scores by Category')
        ax.set_xticklabels(categories)
        plt.show()

class Concentration:
    """
    The main game itself. Concetration 64! It initilizes the game adn keep 
    tracks of the players and words being used. Time is alos a factor.
    
    Attributes:
        player_list (list of Human Players): The current players of the game
        game_list(list of Human Players): The players for the game after a winner is determined
        managewords(set of str): The words used in the game
    
    Author(s): Jose, Adithya, Mo, John, and Melissa
    """
    
    def __init__(self):
        self.player_list = []
        self.game_list = []
        self.managewords = set()
        
    def __repr__(self):
        """
        Provides a readable representation of the player object(s) when the 
        game runs. Returns the names of the players in a list.
        
        Author: John
        
        
        Returns:
            player_list(str): A string representation of the player list
        """
        return f"{self.player_list}"
    
    def clap_mode(self):
        """
        
        
        Author: Melissa
        """
        time.sleep(0.5)
        print("clap")
        time.sleep(0.5)
        print("clap")
        time.sleep(0.5)
        print("clap")
    
    def sequence(self, placement):
        """
        Establishes the order of each player's turn when the game is running
        
        
        Args:
               placement(int): a numerical value that tracks the players placement 
               in the game
        
        Returns:
                player placement as a string
                
        Author(s): John
        
        """
        if placement == 1:
            return f"first"
        elif placement == 2:
            return f"second"
        elif placement == 3:
            return f"thrid"
        elif placement == 4:
            return f"fourth"
    
    def start_game(self, player_list, filepath):
        """
        This method starts the game and prints out each message to display the
        beginning of the round and accounts for the game starting.
        
        Author(s): Mo
        
        """
        game_order = self.order(player_list)
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
        self.round_start(game_order, filepath)
    
    def round_start(self,player_list,filepath):
        """
        Starts and manages the round with keeping track of the players in the 
        player_list and makes sure words are not repeated
        
        
        Args:
            player_list(List of Players): the current players
            
        Side Effects:
            Updates the games managewords set and the Players word if valide word
            If the word is not valid then the player gets removed from the games
            current players list
        
        Author(s): Jose
        Technique: Use of json.load() and compostion between two class
        """
        round = Concentration()
        with open(filepath, "r", encoding="utf-8") as file:
            options = json.load(file)
        
        category = input(("Category is (NBA [from 2010-11]/Occupations/Animals/Card Games/Fruits): "))
        
        #Handles the case sensitivty
        valid_category = self.category_adjuster(category, options)
        

        count = 0 #Manages the amount of times we put in words
        infinite = 0 #Manages going through the players through their turn
        
        #Gets the values of the keys
        words = options.get(valid_category)
        
        #Gets the length of how many words are available for that category
        length2 = 0
        for x in options:
            if x.lower() == valid_category.lower():
                length2 += len(options.get(valid_category))
        
        #Limit for how long a person has to answer        
        limit = 10
        t1 = time.time()
    
        
        #As long as their are still enough words in the list
        while count < length2 and infinite < len(player_list) and time.time() - t1 < limit:
            
            print("You have 5 seconds to provie an answer")
            word = input(f"{player_list[infinite]} type your word: ")
            
            
            checklist = words
            
            #We put all the values into a list
            valid_words = self.convert_dict(checklist)
            
            #Check if the word is in the list, so a valid word
            crash = self.check_vw(word.lower(), valid_words)
            
            #If the word was not valid
            if crash:
                
            #takes the given word and puts it into a set
                given_word = set()
                given_word.add(word)
                
            #checks whether the word provided is a repeat before adding to 
            #set of the managewords
                question = self.check_words(round.managewords, given_word)
                
                
                #now adds to managewords for next player
                round.managewords.add(word)
            
            #the results from question either True or False  
                if question:
                    #Tells the player the word is already used
                    print(f"{player_list[infinite]} you provided a used word")
                    #Stops the round and removes the player
                    players = self.round_over(player_list[infinite], player_list)
                    #Checks if only one player left
                    if self.is_there_a_winner(players):
                        #The game is officially over announcing the winner and score
                        self.game_over(players)
                        play_again = input("Would you, the player(s) like to play again? (Y/N) ")
                        if play_again.lower() == 'Y'.lower():
                            main(filepath)
                    elif play_again.lower() == 'N'.lower() :
                        print("Well hopefully you come back!"
                        "\nDon't forget to leave a 5 star review on Yelp!")
                            
                    else: 
                        #if player count is 2 or more we restart the round with new or same category
                        self.round_start(player_list, filepath)
                else:
                    #Not repaeated word and valid then add to players wors
                    player_list[infinite].words.add(word)
                    #Allows to go to the next player         
                    infinite += 1
                    #Keeps going until there are no more words to count
                    count += 1
                    #makes it go through each player more than once until the player
                    #breaks a rule
                    if infinite == len(player_list):
                        infinite = 0
                    else:
                        continue
                
            elif not crash:
                #the word was invalid
                print(f"{player_list[infinite]} you provided an invalid word.")
                players = self.round_over(player_list[infinite], player_list)
                if self.is_there_a_winner(players):
                    self.game_over(players)
                    play_again = input("Would you, the player(s) like to play again? (Y/N) ")
                    if play_again.lower() == 'Y'.lower():
                        main(filepath)
                    elif play_again.lower() == 'N'.lower() :
                        print("Well hopefully you come back!"
                        "\nDon't forget to leave a 5 star review on Yelp!")
                        
                else: 
                    self.round_start(player_list, filepath)
                        
        if count == length2:
            print(f"We ran out of words....so....game over you guys are too smart")
            print("Well hopefully you come back!"
            "\nDon't forget to leave a 5 star review on Yelp!")
        else:
            pass

    def category_adjuster(self, category, options):
        """
        Resolves the case sensitivty for the category the player chooses
        Args:
            category(str): The users choice of category given from the list
            options(json file): the '
        
        Author(s): Jose
        """
        for x in options.keys():
            if x.lower() == category.lower():
                category = x
                return category
            else:
                continue

    def round_over(self, player, player_list):
        """
        
        Author(s): Mo
        """
        score = len(player.words)
        update_players = []
        player.score = score
        if player in player_list and len(player_list) > 1:
            player_list.remove(player)
            update_players = player_list
        else:
            update_players = player_list
        return update_players
    
    def is_there_a_winner(self, player_list):
        """
            
        Author(s): Melissa
        Technique: conditional expression
        """
        current = len(player_list)
        return True if current == 1 else False
        
    def game_over(self, player_list):
        """
        
        Author(s): 
        """
        score = len(player_list[0].words)
        player_list[0].score += score
        return print(f"Player {player_list[0]} is your winner with a score of {player_list[0].score}")     
    
    def add_players(self, player_obj):
        """
       
        Author(s): 
        """
        self.player_list.append(player_obj)
  
    def add_to_game(self, player_obj):
        """
        Author(s):
        """
        self.game_list.append(player_obj)     
     
    def order(self,player_list):
        """
        Provides the order the players will go
        
        Args:
            player_list(list of Players): the current players
        Returns:
            the order of who goes 1st, 2nd, 3rd, and 4th
        Authro(s): Jose
        """
        player = len(player_list)
        order = random.sample(player_list, k= player)
        return order 

    def check_words(self, game_words, player_words):
        """
                   
        Author(s): Melissa
        Technique: Set operations on sets
        """
        x = game_words
        y = player_words
        a = x.intersection(y)
        size = len(a)
        return True if size == 1 else False
    
    def check_vw(self,word, word_list):
        """
        Checks if the word is in the list
        Args:
            word(str): the word given by the player
            word_list(list of words): The valid words
        Returns:
            True if its a valid option, otherwise False
        Author: Adithya
        """
        return True if word in word_list else False
     
    def convert_dict(self, dict):
        """
        This method takes the words that are guessed by the player and checks 
        whether they are already in the dictionary or not. It returns a list of 
        valid words that can be used
        Args:
            dict(the categories): the keys of the dictionaries 
        
        Author(s): Mo
        Technique: comprehensions, list comprehensions
        """
        temp = dict.values()
        temp2 = [f'{x.lower()}' for x in temp]
    
        valid_words = [f"{word.lower()}" for word in temp2]
        return valid_words

def main(filepath):
    """
    What runs the program and provides the functionality for the program to run
    Author(s): Jose, Adithya, Mo, John, and Melissa
    """
    print("Welcome to our project 'Concentration 64.py'. We offer two modes: Memory Training and the Game. Which would you like to do? (1/2)")
    print("Option 1: Training\nOption 2: Concentration 64")
    
    which_mode = (input("Answer: "))

    if which_mode == '1':
        modes = TrainingMemory.mode()
        TrainingMemory.training_exercise(modes)
    elif which_mode == '2':
        new_game = Concentration()
        answer = input("Welcome To Concentration 64!!!! Ready to begin your"
                       " journey of fun (Y/N)? ")
        if answer.lower() == 'Y'.lower():
            print("Great! Let's begin!")
            player_count = int(input("How many players will be there? (2-4) "))
    
            if player_count > 1 and player_count <= 4:
                start = 0
                while start < player_count:
                    player_name = input("What's your name? ")
                    
                    score_update = input("Would you like to have a point advantage? (Y/N) ")
                    if score_update.lower() == 'Y'.lower():
                        new_score = input("How many points would you like? (1-10) ")
                        new_score = int(new_score)
                        if new_score >= 1 and new_score <= 10:
                            new_game.add_players(Player(player_name, new_score))
                            new_game.add_to_game(Player(player_name, new_score))
                            start += 1
                        else:
                            print("Sorry thats not within range, no points will"
                                  " be added")
                            new_game.add_players(Player(player_name))
                            new_game.add_to_game(Player(player_name))               
                            start += 1
                    else:          
                        new_game.add_players(Player(player_name))
                        new_game.add_to_game(Player(player_name))               
                        start += 1
                print("Let the games begin\nDisclaimer: Spelling does matter in this program :)")
                new_game.start_game(new_game.player_list, filepath)
            elif player_count > 4:
                print("Sorry! That is too many players. The game will crash now")
        elif answer.lower() == 'N'.lower():
            print("Okay! We tried :( Just know I could've beaten you with half my power!)")
        else:
            print("""So you don't know what to say? Well I will say it for you. Thank you, please come again!
                Don't forget to leave a 5 star rating on Yelp""")

def argesparse(arglst): 
    """
    Parse and validate command-line arguments.
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Author(s): Mo 
    Technique: The ArgumentParser class from the arparse module
    """
    
    parser = ArgumentParser()
    parser.add_argument('filepath', help="json file")
    setup = parser.parse_args(arglst)
    return setup

if __name__ == '__main__':
    calling = argesparse(sys.argv[1:])
    main(calling.filepath)
