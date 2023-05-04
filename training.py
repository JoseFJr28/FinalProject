import time
import random

#demo stages of method, will insert into class and also import list of words from a separate file for the final project
words = ['hill', 'vein', 'queen', 'deafening','malicious', 'womanly', 'busy', 'calculate', 'thrill', 'tenuous', 'melt' 'paltry', 'first', 'own', 'sock'
         ,'rifle', 'cause', 'peaceful', 'arithmetic', 'disillusioned', 'quaint', 'detail', 'rock', 'clap', 'settle', 'tie', 'various', 'property', 'elephant','sloth'] 


def mode():
    """ Function that determines the mode for training
    
    Attributes:
        res (str): number of seconds that user inputs to determine the mode of difficulty
    """
    res = int(input(f"Would you like to 10 seconds, 7 seconds, or 3 seconds to memorize the word? Respond with num only."))
    if res == int("10"):
        mode = "Easy"
    elif res == int("7"):
        mode = "Medium"
    else:
        mode = "Hard"
    return mode

def training(mode):
    keep = input("Would you like to start? Type y")
    count = 0
    wrong = 0
    if mode == "Easy":
        print(f"Your mode is Easy")
        while keep != "n":
            word = random.choice(words)
            print(f"Your word is {word}")
            time.sleep(9)
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            ans = input("What word did you see?")
            if ans == word:
                print(f"Good job! You got it right!")
                keep = input("Would you like to keep going? y or n")
                count += 1
            else:
                print(f"Nice try! The answer is {word}")
                wrong += 1
                keep = input("Would you like to keep going? y or n")
    elif mode == "Medium":
        print(f"Your mode is Medium \n")
        while keep != "n":
            word = random.choice(words)
            print(f"Your word is {word}")
            time.sleep(6)
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            ans = input("What word did you see?")
            if ans == word:
                print(f"Good job! You got it right!")
                keep = input("Would you like to keep going? y or n")
                count += 1
            else:
                print(f"Nice try! The answer is {word}")
                wrong += 1
                keep = input("Would you like to keep going? y or n")     
    else:
        print(f"Your mode is Hard \n")
        while keep != "n":
            word = random.choice(words)
            print(f"Your word is {word}")
            time.sleep(2)
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            ans = input("What word did you see?")
            if ans == word:
                print(f"Good job! You got it right!")
                count += 1
                keep = input("Would you like to keep going? y or n")
            else:
                print(f"Nice try! The answer is {word}")
                wrong += 1
                keep = input("Would you like to keep going? y or n")
    print(f"Nice session. You've got {count} words right and {wrong} words wrong! Keep practicing your memory training!")
    
training(mode())
            
    
        
        
    